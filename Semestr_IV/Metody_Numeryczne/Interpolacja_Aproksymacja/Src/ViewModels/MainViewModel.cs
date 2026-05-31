using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Windows;
using System.Windows.Input;
using OxyPlot;
using OxyPlot.Series;
using Interpolacja_Aproksymacja.Domain.Interfaces;
using Interpolacja_Aproksymacja.Domain.Services;
using Interpolacja_Aproksymacja.Infrastructure;
using Interpolacja_Aproksymacja.Domain.Validation;

namespace Interpolacja_Aproksymacja.ViewModels
{
    public class MainViewModel : INotifyPropertyChanged
    {
        private readonly IDataImportService _importService;
        private readonly IApproximationService _approximationService;
        private readonly IInterpolationService _interpolationService;

        private PlotModel _plotModel;
        private string _polynomialDegree = "1";
        private string _importStartAddress = "B2";
        private bool _isInterpolationSelected = true;
        private bool _isApproximationSelected = false;
        private ObservableCollection<DataPoint> _inputPoints = new ObservableCollection<DataPoint>();

        public PlotModel PlotModel { get => _plotModel; set { _plotModel = value; OnPropertyChanged(nameof(PlotModel)); } }
        public ObservableCollection<DataPoint> InputPoints => _inputPoints;

        public string ImportStartAddress
        {
            get => _importStartAddress;
            set { _importStartAddress = value; OnPropertyChanged(nameof(ImportStartAddress)); }
        }

        public bool IsInterpolationSelected
        {
            get => _isInterpolationSelected;
            set
            {
                _isInterpolationSelected = value;
                if (value) SyncDegree();
                OnPropertyChanged(nameof(IsInterpolationSelected));
                OnPropertyChanged(nameof(IsConditionMet));
                CommandManager.InvalidateRequerySuggested();
            }
        }

        public bool IsApproximationSelected
        {
            get => _isApproximationSelected;
            set
            {
                _isApproximationSelected = value;
                OnPropertyChanged(nameof(IsApproximationSelected));
                OnPropertyChanged(nameof(IsConditionMet));
                CommandManager.InvalidateRequerySuggested();
            }
        }

        public string PolynomialDegree
        {
            get => _polynomialDegree;
            set
            {
                _polynomialDegree = value;
                OnPropertyChanged(nameof(PolynomialDegree));
                OnPropertyChanged(nameof(IsConditionMet));
            }
        }

        public bool IsConditionMet => IsInterpolationSelected ? _inputPoints.Count >= 2 : (int.TryParse(_polynomialDegree, out int m) && _inputPoints.Count > m);

        public ICommand ImportDataCommand { get; }
        public ICommand CalculateCommand { get; }

        public MainViewModel()
        {
            var matrixCalc = new MatrixCalculator();
            _approximationService = new ApproximationLseService(matrixCalc);
            _interpolationService = new LagrangeInterpolationService();
            _importService = new ExcelDataImportService(new ExcelFileValidator(), new ExcelReaderService());

            PlotModel = new PlotModel { Title = "Analiza Numeryczna" };
            ImportDataCommand = new RelayCommand(ExecuteImport);
            CalculateCommand = new RelayCommand(ExecuteCalculate, _ => IsConditionMet && _inputPoints.Any());
        }

        private void SyncDegree()
        {
            if (_inputPoints.Any()) PolynomialDegree = (_inputPoints.Count - 1).ToString();
        }

        private void ExecuteImport(object obj)
        {
            var dialogService = new DialogService();
            string path = dialogService.OpenExcelFileDialog();

            if (string.IsNullOrEmpty(path)) return;

            try
            {
                var pts = _importService.ImportFromExcel(path, ImportStartAddress);

                if (pts != null && pts.Any())
                {
                    _inputPoints.Clear();
                    foreach (var p in pts.OrderBy(x => x.X))
                    {
                        _inputPoints.Add(p);
                    }

                    if (IsInterpolationSelected)
                    {
                        SyncDegree();
                    }

                    OnPropertyChanged(nameof(IsConditionMet));
                    CommandManager.InvalidateRequerySuggested();
                    UpdatePlot();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Błąd podczas importu danych: {ex.Message}", "Błąd", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void ExecuteCalculate(object obj)
        {
            var pts = _inputPoints.ToList();

            var line = new LineSeries { Color = OxyColors.Red };
            int m = int.TryParse(_polynomialDegree, out int parsedM) ? parsedM : 1;

            double minX = pts.Min(p => p.X);
            double maxX = pts.Max(p => p.X);
            double step = (maxX - minX) / 100;

            if (IsApproximationSelected)
            {
                line.Title = $"Aproksymacja (m={m})";
                var coeffs = _approximationService.CalculateCoefficients(pts, m);
                for (double x = minX; x <= maxX; x += step)
                {
                    double y = 0;
                    for (int i = 0; i < coeffs.Length; i++) y += coeffs[i] * Math.Pow(x, i);
                    line.Points.Add(new DataPoint(x, y));
                }
            }
            else
            {
                line.Title = "Interpolacja (Lagrange)";
                for (double x = minX; x <= maxX; x += step)
                    line.Points.Add(new DataPoint(x, _interpolationService.CalculateValue(pts, x)));
            }

            UpdatePlot(line);
        }

        private void UpdatePlot(LineSeries line = null)
        {
            if (PlotModel == null) return;

            PlotModel.Series.Clear();

            var scatter = new ScatterSeries
            {
                Title = "Punkty wejściowe",
                MarkerType = MarkerType.Circle,
                MarkerFill = OxyColors.Blue,
                MarkerSize = 4
            };

            foreach (var p in _inputPoints)
            {
                scatter.Points.Add(new ScatterPoint(p.X, p.Y));
            }

            PlotModel.Series.Add(scatter);

            if (line != null)
            {
                PlotModel.Series.Add(line);
            }

            PlotModel.InvalidatePlot(true);
        }

        public event PropertyChangedEventHandler PropertyChanged;
        protected void OnPropertyChanged(string n) => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(n));
    }
}