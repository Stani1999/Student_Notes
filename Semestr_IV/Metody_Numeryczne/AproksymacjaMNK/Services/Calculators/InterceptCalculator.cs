using System;
using AproksymacjaMNK.Core.Interfaces;
using AproksymacjaMNK.Models;

namespace AproksymacjaMNK.Services.Calculators
{
    public class InterceptCalculator : IInterceptCalculator
    {
        public double CalculateA0(SummationModel sums)
        {
            double denominator = sums.GetDenominator();

            if (Math.Abs(denominator) < 1e-10)
                throw new InvalidOperationException("Mianownik jest równy 0. Nie można wyznaczyć wyrazu wolnego.");

            // (Σx^2 * Σy - Σxy * Σx) / (n * Σx^2 - (Σx)^2)
            double numerator = (sums.SumX2 * sums.SumY) - (sums.SumXY * sums.SumX);

            return numerator / denominator;
        }
    }
}