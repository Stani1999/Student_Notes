using CommunityToolkit.Mvvm.Input;
using Kwadratury.Models;
using System;
using System.Linq;

namespace Kwadratury.ViewModels
{
    public partial class MainViewModel
    {
        [RelayCommand]
        private void Calculate()
        {
            Parameters.ClearErrors();
            var validationResult = _validator.Validate(Parameters);
            if (!validationResult.IsValid)
            {
                foreach (var error in validationResult.Errors)
                {
                    Parameters.AddError(error.PropertyName, error.ErrorMessage);
                }
                return;
            }

            try
            {
                string safeExpression = Parameters.FunctionExpression?.Replace(',', '.') ?? string.Empty;
                Func<double, double> func = _parser.Parse(safeExpression);

                double aVal = ParsedA;
                double bVal = ParsedB;
                int nVal = ParsedN;

                MethodResults.Clear();
                foreach (var method in _methods)
                {
                    int currentN = (method.Name == "Metoda Simpsona" && nVal % 2 != 0) ? nVal + 1 : nVal;
                    var mResult = method.Calculate(func, aVal, bVal, currentN);

                    MethodResults.Add(new MethodResultModel
                    {
                        MethodName = method.Name,
                        N = currentN,
                        Result = mResult.TotalArea
                    });
                }

                var algorithm = _methods.First(m => m.Name == Parameters.SelectedMethod);
                int plotN = (algorithm.Name == "Metoda Simpsona" && nVal % 2 != 0) ? nVal + 1 : nVal;
                var result = algorithm.Calculate(func, aVal, bVal, plotN);

                FinalResult = result.TotalArea;
                Steps.Clear();
                foreach (var step in result.Steps) Steps.Add(step);

                PlotModel = _plotService.GeneratePlotModel(func, aVal, bVal, plotN, Parameters.SelectedMethod, FinalResult, Steps);
                CalculatedMethod = Parameters.SelectedMethod;
            }
            catch (Exception ex)
            {
                Parameters.AddError(nameof(Parameters.FunctionExpression), $"Błąd wzoru: {ex.Message}");
            }
        }
    }
}