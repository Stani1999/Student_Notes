using System;

namespace DFT.Services.Application
{
    public static class ThresholdCalculationService
    {
        public static double CalculateDefaultThreshold(int elementsCount)
        {
            return Math.Floor(elementsCount / 2.0) - 1;
        }
    }
}