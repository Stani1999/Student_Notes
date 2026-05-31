using System;
using Interpolacja_Aproksymacja.Domain.Interfaces;

namespace Interpolacja_Aproksymacja.Infrastructure
{
    public class MatrixCalculator : IMatrixCalculator
    {
        public double[] SolveLinearSystem(double[,] matrix, double[] vector)
        {
            int n = vector.Length;
            for (int i = 0; i < n; i++)
            {
                int pivot = i;
                for (int j = i + 1; j < n; j++)
                {
                    if (Math.Abs(matrix[j, i]) > Math.Abs(matrix[pivot, i])) pivot = j;
                }

                for (int j = i; j < n; j++)
                {
                    double temp = matrix[i, j];
                    matrix[i, j] = matrix[pivot, j];
                    matrix[pivot, j] = temp;
                }
                double t = vector[i];
                vector[i] = vector[pivot];
                vector[pivot] = t;

                for (int j = i + 1; j < n; j++)
                {
                    double factor = matrix[j, i] / matrix[i, i];
                    vector[j] -= factor * vector[i];
                    for (int k = i; k < n; k++)
                    {
                        matrix[j, k] -= factor * matrix[i, k];
                    }
                }
            }

            double[] x = new double[n];
            for (int i = n - 1; i >= 0; i--)
            {
                double sum = 0;
                for (int j = i + 1; j < n; j++) sum += matrix[i, j] * x[j];
                x[i] = (vector[i] - sum) / matrix[i, i];
            }
            return x;
        }
    }
}