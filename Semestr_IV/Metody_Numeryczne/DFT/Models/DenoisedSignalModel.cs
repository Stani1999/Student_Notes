using CommunityToolkit.Mvvm.ComponentModel;
using System.Numerics;

namespace DFT.Models
{
    public partial class DenoisedSignalModel : ObservableObject
    {
        [ObservableProperty]
        private int _n;

        [ObservableProperty]
        private Complex _filteredDftValue;

        [ObservableProperty]
        private double _filteredDftMagnitude;

        [ObservableProperty]
        private Complex _idftValue;

        [ObservableProperty]
        private double _denoisedY;
    }
}