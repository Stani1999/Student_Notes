using FluentValidation;
using Schemat_Hornera.ViewModels;
using System.Globalization;

namespace Schemat_Hornera.Validators
{
    public class MainViewModelValidator : AbstractValidator<MainViewModel>
    {
        public MainViewModelValidator()
        {
            RuleFor(x => x.XValueInput)
                .NotEmpty().WithMessage("Pole x nie może być puste.")
                .Must(BeAValidNumber).WithMessage("Wprowadź poprawną liczbę dla x.");

            RuleForEach(x => x.CoefficientsList).SetValidator(new CoefficientItemValidator());
        }

        private bool BeAValidNumber(string input)
        {
            if (string.IsNullOrWhiteSpace(input)) return false;
            string normalizedInput = input.Replace(',', '.');
            return double.TryParse(normalizedInput, NumberStyles.Any, CultureInfo.InvariantCulture, out _);
        }
    }
}