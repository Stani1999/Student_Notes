using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using Warehouse.Models;
using Warehouse.Services.Infrastructure;

namespace Warehouse.Services.Application
{
    public class ProductService
    {
        private readonly IMongoCollection<Product> _products;

        public ProductService(IMongoService mongoService)
        {
            _products = mongoService.GetCollection<Product>("Product");
        }

        public async Task<List<Product>> GetFilteredProductsAsync(string searchQuery, string categoryId, List<string> categoryIdsFromGroup, int skip, int limit)
        {
            var filters = new List<FilterDefinition<Product>>();

            if (!string.IsNullOrWhiteSpace(searchQuery))
            {
                var safeQuery = Regex.Escape(searchQuery);
                var regex = new BsonRegularExpression(safeQuery, "i");
                filters.Add(Builders<Product>.Filter.Or(
                    Builders<Product>.Filter.Regex(p => p.Name, regex),
                    Builders<Product>.Filter.Regex(p => p.Barcode, regex),
                    Builders<Product>.Filter.Regex(p => p.Description, regex)
                ));
            }

            bool isAllCategoriesOption = categoryId == "-- Wszystkie Kategorie --" ||
                                         categoryId == "-- Wszystkie Grupy --" ||
                                         categoryId == "-- Wszystkie --";

            if (!string.IsNullOrWhiteSpace(categoryId) && !isAllCategoriesOption)
            {
                filters.Add(Builders<Product>.Filter.Eq(p => p.CategoryId, categoryId));
            }
            else if (categoryIdsFromGroup != null && categoryIdsFromGroup.Count > 0)
            {
                filters.Add(Builders<Product>.Filter.In(p => p.CategoryId, categoryIdsFromGroup));
            }

            var combinedFilter = filters.Count > 0 ? Builders<Product>.Filter.And(filters) : Builders<Product>.Filter.Empty;

            return await _products.Find(combinedFilter)
                                  .Skip(skip)
                                  .Limit(limit)
                                  .ToListAsync();
        }

        public async Task AddProductAsync(Product product)
        {
            await _products.InsertOneAsync(product);
        }

        public async Task UpdateProductAsync(Product product)
        {
            var filter = Builders<Product>.Filter.Eq(p => p.Id, product.Id);
            await _products.ReplaceOneAsync(filter, product);
        }

        public async Task DeleteProductAsync(ObjectId id)
        {
            var filter = Builders<Product>.Filter.Eq(p => p.Id, id);
            await _products.DeleteOneAsync(filter);
        }

        public async Task<bool> IsBarcodeUniqueAsync(string barcode, ObjectId currentProductId)
        {
            if (string.IsNullOrWhiteSpace(barcode))
            {
                return true;
            }

            var filter = Builders<Product>.Filter.Eq(p => p.Barcode, barcode);

            if (currentProductId != ObjectId.Empty)
            {
                filter &= Builders<Product>.Filter.Ne(p => p.Id, currentProductId);
            }

            var count = await _products.CountDocumentsAsync(filter);
            return count == 0;
        }
    }
}