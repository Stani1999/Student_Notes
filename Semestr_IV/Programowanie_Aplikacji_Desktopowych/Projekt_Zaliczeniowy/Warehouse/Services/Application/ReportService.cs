using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MongoDB.Driver;
using Warehouse.Models;
using Warehouse.Services.Infrastructure;

namespace Warehouse.Services.Application
{
    public class ReportService
    {
        private readonly IMongoCollection<InventoryTransaction> _transactions;

        public ReportService(IMongoService mongoService)
        {
            _transactions = mongoService.GetCollection<InventoryTransaction>("InventoryTransaction");
        }

        public async Task<List<InventoryReportRow>> GetMonthlyReportAsync(int year, int month)
        {
            var startDate = new DateTime(year, month, 1, 0, 0, 0, DateTimeKind.Utc);
            var endDate = startDate.AddMonths(1);

            var filter = Builders<InventoryTransaction>.Filter.And(
                Builders<InventoryTransaction>.Filter.Gte(x => x.Timestamp, startDate),
                Builders<InventoryTransaction>.Filter.Lt(x => x.Timestamp, endDate)
            );

            var transactions = await _transactions.Find(filter).ToListAsync();

            foreach (var t in transactions)
            {
                if (string.IsNullOrWhiteSpace(t.ProductName))
                {
                    t.ProductName = "Nieznany Produkt (Brak Nazwy w Logu)";
                }
            }

            var report = transactions
                .GroupBy(t => t.ProductName)
                .Select(g => new InventoryReportRow
                {
                    ProductName = g.Key,
                    Received = g.Where(t => t.TransactionType == "IN").Sum(t => t.QuantityChanged),
                    Issued = System.Math.Abs(g.Where(t => t.TransactionType == "OUT").Sum(t => t.QuantityChanged))
                })
                .OrderBy(r => r.ProductName)
                .ToList();

            return report;
        }
    }
}