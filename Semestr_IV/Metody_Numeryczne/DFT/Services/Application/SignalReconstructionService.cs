using DFT.Models;
using System.Collections.Generic;

namespace DFT.Services.Application
{
    public static class SignalReconstructionService
    {
        public static void ExtractRealSignal(List<DenoisedSignalModel> signals)
        {
            foreach (var signal in signals)
            {
                signal.DenoisedY = signal.IdftValue.Real;
            }
        }
    }
}