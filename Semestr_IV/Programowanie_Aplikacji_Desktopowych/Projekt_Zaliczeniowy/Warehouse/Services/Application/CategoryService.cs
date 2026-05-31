using System.Collections.Generic;
using System.Threading.Tasks;
using MongoDB.Driver;
using Warehouse.Models;
using Warehouse.Services.Infrastructure;

namespace Warehouse.Services.Application
{
    public class CategoryService
    {
        private readonly IMongoCollection<Category> _categories;

        public CategoryService(IMongoService mongoService)
        {
            _categories = mongoService.GetCollection<Category>("Category");
        }

        public async Task<List<string>> GetAllGroupsAsync()
        {
            var filter = Builders<Category>.Filter.Empty;
            return await _categories.Distinct(c => c.Group, filter).ToListAsync();
        }

        public async Task<List<Category>> GetCategoriesByGroupAsync(string group)
        {
            return await _categories.Find(c => c.Group == group).ToListAsync();
        }

        public async Task<List<Category>> GetAllCategoriesAsync()
        {
            return await _categories.Find(_ => true).ToListAsync();
        }

        public async Task<Category> GetCategoryByIdAsync(string id)
        {
            return await _categories.Find(c => c.Id == id).FirstOrDefaultAsync();
        }
    }
}