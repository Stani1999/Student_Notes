using Kwadratury.Models;
using OxyPlot;
using System;
using System.Collections.Generic;

namespace Kwadratury.Interfaces
{
    public interface IPlottingStrategy
    {
        string SupportedMethodName { get; }
        void Draw(PlotModel plot, Func<double, double> func, double a, double b, int n, IEnumerable<QuadratureStepModel> steps);
    }
}