using Kwadratury.Interfaces;
using Kwadratury.Models;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.Algorithms
{
    public class TrapezoidalMethod : IQuadratureMethod
    {
        public string Name => "Metoda Trapezów";

        public (double TotalArea, List<QuadratureStepModel> Steps) Calculate(Func<double, double> f, double a, double b, int n)
        {
            double h = (b - a) / n;
            double sum = 0;
            var steps = new List<QuadratureStepModel>();

            for (int i = 0; i < n; i++)
            {
                double x_left = a + (i * h);
                double x_right = a + ((i + 1) * h);
                double area = Math.Abs(((f(x_left) + f(x_right)) / 2.0) * h);

                sum += area;

                steps.Add(new QuadratureStepModel
                {
                    StepIndex = i,
                    X = x_left,
                    Y = f(x_left),
                    StepDetails = $"Pole = {area:F4}"
                });
            }

            steps.Add(new QuadratureStepModel { StepIndex = n, X = b, Y = f(b), StepDetails = "-" });
            return (sum, steps);
        }
    }
}