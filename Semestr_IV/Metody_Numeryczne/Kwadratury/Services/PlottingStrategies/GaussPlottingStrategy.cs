using Kwadratury.Interfaces;
using Kwadratury.Models;
using OxyPlot;
using OxyPlot.Annotations;
using OxyPlot.Series;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.PlottingStrategies
{
    public class GaussPlottingStrategy : IPlottingStrategy
    {
        public string SupportedMethodName => "Metoda Gaussa-Legendre'a";

        public void Draw(PlotModel plot, Func<double, double> func, double a, double b, int n, IEnumerable<QuadratureStepModel> steps)
        {
            var areaSeries = new AreaSeries
            {
                Color = OxyColors.DarkGreen,
                Fill = OxyColor.FromAColor(80, OxyColors.Green),
                StrokeThickness = 1
            };

            for (double x = a; x <= b; x += 0.01)
            {
                areaSeries.Points.Add(new DataPoint(x, func(x)));
                areaSeries.Points2.Add(new DataPoint(x, 0));
            }
            plot.Series.Add(areaSeries);

            foreach (var step in steps)
            {
                var line = new LineAnnotation
                {
                    Type = LineAnnotationType.Vertical,
                    X = step.X,
                    MinimumY = Math.Min(0, step.Y),
                    MaximumY = Math.Max(0, step.Y),
                    Color = OxyColors.Black,
                    StrokeThickness = 0.5,
                    LineStyle = LineStyle.Dash
                };
                plot.Annotations.Add(line);
            }
        }
    }
}