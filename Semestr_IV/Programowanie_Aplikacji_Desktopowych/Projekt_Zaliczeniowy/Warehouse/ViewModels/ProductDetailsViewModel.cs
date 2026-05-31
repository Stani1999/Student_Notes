using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using FluentValidation;
using Microsoft.Win32;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Media.Imaging;
using Warehouse.Models;
using Warehouse.Models.Types;
using Warehouse.Services.Application;
using Warehouse.Validators;

namespace Warehouse.ViewModels
{
    public partial class ProductDetailsViewModel : ObservableObject, INotifyDataErrorInfo
    {
        private readonly ProductService _productService;
        private readonly InventoryService _inventoryService;
        private readonly CategoryService _categoryService;
        private readonly OcrService _ocrService;
        private readonly TranslationService _translationService;
        private readonly IValidator<Product> _productValidator;
        private readonly EANUniqValidator _eanUniqValidator;

        public CategorySelectionViewModel CategorySelector { get; }

        private int _originalQuantity;

        [ObservableProperty]
        private Product _currentProduct;

        [ObservableProperty]
        [NotifyPropertyChangedFor(nameof(CanDelete))]
        private bool _isNewProduct;

        [ObservableProperty]
        private string _productBarcode = string.Empty;

        [ObservableProperty]
        private string _productName = string.Empty;

        [ObservableProperty]
        private string _productDescription = string.Empty;

        [ObservableProperty]
        private int _productQuantity;

        [ObservableProperty]
        private decimal _productPriceAmount;

        [ObservableProperty]
        private Currency _selectedCurrency;

        [ObservableProperty]
        private decimal _measurandAmount;

        [ObservableProperty]
        private Unit _selectedUnit;

        [ObservableProperty]
        private BitmapImage? _productImageSource;

        [ObservableProperty]
        private BitmapImage? _productLabelImageSource;

        [ObservableProperty]
        private string _extractedText = string.Empty;

        [ObservableProperty]
        private ObservableCollection<Currency> _currencies = new();

        [ObservableProperty]
        private ObservableCollection<Unit> _units = new();

        private byte[]? _rawImageData;
        private byte[]? _rawLabelImageData;

        private readonly Dictionary<string, List<string>> _errors = new Dictionary<string, List<string>>();

        public bool HasErrors => _errors.Any();
        public event EventHandler<DataErrorsChangedEventArgs>? ErrorsChanged;
        public event Action? OnRequestClose;

        public bool CanDelete => !IsNewProduct;

        public ProductDetailsViewModel(
            ProductService productService,
            InventoryService inventoryService,
            CategoryService categoryService,
            OcrService ocrService,
            TranslationService translationService,
            CategorySelectionViewModel categorySelector,
            IValidator<Product> productValidator,
            EANUniqValidator eanUniqValidator)
        {
            _productService = productService;
            _inventoryService = inventoryService;
            _categoryService = categoryService;
            _ocrService = ocrService;
            _translationService = translationService;
            CategorySelector = categorySelector;
            _productValidator = productValidator;
            _eanUniqValidator = eanUniqValidator;

            CurrentProduct = new Product();
            IsNewProduct = true;
            Currencies = new ObservableCollection<Currency>(Enum.GetValues(typeof(Currency)).Cast<Currency>());
            Units = new ObservableCollection<Unit>(Enum.GetValues(typeof(Unit)).Cast<Unit>());
        }

        [RelayCommand]
        private void ReturnToList() => OnRequestClose?.Invoke();

        public async Task InitializeNewAsync()
        {
            CurrentProduct = new Product();
            IsNewProduct = true;
            _originalQuantity = 0;
            ProductBarcode = string.Empty;
            ProductName = string.Empty;
            ProductDescription = string.Empty;
            ProductQuantity = 0;
            ProductPriceAmount = 0m;
            MeasurandAmount = 0m;
            ExtractedText = string.Empty;
            _rawImageData = null;
            _rawLabelImageData = null;
            ProductImageSource = null;
            ProductLabelImageSource = null;
            CategorySelector.SelectedGroup = "-- Wszystkie --";
            CategorySelector.SelectedCategory = null;
            ClearErrors();
            CategorySelector.ClearAllErrors();
            await CategorySelector.InitializeAsync();
        }

        public async Task SetProductAsync(Product product)
        {
            CurrentProduct = product;
            IsNewProduct = false;
            _originalQuantity = product.Quantity;
            ProductBarcode = product.Barcode;
            ProductName = product.Name;
            ProductDescription = product.Description;
            ProductQuantity = product.Quantity;
            ProductPriceAmount = product.Price.Amount;
            SelectedCurrency = product.Price.Currency;
            MeasurandAmount = product.Measurand.Amount;
            SelectedUnit = product.Measurand.Unit;
            ExtractedText = product.ExtractedLabelText;
            _rawImageData = product.ImageData;
            _rawLabelImageData = product.LabelImageData;
            ProductImageSource = ByteArrayToImage(_rawImageData);
            ProductLabelImageSource = ByteArrayToImage(_rawLabelImageData);

            await CategorySelector.InitializeAsync();
            CategorySelector.ClearAllErrors();

            if (!string.IsNullOrEmpty(product.CategoryId))
            {
                var cat = await _categoryService.GetCategoryByIdAsync(product.CategoryId);
                if (cat != null)
                {
                    CategorySelector.SelectedGroup = cat.Group;
                    await CategorySelector.LoadCategoriesForGroupAsync(cat.Group);
                    CategorySelector.SelectedCategory = CategorySelector.Categories.FirstOrDefault(c => c.Id == cat.Id);
                }
            }
        }

        private static BitmapImage? ByteArrayToImage(byte[]? array)
        {
            if (array == null || array.Length == 0) return null;
            var image = new BitmapImage();
            using var stream = new MemoryStream(array);
            image.BeginInit();
            image.CacheOption = BitmapCacheOption.OnLoad;
            image.StreamSource = stream;
            image.EndInit();
            image.Freeze();
            return image;
        }

        [RelayCommand]
        private void SelectImage()
        {
            var dialog = new OpenFileDialog { Filter = "Image Files|*.jpg;*.jpeg;*.png" };
            if (dialog.ShowDialog() == true)
            {
                _rawImageData = File.ReadAllBytes(dialog.FileName);
                ProductImageSource = ByteArrayToImage(_rawImageData);
            }
        }

        [RelayCommand]
        private void SelectLabelImage()
        {
            var dialog = new OpenFileDialog { Filter = "Image Files|*.jpg;*.jpeg;*.png" };
            if (dialog.ShowDialog() == true)
            {
                _rawLabelImageData = File.ReadAllBytes(dialog.FileName);
                ProductLabelImageSource = ByteArrayToImage(_rawLabelImageData);
            }
        }

        [RelayCommand]
        private void ExtractTextFromLabel()
        {
            if (_rawLabelImageData != null)
            {
                ExtractedText = _ocrService.ExtractTextFromImage(_rawLabelImageData);
            }
        }

        [RelayCommand]
        private async Task TranslateLabelAsync()
        {
            if (!string.IsNullOrWhiteSpace(ExtractedText))
            {
                ProductDescription = await _translationService.TranslateSpanishToPolishAsync(ExtractedText);
            }
        }

        private async Task<bool> SaveCoreAsync()
        {
            var quantityDifference = ProductQuantity - _originalQuantity;

            CurrentProduct.Barcode = ProductBarcode;
            CurrentProduct.Name = ProductName;
            CurrentProduct.Description = ProductDescription;
            CurrentProduct.Quantity = _originalQuantity;
            CurrentProduct.Price.Amount = ProductPriceAmount;
            CurrentProduct.Price.Currency = SelectedCurrency;
            CurrentProduct.Measurand.Amount = MeasurandAmount;
            CurrentProduct.Measurand.Unit = SelectedUnit;
            CurrentProduct.ImageData = _rawImageData;
            CurrentProduct.LabelImageData = _rawLabelImageData;
            CurrentProduct.ExtractedLabelText = ExtractedText;

            if (CategorySelector.SelectedCategory != null && !string.IsNullOrWhiteSpace(CategorySelector.SelectedCategory.Id))
            {
                CurrentProduct.CategoryId = CategorySelector.SelectedCategory.Id;
            }

            ClearErrors();
            CategorySelector.ClearAllErrors();

            bool hasValidationErrors = false;

            if (string.IsNullOrWhiteSpace(CategorySelector.SelectedGroup) || CategorySelector.SelectedGroup == "-- Wybierz Grupę --" || CategorySelector.SelectedGroup == "-- Wszystkie --")
            {
                CategorySelector.AddError(nameof(CategorySelector.SelectedGroup), "Grupa jest wymagana.");
                hasValidationErrors = true;
            }
            if (CategorySelector.SelectedCategory == null || string.IsNullOrWhiteSpace(CategorySelector.SelectedCategory.Id))
            {
                CategorySelector.AddError(nameof(CategorySelector.SelectedCategory), "Kategoria jest wymagana.");
                hasValidationErrors = true;
            }

            var eanValidationResult = await _eanUniqValidator.ValidateAsync(CurrentProduct);
            if (!eanValidationResult.IsValid)
            {
                foreach (var error in eanValidationResult.Errors)
                {
                    AddError(nameof(ProductBarcode), error.ErrorMessage);
                }
                hasValidationErrors = true;
            }

            var validationResult = await _productValidator.ValidateAsync(CurrentProduct);
            if (!validationResult.IsValid || hasValidationErrors)
            {
                foreach (var error in validationResult.Errors)
                {
                    string propName = error.PropertyName switch
                    {
                        "Barcode" => nameof(ProductBarcode),
                        "Name" => nameof(ProductName),
                        "Quantity" => nameof(ProductQuantity),
                        "Price.Amount" => nameof(ProductPriceAmount),
                        "Measurand.Amount" => nameof(MeasurandAmount),
                        _ => error.PropertyName
                    };
                    AddError(propName, error.ErrorMessage);
                }
                return false;
            }

            if (IsNewProduct)
            {
                CurrentProduct.Quantity = 0;
                await _productService.AddProductAsync(CurrentProduct);

                if (ProductQuantity != 0)
                {
                    await _inventoryService.LogTransactionAsync(new InventoryTransaction
                    {
                        ProductId = CurrentProduct.Id,
                        ProductName = CurrentProduct.Name,
                        TransactionType = ProductQuantity > 0 ? "IN" : "OUT",
                        QuantityChanged = ProductQuantity,
                        Timestamp = DateTime.UtcNow,
                        UserId = "system"
                    });
                }

                IsNewProduct = false;
                _originalQuantity = ProductQuantity;
                CurrentProduct.Quantity = ProductQuantity;
            }
            else
            {
                await _productService.UpdateProductAsync(CurrentProduct);

                if (quantityDifference != 0)
                {
                    await _inventoryService.LogTransactionAsync(new InventoryTransaction
                    {
                        ProductId = CurrentProduct.Id,
                        ProductName = CurrentProduct.Name,
                        TransactionType = quantityDifference > 0 ? "IN" : "OUT",
                        QuantityChanged = Math.Abs(quantityDifference),
                        Timestamp = DateTime.UtcNow,
                        UserId = "system_edit"
                    });
                }

                _originalQuantity = ProductQuantity;
                CurrentProduct.Quantity = ProductQuantity;
            }
            return true;
        }

        [RelayCommand]
        private async Task SaveAsync()
        {
            if (await SaveCoreAsync())
            {
                OnRequestClose?.Invoke();
            }
        }

        [RelayCommand]
        private async Task SaveAndNextAsync()
        {
            if (await SaveCoreAsync())
            {
                await InitializeNewAsync();
            }
        }

        [RelayCommand]
        private async Task DeleteAsync()
        {
            if (!IsNewProduct)
            {
                await _productService.DeleteProductAsync(CurrentProduct.Id);
                OnRequestClose?.Invoke();
            }
        }

        public IEnumerable GetErrors(string? propertyName) => (!_errors.ContainsKey(propertyName ?? "")) ? null! : _errors[propertyName ?? ""];

        private void AddError(string propertyName, string errorMessage)
        {
            if (!_errors.ContainsKey(propertyName)) _errors[propertyName] = new List<string>();
            _errors[propertyName].Add(errorMessage);
            ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
        }

        private void ClearErrors()
        {
            var propertyNames = _errors.Keys.ToList();
            _errors.Clear();
            foreach (var propertyName in propertyNames) ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
        }
    }
}