using CommunityToolkit.Mvvm.ComponentModel;
using DFT.Models;
using FluentValidation;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;

namespace DFT.ViewModels
{
    public partial class MainViewModel : ObservableObject, INotifyDataErrorInfo
    {
        private readonly IValidator<MainViewModel> _validator;

        private string _lastDataSource = string.Empty;

        [ObservableProperty]
        private string _excelFilePath;

        [ObservableProperty]
        private int _sheetIndex = 0;

        [ObservableProperty]
        private string _startCell = "B2";

        [ObservableProperty]
        private double _noiseThreshold = 1.0;

        [ObservableProperty]
        private PlotDataModel _plots;

        [ObservableProperty]
        private bool _isSettingsChangedInfoVisible;

        public ObservableCollection<NoisySignalModel> NoisySignals { get; } = new();
        public ObservableCollection<DenoisedSignalModel> DenoisedSignals { get; } = new();

        private readonly Dictionary<string, List<string>> _errors = new();
        public bool HasErrors => _errors.Any();
        public event EventHandler<DataErrorsChangedEventArgs>? ErrorsChanged;

        public MainViewModel(IValidator<MainViewModel> validator)
        {
            _validator = validator;
            _excelFilePath = string.Empty;
            _plots = new PlotDataModel();
        }

        public IEnumerable GetErrors(string? propertyName)
        {
            if (string.IsNullOrEmpty(propertyName) || !_errors.ContainsKey(propertyName))
            {
                return Enumerable.Empty<string>();
            }
            return _errors[propertyName];
        }

        private void AddError(string propertyName, string errorMessage)
        {
            if (!_errors.ContainsKey(propertyName))
            {
                _errors[propertyName] = new List<string>();
            }
            _errors[propertyName].Add(errorMessage);
            ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
        }

        private void ClearErrors()
        {
            var keys = _errors.Keys.ToList();
            _errors.Clear();
            foreach (var key in keys)
            {
                ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(key));
            }
        }
    }
}