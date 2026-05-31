using System.Collections.Generic;
using System.Linq;
using OxyPlot;

namespace AproksymacjaMNK.Models
{
    public class SummationModel
    {
        public double SumX { get; }
        public double SumY { get; }
        public double SumX2 { get; }
        public double SumXY { get; }
        public int N { get; }

        public SummationModel(IEnumerable<DataPoint> points)
        {
            var list = points.ToList();
            N = list.Count;

            SumX = list.Sum(p => p.X);
            SumY = list.Sum(p => p.Y);
            SumX2 = list.Sum(p => p.X * p.X);
            SumXY = list.Sum(p => p.X * p.Y);
        }

        public double GetDenominator()
        {
            // n*Σ(x^2) - (Σx)^2
            return (N * SumX2 - SumX * SumX);
        }
    }
}