using MongoDB.Driver;

namespace Warehouse.Services.Infrastructure
{
    /// <summary>
    /// Concrete implementation of the MongoDB connection service.
    /// Initializes the MongoClient and connects to the specified database instance.
    /// </summary>
    public class MongoService : IMongoService
    {
        private readonly IMongoDatabase _database;

        public MongoService()
        {
            var client = new MongoClient("mongodb://localhost:27017");
            _database = client.GetDatabase("WarehouseDB");
        }

        public IMongoCollection<T> GetCollection<T>(string name)
        {
            return _database.GetCollection<T>(name);
        }
    }
}