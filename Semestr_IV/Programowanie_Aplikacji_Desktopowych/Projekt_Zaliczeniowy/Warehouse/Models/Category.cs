using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Warehouse.Models
{
    [BsonIgnoreExtraElements]
    public class Category
    {
        [BsonId]
        public ObjectId InternalId { get; set; }

        [BsonElement("Id")]
        public string Id { get; set; } = string.Empty;

        public string Group { get; set; } = string.Empty;

        public string Name { get; set; } = string.Empty;
    }
}