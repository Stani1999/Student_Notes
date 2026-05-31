using CommunityToolkit.Mvvm.ComponentModel;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Threading.Tasks;
using Warehouse.Models;
using Warehouse.Services.Application;

namespace Warehouse.ViewModels
{
    public partial class CategorySelectionViewModel : ObservableObject, INotifyDataErrorInfo
    {
        private readonly CategoryService _categoryService;

        [ObservableProperty]
        private ObservableCollection<string> _groups = new();

        [ObservableProperty]
        private ObservableCollection<Category> _categories = new();

        [ObservableProperty]
        private string _selectedGroup = string.Empty;

        [ObservableProperty]
        private Category? _selectedCategory;

        private readonly Dictionary<string, List<string>> _errors = new();

        public bool HasErrors => _errors.Any();
        public event EventHandler<DataErrorsChangedEventArgs>? ErrorsChanged;
        public event Action? SelectionChanged;

        public CategorySelectionViewModel(CategoryService categoryService)
        {
            _categoryService = categoryService;
        }

        public async Task InitializeAsync()
        {
            var groups = await _categoryService.GetAllGroupsAsync();
            Groups.Clear();
            Groups.Add("-- Wszystkie Grupy --");
            foreach (var group in groups)
            {
                Groups.Add(group);
            }
            SelectedGroup = "-- Wszystkie Grupy --";
        }

        async partial void OnSelectedGroupChanged(string value)
        {
            ClearErrors(nameof(SelectedGroup));

            if (value == "-- Wszystkie Grupy --")
            {
                await LoadAllCategoriesAsync();
            }
            else if (string.IsNullOrWhiteSpace(value) || value == "-- Wybierz Grupę --")
            {
                Categories.Clear();
                SelectedCategory = null;
            }
            else
            {
                await LoadCategoriesForGroupAsync(value);
            }
            SelectionChanged?.Invoke();
        }

        private async Task LoadAllCategoriesAsync()
        {
            Categories.Clear();

            var allCategory = new Category { Id = string.Empty, Name = "-- Wszystkie Kategorie --", Group = "-- Wszystkie --" };
            Categories.Add(allCategory);

            var allCats = await _categoryService.GetAllCategoriesAsync();
            foreach (var cat in allCats)
            {
                Categories.Add(cat);
            }

            SelectedCategory = allCategory;
        }

        partial void OnSelectedCategoryChanged(Category? value)
        {
            ClearErrors(nameof(SelectedCategory));
            SelectionChanged?.Invoke();
        }

        public async Task LoadCategoriesForGroupAsync(string group)
        {
            Categories.Clear();

            if (string.IsNullOrWhiteSpace(group) || group == "-- Wybierz Grupę --" || group == "-- Wszystkie grupy --")
            {
                SelectedCategory = null;
                return;
            }

            var allCategory = new Category { Id = string.Empty, Name = "-- Wszystkie Kategorie --", Group = group };
            Categories.Add(allCategory);

            var cats = await _categoryService.GetCategoriesByGroupAsync(group);
            foreach (var cat in cats)
            {
                Categories.Add(cat);
            }

            SelectedCategory = allCategory;
        }

        public IEnumerable GetErrors(string? propertyName)
        {
            if (string.IsNullOrEmpty(propertyName) || !_errors.ContainsKey(propertyName))
                return null!;
            return _errors[propertyName];
        }

        public void AddError(string propertyName, string errorMessage)
        {
            if (!_errors.ContainsKey(propertyName))
                _errors[propertyName] = new List<string>();

            _errors[propertyName].Add(errorMessage);
            ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
        }

        public void ClearErrors(string propertyName)
        {
            if (_errors.ContainsKey(propertyName))
            {
                _errors.Remove(propertyName);
                ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
            }
        }

        public void ClearAllErrors()
        {
            var keys = _errors.Keys.ToList();
            _errors.Clear();
            foreach (var key in keys)
            {
                ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(key));
            }
        }
    }
}