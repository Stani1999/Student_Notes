using System;
using AproksymacjaMNK.Core.Interfaces;
using AproksymacjaMNK.Models;

namespace AproksymacjaMNK.Services.Calculators
{
    public class SlopeCalculator : ISlopeCalculator
    {
        public double CalculateA1(SummationModel sums)
        {
            double denominator = sums.GetDenominator();

            if (Math.Abs(denominator) < 1e-10)
                throw new InvalidOperationException("Mianownik jest równy 0. Nie można wyznaczyć nachylenia (punkty mogą być w pionie).");

            // (n * Σxy - Σx * Σy) / (n * Σx^2 - (Σx)^2)
            double numerator = (sums.N * sums.SumXY) - (sums.SumX * sums.SumY);

            return numerator / denominator;
        }
    }
}