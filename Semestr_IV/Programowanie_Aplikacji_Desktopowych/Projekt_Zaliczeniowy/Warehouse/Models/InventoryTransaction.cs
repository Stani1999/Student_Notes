using System;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Warehouse.Models
{
    [BsonIgnoreExtraElements]
    public class InventoryTransaction
    {
        [BsonId]
        public ObjectId Id { get; set; }
        public ObjectId ProductId { get; set; }
        public string ProductName { get; set; } = string.Empty;
        public string TransactionType { get; set; } = string.Empty;
        public int QuantityChanged { get; set; }
        public DateTime Timestamp { get; set; }
        public string UserId { get; set; } = string.Empty;
    }
}