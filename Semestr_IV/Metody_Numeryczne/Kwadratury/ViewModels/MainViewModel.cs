using CommunityToolkit.Mvvm.ComponentModel;
using FluentValidation;
using Kwadratury.Interfaces;
using Kwadratury.Models;
using Kwadratury.Services.Application;
using OxyPlot;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Globalization;
using System.Linq;

namespace Kwadratury.ViewModels
{
    public partial class MainViewModel : ObservableObject
    {
        private readonly IValidator<IntegrationParameters> _validator;
        private readonly FunctionParserService _parser;
        private readonly IEnumerable<IQuadratureMethod> _methods;
        private readonly QuadraturePlotService _plotService;

        [ObservableProperty] private IntegrationParameters _parameters = new();
        [ObservableProperty] private string _calculatedMethod = string.Empty;
        [ObservableProperty] private double _finalResult;
        [ObservableProperty] private PlotModel _plotModel;
        [ObservableProperty] private bool _showSimpsonWarning;
        [ObservableProperty] private string _simpsonWarningMessage = string.Empty;

        public ObservableCollection<string> AvailableMethods { get; }
        public ObservableCollection<QuadratureStepModel> Steps { get; } = new();
        public ObservableCollection<MethodResultModel> MethodResults { get; } = new();

        public double ParsedA => double.TryParse(Parameters.A?.Replace(',', '.'), NumberStyles.Any, CultureInfo.InvariantCulture, out var a) ? a : 0;
        public double ParsedB => double.TryParse(Parameters.B?.Replace(',', '.'), NumberStyles.Any, CultureInfo.InvariantCulture, out var b) ? b : 0;
        public int ParsedN => int.TryParse(Parameters.N, out var n) ? n : 1;

        public MainViewModel(
            IValidator<IntegrationParameters> validator,
            FunctionParserService parser,
            IEnumerable<IQuadratureMethod> methods,
            QuadraturePlotService plotService)
        {
            _validator = validator;
            _parser = parser;
            _methods = methods;
            _plotService = plotService;

            AvailableMethods = new ObservableCollection<string>(_methods.Select(m => m.Name));
            if (AvailableMethods.Any())
            {
                Parameters.SelectedMethod = AvailableMethods[0];
                CalculatedMethod = AvailableMethods[0];
            }

            PlotModel = new PlotModel { Title = "Wizualizacja funkcji" };

            InitializeObservers();
            UpdateSimpsonWarning();
        }
    }
}