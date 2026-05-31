using CommunityToolkit.Mvvm.ComponentModel;
using System.Numerics;

namespace DFT.Models
{
    public partial class NoisySignalModel : ObservableObject
    {
        [ObservableProperty]
        private int _n;

        [ObservableProperty]
        private double _originalX;

        [ObservableProperty]
        private Complex _dftValue;

        [ObservableProperty]
        private double _dftMagnitude;
    }
}