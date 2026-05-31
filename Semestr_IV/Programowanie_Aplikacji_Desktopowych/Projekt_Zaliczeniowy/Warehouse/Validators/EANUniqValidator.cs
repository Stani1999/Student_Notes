using FluentValidation;
using System.Threading;
using System.Threading.Tasks;
using Warehouse.Models;
using Warehouse.Services.Application;

namespace Warehouse.Validators
{
    public class EANUniqValidator : AbstractValidator<Product>
    {
        private readonly ProductService _productService;

        public EANUniqValidator(ProductService productService)
        {
            _productService = productService;

            RuleFor(x => x.Barcode)
                .MustAsync(async (product, barcode, cancellation) =>
                {
                    return await _productService.IsBarcodeUniqueAsync(barcode, product.Id);
                })
                .WithMessage("Produkt o podanym kodzie EAN już istnieje.");
        }
    }
}