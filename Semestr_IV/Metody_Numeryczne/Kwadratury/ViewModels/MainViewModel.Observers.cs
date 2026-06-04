using Kwadratury.Models;

namespace Kwadratury.ViewModels
{
    public partial class MainViewModel
    {
        private void InitializeObservers()
        {
            Parameters.PropertyChanged += (s, e) =>
            {
                if (e.PropertyName == nameof(IntegrationParameters.N) || e.PropertyName == nameof(IntegrationParameters.SelectedMethod))
                {
                    UpdateSimpsonWarning();
                }
            };
        }

        private void UpdateSimpsonWarning()
        {
            int nVal = ParsedN;
            ShowSimpsonWarning = Parameters.SelectedMethod == "Metoda Simpsona" && nVal % 2 != 0;
            if (ShowSimpsonWarning)
            {
                SimpsonWarningMessage = $"Metoda wymaga liczb parzystych! Zaokrąglono w górę do {nVal + 1}";
            }
        }
    }
}