using FluentValidation;
using Warehouse.Models;

namespace Warehouse.Validators
{
    public class ProductValidator : AbstractValidator<Product>
    {
        public ProductValidator()
        {
            RuleFor(x => x.Name)
                .NotEmpty()
                .MaximumLength(100);

            RuleFor(x => x.Barcode)
                .NotEmpty()
                .MinimumLength(3)
                .MaximumLength(20);

            RuleFor(x => x.CategoryId)
                .NotEmpty();

            RuleFor(x => x.Quantity)
                .GreaterThanOrEqualTo(0);

            RuleFor(x => x.Price)
                .NotNull();

            RuleFor(x => x.Price.Amount)
                .GreaterThanOrEqualTo(0);

            RuleFor(x => x.Measurand)
                .NotNull();

            RuleFor(x => x.Measurand.Amount)
                .GreaterThan(0);
        }
    }
}