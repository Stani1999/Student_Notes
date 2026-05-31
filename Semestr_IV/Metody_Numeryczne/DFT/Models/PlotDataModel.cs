using CommunityToolkit.Mvvm.ComponentModel;
using OxyPlot;

namespace DFT.Models
{
    public partial class PlotDataModel : ObservableObject
    {
        [ObservableProperty]
        private PlotModel _spectrumPlot = new PlotModel();

        [ObservableProperty]
        private PlotModel _comparisonPlot = new PlotModel();
    }
}