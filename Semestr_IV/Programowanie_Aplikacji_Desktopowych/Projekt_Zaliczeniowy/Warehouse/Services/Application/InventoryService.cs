using System.Threading.Tasks;
using MongoDB.Driver;
using Warehouse.Models;
using Warehouse.Services.Infrastructure;

namespace Warehouse.Services.Application
{
    /// <summary>
    /// Manages the inventory lifecycle using an append-only ledger pattern.
    /// Ensures the materialized view (Product.Quantity) is kept in sync with historical truth.
    /// </summary>
    public class InventoryService
    {
        private readonly IMongoCollection<InventoryTransaction> _transactions;
        private readonly IMongoCollection<Product> _products;

        public InventoryService(IMongoService mongoService)
        {
            _transactions = mongoService.GetCollection<InventoryTransaction>("InventoryTransaction");
            _products = mongoService.GetCollection<Product>("Product");
        }

        public async Task LogTransactionAsync(InventoryTransaction transaction)
        {
            await _transactions.InsertOneAsync(transaction);

            var update = Builders<Product>.Update.Inc(p => p.Quantity, transaction.QuantityChanged);
            var filter = Builders<Product>.Filter.Eq(p => p.Id, transaction.ProductId);

            await _products.UpdateOneAsync(filter, update);
        }
    }
}