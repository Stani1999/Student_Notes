using System;
using System.Collections.Generic;
using System.Linq;
using OxyPlot;
using Interpolacja_Aproksymacja.Domain.Interfaces;

namespace Interpolacja_Aproksymacja.Domain.Services
{
    public class ApproximationLseService : IApproximationService
    {
        private readonly IMatrixCalculator _matrixCalculator;

        public ApproximationLseService(IMatrixCalculator matrixCalculator)
        {
            _matrixCalculator = matrixCalculator;
        }

        public double[] CalculateCoefficients(List<DataPoint> points, int degree)
        {
            int size = degree + 1;
            double[,] matrix = new double[size, size];
            double[] b = new double[size];

            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    matrix[i, j] = points.Sum(p => Math.Pow(p.X, i + j));
                }
                b[i] = points.Sum(p => p.Y * Math.Pow(p.X, i));
            }

            return _matrixCalculator.SolveLinearSystem(matrix, b);
        }
    }
}