using DFT.Models;
using OxyPlot;
using OxyPlot.Axes;
using OxyPlot.Series;
using System.Collections.Generic;

namespace DFT.Services.Infrastructure
{
    public static class ComparisonPlotGenerator
    {
        public static PlotModel GenerateComparisonPlot(List<NoisySignalModel> noisySignals, List<DenoisedSignalModel> denoisedSignals)
        {
            var model = new PlotModel { Title = null };

            model.Axes.Add(new LinearAxis { Position = AxisPosition.Bottom, IsZoomEnabled = false, IsPanEnabled = false });
            model.Axes.Add(new LinearAxis { Position = AxisPosition.Left, IsZoomEnabled = false, IsPanEnabled = false });

            var noisySeries = new LineSeries { Title = "Zaszumiony x(n)", Color = OxyColors.Orange };
            var denoisedSeries = new LineSeries { Title = "Odszumiony y(n)", Color = OxyColors.Green };

            for (int i = 0; i < noisySignals.Count; i++)
            {
                noisySeries.Points.Add(new DataPoint(noisySignals[i].N, noisySignals[i].OriginalX));
                denoisedSeries.Points.Add(new DataPoint(denoisedSignals[i].N, denoisedSignals[i].DenoisedY));
            }

            model.Series.Add(noisySeries);
            model.Series.Add(denoisedSeries);

            return model;
        }
    }
}