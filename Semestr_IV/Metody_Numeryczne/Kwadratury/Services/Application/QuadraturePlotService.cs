using Kwadratury.Interfaces;
using Kwadratury.Models;
using OxyPlot;
using OxyPlot.Axes;
using OxyPlot.Series;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Kwadratury.Services.Application
{
    public class QuadraturePlotService
    {
        private readonly IEnumerable<IPlottingStrategy> _plottingStrategies;

        public QuadraturePlotService(IEnumerable<IPlottingStrategy> plottingStrategies)
        {
            _plottingStrategies = plottingStrategies;
        }

        public PlotModel GeneratePlotModel(Func<double, double> func, double a, double b, int n, string selectedMethod, double finalResult, IEnumerable<QuadratureStepModel> steps)
        {
            var plot = new PlotModel { Title = $"Wynik całki: {finalResult:F4}" };

            plot.Axes.Add(new LinearAxis
            {
                Position = AxisPosition.Bottom,
                PositionAtZeroCrossing = true,
                AxislineStyle = LineStyle.Solid,
                AxislineThickness = 2,
                TickStyle = TickStyle.Crossing,
                IsZoomEnabled = false,
                IsPanEnabled = false
            });

            plot.Axes.Add(new LinearAxis
            {
                Position = AxisPosition.Left,
                PositionAtZeroCrossing = true,
                AxislineStyle = LineStyle.Solid,
                AxislineThickness = 2,
                TickStyle = TickStyle.Crossing,
                IsZoomEnabled = false,
                IsPanEnabled = false
            });

            double padding = (b - a) * 0.1;
            if (padding == 0) padding = 1;

            var exactArea = new AreaSeries
            {
                Color = OxyColors.Transparent,
                Fill = OxyColor.FromAColor(40, OxyColors.Gray)
            };

            for (double x = a; x <= b; x += 0.01)
            {
                exactArea.Points.Add(new DataPoint(x, func(x)));
                exactArea.Points2.Add(new DataPoint(x, 0));
            }
            plot.Series.Add(exactArea);

            plot.Series.Add(new FunctionSeries(func, a - padding, b + padding, 0.01)
            {
                Color = OxyColors.Blue,
                StrokeThickness = 2
            });

            var strategy = _plottingStrategies.FirstOrDefault(s => s.SupportedMethodName == selectedMethod);
            strategy?.Draw(plot, func, a, b, n, steps);

            return plot;
        }
    }
}