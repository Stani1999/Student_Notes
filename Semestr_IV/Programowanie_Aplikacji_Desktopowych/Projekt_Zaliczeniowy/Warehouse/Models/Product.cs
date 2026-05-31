using System.Collections.Generic;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using Warehouse.Models.Types;

namespace Warehouse.Models
{
    [BsonIgnoreExtraElements]
    public class Product
    {
        [BsonId]
        public ObjectId Id { get; set; }
        public string Barcode { get; set; } = string.Empty;
        public string Name { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public string CategoryId { get; set; } = string.Empty;
        public int Quantity { get; set; }
        public Price Price { get; set; } = new(); 
        public Measurand Measurand { get; set; } = new();
        public byte[]? ImageData { get; set; }
        public byte[]? LabelImageData { get; set; }
        public string ExtractedLabelText { get; set; } = string.Empty;
    }
}