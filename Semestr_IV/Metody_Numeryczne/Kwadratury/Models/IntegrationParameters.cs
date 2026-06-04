using CommunityToolkit.Mvvm.ComponentModel;
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;

namespace Kwadratury.Models
{
    public partial class IntegrationParameters : ObservableObject, INotifyDataErrorInfo
    {
        [ObservableProperty] private string _functionExpression = "1 - x*x";
        [ObservableProperty] private string _a = "0";
        [ObservableProperty] private string _b = "1";
        [ObservableProperty] private string _n = "5";
        [ObservableProperty] private string _selectedMethod = string.Empty;

        private readonly Dictionary<string, List<string>> _errors = new();
        public bool HasErrors => _errors.Any();
        public event EventHandler<DataErrorsChangedEventArgs>? ErrorsChanged;

        public IEnumerable GetErrors(string? propertyName) =>
            (string.IsNullOrEmpty(propertyName) || !_errors.ContainsKey(propertyName))
                ? Enumerable.Empty<string>()
                : _errors[propertyName];

        public void AddError(string propertyName, string errorMessage)
        {
            if (!_errors.ContainsKey(propertyName)) _errors[propertyName] = new List<string>();
            _errors[propertyName].Add(errorMessage);
            ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
        }

        public void ClearErrors()
        {
            var keys = _errors.Keys.ToList();
            _errors.Clear();
            foreach (var key in keys) ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(key));
        }
    }
}