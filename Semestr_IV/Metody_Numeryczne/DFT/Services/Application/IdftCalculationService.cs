using DFT.Models;
using System;
using System.Collections.Generic;
using System.Numerics;

namespace DFT.Services.Application
{
    public static class IdftCalculationService
    {
        public static void CalculateIdft(List<DenoisedSignalModel> signals)
        {
            int N = signals.Count;
            for (int n = 0; n < N; n++)
            {
                double realSum = 0;
                double imaginarySum = 0;

                for (int k = 0; k < N; k++)
                {
                    double angle = 2.0 * Math.PI * k * n / N;
                    realSum += signals[k].FilteredDftValue.Real * Math.Cos(angle) - signals[k].FilteredDftValue.Imaginary * Math.Sin(angle);
                    imaginarySum += signals[k].FilteredDftValue.Real * Math.Sin(angle) + signals[k].FilteredDftValue.Imaginary * Math.Cos(angle);
                }

                signals[n].IdftValue = new Complex(realSum / N, imaginarySum / N);
            }
        }
    }
}