using System;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Windows;
using System.Windows.Input;
using Microsoft.Win32;
using OxyPlot;
using OxyPlot.Series;
using AproksymacjaMNK.Core.Interfaces;
using AproksymacjaMNK.Services;

namespace AproksymacjaMNK.ViewModels
{
    public class MainViewModel : INotifyPropertyChanged
    {
        private readonly IApproximationService _approximationService;
        private readonly IExcelImportService _excelService;

        private PlotModel _plotModel;
        private string _importStartAddress = "B2";
        private ObservableCollection<DataPoint> _inputPoints;

        public PlotModel PlotModel
        {
            get => _plotModel;
            set { _plotModel = value; OnPropertyChanged(nameof(PlotModel)); }
        }

        public ObservableCollection<DataPoint> InputPoints
        {
            get => _inputPoints;
            set
            {
                _inputPoints = value;
                OnPropertyChanged(nameof(InputPoints));
                OnPropertyChanged(nameof(IsConditionMet));
            }
        }

        public string ImportStartAddress
        {
            get => _importStartAddress;
            set { _importStartAddress = value; OnPropertyChanged(nameof(ImportStartAddress)); }
        }

        public bool IsConditionMet => InputPoints != null && InputPoints.Count >= 2;

        public ICommand ImportDataCommand { get; }
        public ICommand CalculateCommand { get; }

        public MainViewModel()
        {
            _approximationService = new ApproximationService();
            _excelService = new ExcelImportService();

            InputPoints = new ObservableCollection<DataPoint>();
            PlotModel = new PlotModel { Title = "Wykres Aproksymacji" };

            ImportDataCommand = new RelayCommand(ExecuteImport);
            CalculateCommand = new RelayCommand(ExecuteCalculate, _ => IsConditionMet);
        }

        private void ExecuteImport(object obj)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog
            {
                Filter = "Excel Files|*.xlsx;*.xls"
            };

            if (openFileDialog.ShowDialog() == true)
            {
                try
                {
                    var points = _excelService.ImportFromExcel(openFileDialog.FileName, ImportStartAddress);
                    InputPoints = new ObservableCollection<DataPoint>(points);
                    UpdatePlot();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Błąd importu", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }

        private void ExecuteCalculate(object obj)
        {
            try
            {
                var (a1, a0) = _approximationService.GetLinearRegression(InputPoints);
                UpdatePlot(a1, a0);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Błąd obliczeń", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void UpdatePlot(double? a1 = null, double? a0 = null)
        {
            var newModel = new PlotModel { Title = "Aproksymacja MNK" };

            var scatterSeries = new ScatterSeries
            {
                MarkerType = MarkerType.Circle,
                MarkerFill = OxyColors.Blue,
                Title = "Dane wejściowe"
            };

            foreach (var p in InputPoints) scatterSeries.Points.Add(new OxyPlot.Series.ScatterPoint(p.X, p.Y));
            newModel.Series.Add(scatterSeries);

            if (a1.HasValue && a0.HasValue)
            {
                double minX = InputPoints.Min(p => p.X);
                double maxX = InputPoints.Max(p => p.X);
                double padding = (maxX - minX) * 0.1;

                var lineSeries = new LineSeries
                {
                    Color = OxyColors.Red,
                    StrokeThickness = 2,
                    Title = $"y = {a1:F4}x + {a0:F4}"
                };

                lineSeries.Points.Add(new DataPoint(minX - padding, a1.Value * (minX - padding) + a0.Value));
                lineSeries.Points.Add(new DataPoint(maxX + padding, a1.Value * (maxX + padding) + a0.Value));
                newModel.Series.Add(lineSeries);
            }

            PlotModel = newModel;
        }

        public event PropertyChangedEventHandler PropertyChanged;
        protected void OnPropertyChanged(string name) => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}