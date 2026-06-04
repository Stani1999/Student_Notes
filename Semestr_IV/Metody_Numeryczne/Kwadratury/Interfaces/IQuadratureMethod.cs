using Kwadratury.Models;
using System;
using System.Collections.Generic;

namespace Kwadratury.Interfaces
{
    public interface IQuadratureMethod
    {
        string Name { get; }
        (double TotalArea, List<QuadratureStepModel> Steps) Calculate(Func<double, double> f, double a, double b, int n);
    }
}