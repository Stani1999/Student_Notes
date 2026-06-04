using Kwadratury.Interfaces;
using Kwadratury.Models;
using OxyPlot;
using OxyPlot.Annotations;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.PlottingStrategies
{
    public class TrapezoidalPlottingStrategy : IPlottingStrategy
    {
        public string SupportedMethodName => "Metoda Trapezów";

        public void Draw(PlotModel plot, Func<double, double> func, double a, double b, int n, IEnumerable<QuadratureStepModel> steps)
        {
            double h = (b - a) / n;

            foreach (var step in steps)
            {
                if (step.StepDetails == "-")
                {
                    continue;
                }

                var poly = new PolygonAnnotation
                {
                    Fill = OxyColor.FromAColor(150, OxyColors.Yellow),
                    Stroke = OxyColors.Black,
                    StrokeThickness = 0.5
                };

                poly.Points.Add(new DataPoint(step.X, 0));
                poly.Points.Add(new DataPoint(step.X, step.Y));
                poly.Points.Add(new DataPoint(step.X + h, func(step.X + h)));
                poly.Points.Add(new DataPoint(step.X + h, 0));

                plot.Annotations.Add(poly);
            }
        }
    }
}