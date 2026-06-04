using Kwadratury.Interfaces;
using Kwadratury.Models;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.Algorithms
{
    public class GaussLegendreMethod : IQuadratureMethod
    {
        public string Name => "Metoda Gaussa-Legendre'a";

        public (double TotalArea, List<QuadratureStepModel> Steps) Calculate(Func<double, double> f, double a, double b, int n)
        {
            if (n < 1) n = 1;
            if (n > 5) n = 5;

            double[] nodes = GetNodes(n);
            double[] weights = GetWeights(n);

            double sum = 0;
            var steps = new List<QuadratureStepModel>();
            double multiplier = (b - a) / 2.0;
            double adder = (a + b) / 2.0;

            for (int i = 0; i < n; i++)
            {
                double t_i = nodes[i];
                double w_i = weights[i];

                double x_i = multiplier * t_i + adder;
                double y_i = f(x_i);

                double term = w_i * y_i * multiplier;
                sum += Math.Abs(term);

                steps.Add(new QuadratureStepModel
                {
                    StepIndex = i + 1,
                    X = x_i,
                    Y = y_i,
                    StepDetails = $"w = {w_i:F4} | Węzeł = {t_i:F4}"
                });
            }

            return (sum, steps);
        }

        private double[] GetNodes(int n)
        {
            return n switch
            {
                1 => new[] { 0.0 },
                2 => new[] { -1.0 / Math.Sqrt(3), 1.0 / Math.Sqrt(3) },
                3 => new[] { -Math.Sqrt(3.0 / 5.0), 0.0, Math.Sqrt(3.0 / 5.0) },
                4 => new[] { -Math.Sqrt((3.0 + 2.0 * Math.Sqrt(1.2)) / 7.0), -Math.Sqrt((3.0 - 2.0 * Math.Sqrt(1.2)) / 7.0), Math.Sqrt((3.0 - 2.0 * Math.Sqrt(1.2)) / 7.0), Math.Sqrt((3.0 + 2.0 * Math.Sqrt(1.2)) / 7.0) },
                5 => new[] { -1.0 / 3.0 * Math.Sqrt(5.0 + 2.0 * Math.Sqrt(10.0 / 7.0)), -1.0 / 3.0 * Math.Sqrt(5.0 - 2.0 * Math.Sqrt(10.0 / 7.0)), 0.0, 1.0 / 3.0 * Math.Sqrt(5.0 - 2.0 * Math.Sqrt(10.0 / 7.0)), 1.0 / 3.0 * Math.Sqrt(5.0 + 2.0 * Math.Sqrt(10.0 / 7.0)) },
                _ => new[] { 0.0 }
            };
        }

        private double[] GetWeights(int n)
        {
            return n switch
            {
                1 => new[] { 2.0 },
                2 => new[] { 1.0, 1.0 },
                3 => new[] { 5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0 },
                4 => new[] { (18.0 - Math.Sqrt(30.0)) / 36.0, (18.0 + Math.Sqrt(30.0)) / 36.0, (18.0 + Math.Sqrt(30.0)) / 36.0, (18.0 - Math.Sqrt(30.0)) / 36.0 },
                5 => new[] { (322.0 - 13.0 * Math.Sqrt(70.0)) / 900.0, (322.0 + 13.0 * Math.Sqrt(70.0)) / 900.0, 128.0 / 225.0, (322.0 + 13.0 * Math.Sqrt(70.0)) / 900.0, (322.0 - 13.0 * Math.Sqrt(70.0)) / 900.0 },
                _ => new[] { 2.0 }
            };
        }
    }
}