using System;
using FluentValidation;
using Warehouse.Models;

namespace Warehouse.Validators
{
    /// <summary>
    /// Defines the validation rules for the InventoryTransaction entity.
    /// Prevents empty stock movements and ensures timestamps are not set in the future.
    /// </summary>
    public class TransactionValidator : AbstractValidator<InventoryTransaction>
    {
        public TransactionValidator()
        {
            RuleFor(x => x.ProductId)
                .NotEmpty();

            RuleFor(x => x.TransactionType)
                .NotEmpty()
                .MaximumLength(50);

            RuleFor(x => x.QuantityChanged)
                .NotEqual(0);

            RuleFor(x => x.Timestamp)
                .LessThanOrEqualTo(DateTime.UtcNow);

            RuleFor(x => x.UserId)
                .NotEmpty();
        }
    }
}