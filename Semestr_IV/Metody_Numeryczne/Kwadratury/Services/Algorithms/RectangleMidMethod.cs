using Kwadratury.Interfaces;
using Kwadratury.Models;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.Algorithms
{
    public class RectangleMidMethod : IQuadratureMethod
    {
        public string Name => "Prostokąty (Środkowe)";

        public (double TotalArea, List<QuadratureStepModel> Steps) Calculate(Func<double, double> f, double a, double b, int n)
        {
            double h = (b - a) / n;
            double sum = 0;
            var steps = new List<QuadratureStepModel>();

            for (int i = 0; i < n; i++)
            {
                double x_i = a + (i * h);
                double x_mid = x_i + (0.5 * h);
                double y_mid = f(x_mid);
                double area = Math.Abs(y_mid * h);

                sum += area;

                steps.Add(new QuadratureStepModel
                {
                    StepIndex = i,
                    X = x_i,
                    Y = f(x_i),
                    X_Mid = x_mid,
                    Y_Mid = y_mid,
                    StepDetails = $"Pole = {area:F4}"
                });
            }
            return (sum, steps);
        }
    }
}