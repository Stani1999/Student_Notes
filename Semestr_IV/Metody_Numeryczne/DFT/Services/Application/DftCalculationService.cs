using DFT.Models;
using System;
using System.Collections.Generic;
using System.Numerics;

namespace DFT.Services.Application
{
    public static class DftCalculationService
    {
        public static void CalculateDft(List<NoisySignalModel> signals)
        {
            int N = signals.Count;
            for (int k = 0; k < N; k++)
            {
                double real = 0;
                double imaginary = 0;

                for (int n = 0; n < N; n++)
                {
                    double angle = -2.0 * Math.PI * k * n / N;
                    real += signals[n].OriginalX * Math.Cos(angle);
                    imaginary += signals[n].OriginalX * Math.Sin(angle);
                }

                signals[k].DftValue = new Complex(real, imaginary);
                signals[k].DftMagnitude = CalculateMagnitude(signals[k].DftValue);
            }
        }

        public static double CalculateMagnitude(Complex complexNumber)
        {
            return complexNumber.Magnitude;
        }
    }
}