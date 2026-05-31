using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Threading.Tasks;
using Warehouse.Models;
using Warehouse.Services.Application;

namespace Warehouse.ViewModels
{
    public partial class MainViewModel : ObservableObject
    {
        private readonly ProductService _productService;
        private readonly CategoryService _categoryService;
        private readonly ReportService _reportService;

        public CategorySelectionViewModel CategorySelector { get; }
        public ProductDetailsViewModel DetailsViewModel { get; }

        [ObservableProperty]
        private string _searchQuery = string.Empty;

        [ObservableProperty]
        private ObservableCollection<Product> _products = new();

        [ObservableProperty]
        private Product? _selectedProduct;

        [ObservableProperty]
        private bool _isLoading;

        [ObservableProperty]
        private int _currentPage = 0;

        [ObservableProperty]
        private int _pageSize = 50;

        [ObservableProperty]
        private ObservableCollection<int> _pageSizes = new(new[] { 25, 50, 75, 100, 250 });

        [ObservableProperty]
        private bool _isListVisible = true;

        [ObservableProperty]
        private bool _isDetailsVisible = false;

        public MainViewModel(ProductService productService, CategoryService categoryService, ReportService reportService, CategorySelectionViewModel categorySelector, ProductDetailsViewModel detailsViewModel)
        {
            _productService = productService;
            _categoryService = categoryService;
            _reportService = reportService;
            CategorySelector = categorySelector;
            DetailsViewModel = detailsViewModel;

            DetailsViewModel.OnRequestClose += HideDetails;
            CategorySelector.SelectionChanged += async () => { CurrentPage = 0; await LoadPageAsync(); };

            _ = CategorySelector.InitializeAsync();
            _ = LoadPageAsync();
        }

        [RelayCommand]
        public async Task ShowAddDetailsAsync()
        {
            await DetailsViewModel.InitializeNewAsync();
            IsListVisible = false;
            IsDetailsVisible = true;
        }

        [RelayCommand]
        public async Task ShowEditDetailsAsync(Product product)
        {
            await DetailsViewModel.SetProductAsync(product);
            IsListVisible = false;
            IsDetailsVisible = true;
        }

        private void HideDetails()
        {
            IsDetailsVisible = false;
            IsListVisible = true;
            _ = LoadPageAsync();
        }

        partial void OnSearchQueryChanged(string value)
        {
            CurrentPage = 0;
            _ = LoadPageAsync();
        }

        partial void OnPageSizeChanged(int value)
        {
            CurrentPage = 0;
            _ = LoadPageAsync();
        }

        [RelayCommand]
        private async Task RefreshAsync()
        {
            await LoadPageAsync();
        }

        [RelayCommand]
        private async Task ClearAsync()
        {
            SearchQuery = string.Empty;
            CategorySelector.SelectedGroup = "-- Wszystkie --";
            CategorySelector.SelectedCategory = null;
            CurrentPage = 0;
            await LoadPageAsync();
        }

        [RelayCommand]
        public async Task LoadPageAsync()
        {
            IsLoading = true;
            var skip = CurrentPage * PageSize;

            string catId = CategorySelector.SelectedCategory?.Id ?? string.Empty;
            var groupCategoryIds = new List<string>();

            if (string.IsNullOrEmpty(catId) && !string.IsNullOrEmpty(CategorySelector.SelectedGroup) && CategorySelector.SelectedGroup != "-- Wybierz Grupę --" && CategorySelector.SelectedGroup != "-- Wszystkie --")
            {
                var cats = await _categoryService.GetCategoriesByGroupAsync(CategorySelector.SelectedGroup);
                groupCategoryIds = cats.Select(c => c.Id).ToList();
            }

            var results = await _productService.GetFilteredProductsAsync(SearchQuery, catId, groupCategoryIds, skip, PageSize);
            Products = new ObservableCollection<Product>(results);
            IsLoading = false;
        }

        [RelayCommand]
        private async Task NextPageAsync()
        {
            CurrentPage++;
            await LoadPageAsync();
        }

        [RelayCommand]
        private async Task PreviousPageAsync()
        {
            if (CurrentPage > 0)
            {
                CurrentPage--;
                await LoadPageAsync();
            }
        }
    }
}