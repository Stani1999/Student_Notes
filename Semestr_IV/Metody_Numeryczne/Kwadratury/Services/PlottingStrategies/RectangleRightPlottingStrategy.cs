using Kwadratury.Interfaces;
using Kwadratury.Models;
using OxyPlot;
using OxyPlot.Annotations;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.PlottingStrategies
{
    public class RectangleRightPlottingStrategy : IPlottingStrategy
    {
        public string SupportedMethodName => "Prostokąty (Prawe)";

        public void Draw(PlotModel plot, Func<double, double> func, double a, double b, int n, IEnumerable<QuadratureStepModel> steps)
        {
            double h = (b - a) / n;

            foreach (var step in steps)
            {
                if (step.StepDetails == "-")
                {
                    continue;
                }

                double yVal = func(step.X + h);
                var rect = new RectangleAnnotation
                {
                    MinimumX = step.X,
                    MaximumX = step.X + h,
                    MinimumY = Math.Min(0, yVal),
                    MaximumY = Math.Max(0, yVal),
                    Fill = OxyColor.FromAColor(150, OxyColors.Orange),
                    Stroke = OxyColors.Black,
                    StrokeThickness = 0.5
                };
                plot.Annotations.Add(rect);
            }
        }
    }
}