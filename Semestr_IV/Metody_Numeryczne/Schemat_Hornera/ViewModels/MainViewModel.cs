using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using FluentValidation;
using Schemat_Hornera.Services;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Globalization;
using System.Linq;

namespace Schemat_Hornera.ViewModels
{
    public partial class MainViewModel : ObservableObject, INotifyDataErrorInfo
    {
        private readonly IValidator<MainViewModel> _validator;

        [ObservableProperty]
        private int _selectedDegree;

        [ObservableProperty]
        private string _xValueInput;

        [ObservableProperty]
        private string _resultText;

        public ObservableCollection<int> AvailableDegrees { get; }
        public ObservableCollection<CoefficientItem> CoefficientsList { get; }

        private readonly Dictionary<string, List<string>> _errors = new();
        public bool HasErrors => _errors.Any();
        public event EventHandler<DataErrorsChangedEventArgs>? ErrorsChanged;

        public MainViewModel(IValidator<MainViewModel> validator)
        {
            _validator = validator;
            _xValueInput = string.Empty;
            _resultText = string.Empty;

            AvailableDegrees = new ObservableCollection<int>(Enumerable.Range(1, 20));
            CoefficientsList = new ObservableCollection<CoefficientItem>();

            SelectedDegree = 3;
        }

        partial void OnSelectedDegreeChanged(int value)
        {
            GenerateCoefficients();
        }

        private void GenerateCoefficients()
        {
            CoefficientsList.Clear();
            ClearErrors();

            for (int i = SelectedDegree; i >= 0; i--)
            {
                string labelDisplay = i switch
                {
                    0 => "(Wyraz wolny)",
                    1 => "x",
                    _ => $"x^{i}"
                };

                CoefficientsList.Add(new CoefficientItem
                {
                    Degree = i,
                    Label = labelDisplay
                });
            }
        }

        [RelayCommand]
        private void Calculate()
        {
            ClearErrors();
            foreach (var item in CoefficientsList)
            {
                item.ClearErrors();
            }

            var validationResult = _validator.Validate(this);

            if (!validationResult.IsValid)
            {
                foreach (var error in validationResult.Errors)
                {
                    if (error.PropertyName == nameof(XValueInput))
                    {
                        AddError(nameof(XValueInput), error.ErrorMessage);
                    }
                    else if (error.PropertyName.StartsWith("CoefficientsList"))
                    {
                        int startIndex = error.PropertyName.IndexOf('[') + 1;
                        int endIndex = error.PropertyName.IndexOf(']');

                        if (startIndex > 0 && endIndex > startIndex)
                        {
                            string indexStr = error.PropertyName.Substring(startIndex, endIndex - startIndex);
                            if (int.TryParse(indexStr, out int index) && index < CoefficientsList.Count)
                            {
                                string propName = error.PropertyName.Substring(error.PropertyName.IndexOf('.') + 1);
                                CoefficientsList[index].AddError(propName, error.ErrorMessage);
                            }
                        }
                    }
                }

                ResultText = string.Empty;
                return;
            }

            var coefficients = CoefficientsList
                .Select(c => double.Parse(c.Value.Replace(',', '.'), CultureInfo.InvariantCulture))
                .ToArray();

            double x = double.Parse(XValueInput.Replace(',', '.'), CultureInfo.InvariantCulture);

            double calculationResult = HornerAlgorithm.Calculate(coefficients, x);

            ResultText = $"W(x) = {calculationResult}";
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