using OxyPlot;
using System.Collections.Generic;

namespace Interpolacja_Aproksymacja.Domain.Interfaces
{
    public interface IApproximationService
    {
        double[] CalculateCoefficients(List<DataPoint> points, int degree);
    }
}