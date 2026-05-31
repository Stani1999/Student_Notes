using FluentValidation;
using Schemat_Hornera.ViewModels;
using System.Globalization;

namespace Schemat_Hornera.Validators
{
    public class CoefficientItemValidator : AbstractValidator<CoefficientItem>
    {
        public CoefficientItemValidator()
        {
            RuleFor(x => x.Value)
                .NotEmpty().WithMessage(x => $"Podaj wartość dla {x.Label}")
                .Must(BeAValidNumber).WithMessage(x => $"Niepoprawna liczba przy {x.Label}");
        }

        private bool BeAValidNumber(string input)
        {
            if (string.IsNullOrWhiteSpace(input)) return false;
            string normalizedInput = input.Replace(',', '.');
            return double.TryParse(normalizedInput, NumberStyles.Any, CultureInfo.InvariantCulture, out _);
        }
    }
}