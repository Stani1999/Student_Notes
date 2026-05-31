using System.Collections.Generic;
using OxyPlot;
using AproksymacjaMNK.Core.Interfaces;
using AproksymacjaMNK.Models;
using AproksymacjaMNK.Services.Calculators;

namespace AproksymacjaMNK.Services
{
    public class ApproximationService : IApproximationService
    {
        private readonly ISlopeCalculator _slopeCalc;
        private readonly IInterceptCalculator _interceptCalc;

        public ApproximationService()
        {
            _slopeCalc = new SlopeCalculator();
            _interceptCalc = new InterceptCalculator();
        }

        public (double a1, double a0) GetLinearRegression(IEnumerable<DataPoint> points)
        {
            var sums = new SummationModel(points);

            double a1 = _slopeCalc.CalculateA1(sums);
            double a0 = _interceptCalc.CalculateA0(sums);

            return (a1, a0);
        }
    }
}