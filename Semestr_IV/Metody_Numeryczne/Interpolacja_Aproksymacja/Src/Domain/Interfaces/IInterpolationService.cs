using OxyPlot;
using System.Collections.Generic;

namespace Interpolacja_Aproksymacja.Domain.Interfaces
{
    public interface IInterpolationService
    {
        double CalculateValue(List<DataPoint> points, double targetX);
    }
}