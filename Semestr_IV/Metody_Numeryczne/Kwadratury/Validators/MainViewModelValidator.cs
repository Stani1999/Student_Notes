using FluentValidation;
using Kwadratury.Models;
using System.Globalization;

namespace Kwadratury.Validators
{
    public class MainViewModelValidator : AbstractValidator<IntegrationParameters>
    {
        public MainViewModelValidator()
        {
            RuleFor(x => x.FunctionExpression)
                .NotEmpty().WithMessage("Pole nie może być puste.");

            RuleFor(x => x.N)
                .NotEmpty().WithMessage("Pole nie może być puste.")
                .Must(BeAValidPositiveInteger).WithMessage("Musi być dodatnią liczbą całkowitą.");

            RuleFor(x => x.A)
                .NotEmpty().WithMessage("Pole nie może być puste.")
                .Must(BeAValidNumber).WithMessage("Początek (a) musi być poprawną liczbą.");

            RuleFor(x => x.B)
                .NotEmpty().WithMessage("Pole nie może być puste.")
                .Must(BeAValidNumber).WithMessage("Koniec (b) musi być poprawną liczbą.");

            RuleFor(x => x)
                .Must(x => ParseDouble(x.A) < ParseDouble(x.B))
                .When(x => !string.IsNullOrWhiteSpace(x.A) && !string.IsNullOrWhiteSpace(x.B) && BeAValidNumber(x.A) && BeAValidNumber(x.B))
                .WithMessage("Początek przedziału (a) musi być mniejszy niż koniec (b).")
                .WithName("A");
        }

        private bool BeAValidNumber(string value)
        {
            if (string.IsNullOrWhiteSpace(value)) return false;
            string normalized = value.Replace(',', '.');
            return double.TryParse(normalized, NumberStyles.Any, CultureInfo.InvariantCulture, out _);
        }

        private bool BeAValidPositiveInteger(string value)
        {
            if (string.IsNullOrWhiteSpace(value)) return false;
            return int.TryParse(value, out int result) && result > 0;
        }

        private double ParseDouble(string value)
        {
            string normalized = value?.Replace(',', '.') ?? "0";
            double.TryParse(normalized, NumberStyles.Any, CultureInfo.InvariantCulture, out double result);
            return result;
        }
    }
}