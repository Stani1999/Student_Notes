namespace Interpolacja_Aproksymacja.Domain.Interfaces
{
    public interface IMatrixCalculator
    {
        double[] SolveLinearSystem(double[,] matrix, double[] vector);
    }
}