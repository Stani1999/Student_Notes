using System.Collections.Generic;
using OxyPlot;
using Interpolacja_Aproksymacja.Domain.Interfaces;

namespace Interpolacja_Aproksymacja.Domain.Services
{
    public class LagrangeInterpolationService : IInterpolationService
    {
        public double CalculateValue(List<DataPoint> points, double targetX)
        {
            double result = 0;
            int n = points.Count;

            for (int i = 0; i < n; i++)
            {
                double term = points[i].Y;
                for (int j = 0; j < n; j++)
                {
                    if (i != j)
                    {
                        term *= (targetX - points[j].X) / (points[i].X - points[j].X);
                    }
                }
                result += term;
            }
            return result;
        }
    }
}