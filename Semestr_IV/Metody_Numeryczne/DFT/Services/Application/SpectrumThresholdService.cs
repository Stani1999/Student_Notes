using DFT.Models;
using System.Collections.Generic;
using System.Numerics;

namespace DFT.Services.Application
{
    public static class SpectrumThresholdService
    {
        public static List<DenoisedSignalModel> FilterSpectrum(List<NoisySignalModel> noisySignals, double threshold)
        {
            var denoisedSignals = new List<DenoisedSignalModel>();

            foreach (var noisy in noisySignals)
            {
                var model = new DenoisedSignalModel { N = noisy.N };

                if (noisy.DftMagnitude >= threshold)
                {
                    model.FilteredDftValue = noisy.DftValue;
                    model.FilteredDftMagnitude = noisy.DftMagnitude;
                }
                else
                {
                    model.FilteredDftValue = new Complex(0, 0);
                    model.FilteredDftMagnitude = 0;
                }

                denoisedSignals.Add(model);
            }

            return denoisedSignals;
        }
    }
}