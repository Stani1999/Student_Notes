using DFT.Models;
using OxyPlot;
using OxyPlot.Axes;
using OxyPlot.Series;
using System.Collections.Generic;

namespace DFT.Services.Application
{
    public static class PlotGeneratorService
    {
        public static PlotModel GenerateSpectrumPlot(List<NoisySignalModel> noisySignals, List<DenoisedSignalModel> denoisedSignals)
        {
            var model = new PlotModel { Title = "|DFT|" };

            model.Axes.Add(new LinearAxis { Position = AxisPosition.Bottom, IsZoomEnabled = false, IsPanEnabled = false });
            model.Axes.Add(new LinearAxis { Position = AxisPosition.Left, IsZoomEnabled = false, IsPanEnabled = false });

            var rawSeries = new StemSeries
            {
                Title = "Zaszumione |DFT|",
                Color = OxyColors.LightGray,
                StrokeThickness = 1
            };

            var filteredSeries = new StemSeries
            {
                Title = "Odszumione |DFT|",
                Color = OxyColors.Green,
                StrokeThickness = 4
            };

            for (int i = 0; i < noisySignals.Count; i++)
            {
                rawSeries.Points.Add(new DataPoint(noisySignals[i].N, noisySignals[i].DftMagnitude));
                filteredSeries.Points.Add(new DataPoint(denoisedSignals[i].N, denoisedSignals[i].FilteredDftMagnitude));
            }

            model.Series.Add(rawSeries);
            model.Series.Add(filteredSeries);

            return model;
        }
    }
}