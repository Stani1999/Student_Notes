using AproksymacjaMNK.Models;

namespace AproksymacjaMNK.Core.Interfaces
{
    public interface ISlopeCalculator
    {
        double CalculateA1(SummationModel sums);
    }

    public interface IInterceptCalculator
    {
        double CalculateA0(SummationModel sums);
    }
}