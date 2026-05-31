using MongoDB.Driver;

namespace Warehouse.Services.Infrastructure
{
    /// <summary>
    /// Provides an abstraction layer for database access.
    /// Exposes a generic method to retrieve MongoDB collections.
    /// </summary>
    public interface IMongoService
    {
        IMongoCollection<T> GetCollection<T>(string name);
    }
}