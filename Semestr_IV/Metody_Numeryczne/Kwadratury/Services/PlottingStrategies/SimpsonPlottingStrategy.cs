using Kwadratury.Interfaces;
using Kwadratury.Models;
using OxyPlot;
using OxyPlot.Series;
using System;
using System.Collections.Generic;

namespace Kwadratury.Services.PlottingStrategies
{
    public class SimpsonPlottingStrategy : IPlottingStrategy
    {
        public string SupportedMethodName => "Metoda Simpsona";

        public void Draw(PlotModel plot, Func<double, double> func, double a, double b, int n, IEnumerable<QuadratureStepModel> steps)
        {
            var areaSeries = new AreaSeries { Color = OxyColor.FromAColor(80, OxyColors.YellowGreen) };

            for (double x = a; x <= b; x += 0.01)
            {
                areaSeries.Points.Add(new DataPoint(x, func(x)));
                areaSeries.Points2.Add(new DataPoint(x, 0));
            }

            plot.Series.Add(areaSeries);
        }
    }
}