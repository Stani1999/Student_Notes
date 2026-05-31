namespace Schemat_Hornera.Services
{
    public static class HornerAlgorithm
    {
        public static double Calculate(double[] Coefficient, double x)
        {
            double result = Coefficient[0];
            for (int i = 1; i < Coefficient.Length; i++)
            {
                result = result * x + Coefficient[i];
            }
            return result;
        }
    }
}