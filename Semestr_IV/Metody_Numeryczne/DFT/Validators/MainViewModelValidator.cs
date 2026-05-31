using FluentValidation;
using DFT.ViewModels;

namespace DFT.Validators
{
    public class MainViewModelValidator : AbstractValidator<MainViewModel>
    {
        public MainViewModelValidator()
        {
            RuleFor(x => x.ExcelFilePath)
                .NotEmpty().WithMessage("Proszę wybrać plik Excel.");

            RuleFor(x => x.SheetIndex)
                .GreaterThanOrEqualTo(0).WithMessage("Indeks arkusza musi wynosić co najmniej 0.");

            RuleFor(x => x.StartCell)
                .NotEmpty().WithMessage("Pole nie może być puste.")
                .Matches(@"^[a-zA-Z]+\d+$").WithMessage("Niepoprawny format (np. B2).");

            RuleFor(x => x.NoiseThreshold)
                .GreaterThanOrEqualTo(0).WithMessage("Próg szumu nie może być ujemny.");
        }
    }
}