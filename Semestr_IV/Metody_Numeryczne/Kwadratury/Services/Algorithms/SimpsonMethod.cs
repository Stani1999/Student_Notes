using Kwadratury.Interfaces;
using Kwadratury.Models;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.Algorithms
{
    public class SimpsonMethod : IQuadratureMethod
    {
        public string Name => "Metoda Simpsona";

        public (double TotalArea, List<QuadratureStepModel> Steps) Calculate(Func<double, double> f, double a, double b, int n)
        {
            if (n % 2 != 0) n++; 
            
            double h = (b - a) / n;
            double termA = Math.Abs(f(a));
            double termB = Math.Abs(f(b));
            double sum = termA + termB;
            
            var steps = new List<QuadratureStepModel>
            {
                new QuadratureStepModel { StepIndex = 0, X = a, Y = f(a), StepDetails = $"Waga = 1 | Iloczyn = {termA:F4}" }
            };

            for (int i = 1; i < n; i++)
            {
                double x_i = a + (i * h);
                double y_i = f(x_i);
                int weight = (i % 2 == 0) ? 2 : 4; 
                double iloczyn = Math.Abs(weight * y_i);
                
                sum += iloczyn;

                steps.Add(new QuadratureStepModel
                {
                    StepIndex = i,
                    X = x_i,
                    Y = y_i,
                    StepDetails = $"Waga = {weight} | Iloczyn = {iloczyn:F4}"
                });
            }

            steps.Add(new QuadratureStepModel { StepIndex = n, X = b, Y = f(b), StepDetails = $"Waga = 1 | Iloczyn = {termB:F4}" });

            double totalArea = sum * (h / 3.0);
            return (totalArea, steps);
        }
    }
}