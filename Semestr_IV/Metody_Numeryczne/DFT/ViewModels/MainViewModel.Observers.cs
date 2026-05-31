using System.Linq;

namespace DFT.ViewModels
{
    public partial class MainViewModel
    {
        partial void OnSheetIndexChanged(int value) => CheckIfSettingsChanged();

        partial void OnStartCellChanged(string value) => CheckIfSettingsChanged();

        partial void OnNoiseThresholdChanged(double value) => CheckIfSettingsChanged();

        partial void OnExcelFilePathChanged(string value) => IsSettingsChangedInfoVisible = false;

        private void CheckIfSettingsChanged()
        {
            if (!string.IsNullOrEmpty(ExcelFilePath) && NoisySignals.Any())
            {
                IsSettingsChangedInfoVisible = true;
            }
        }
    }
}