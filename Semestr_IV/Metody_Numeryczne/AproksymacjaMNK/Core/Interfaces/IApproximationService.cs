using System.Collections.Generic;
using OxyPlot;

namespace AproksymacjaMNK.Core.Interfaces
{
    public interface IApproximationService
    {
        (double a1, double a0) GetLinearRegression(IEnumerable<DataPoint> points);
    }
}