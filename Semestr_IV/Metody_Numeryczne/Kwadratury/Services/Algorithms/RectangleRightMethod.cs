using Kwadratury.Interfaces;
using Kwadratury.Models;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.Algorithms
{
    public class RectangleRightMethod : IQuadratureMethod
    {
        public string Name => "Prostokąty (Prawe)";

        public (double TotalArea, List<QuadratureStepModel> Steps) Calculate(Func<double, double> f, double a, double b, int n)
        {
            double h = (b - a) / n;
            double sum = 0;
            var steps = new List<QuadratureStepModel>();

            for (int i = 0; i < n; i++)
            {
                double x_i = a + (i * h);
                double x_right = a + ((i + 1) * h);
                double y_right = f(x_right);
                double area = Math.Abs(y_right * h);

                sum += area;

                steps.Add(new QuadratureStepModel
                {
                    StepIndex = i,
                    X = x_i,
                    Y = f(x_i),
                    StepDetails = $"Pole = {area:F4}"
                });
            }
            return (sum, steps);
        }
    }
}