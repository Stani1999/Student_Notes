using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Controls;
using Sieci_Neuronowe.Src.Interfaces;

namespace Sieci_Neuronowe.Src.Formatters
{
    /// <summary>
    /// Responsible for mapping UI Slider values to descriptive text.
    /// Acts as a bridge between the View (MainWindow) and IDescriptionProvider implementations.
    /// </summary>
    public static class SliderFormatter
    {
        /// <summary>
        /// Retrieves a formatted description based on the slider's name and the provided description provider.
        /// </summary>
        /// <param name="s">The Slider control from the user interface.</param>
        /// <param name="provider">An instance implementing IDescriptionProvider (e.g., DescriptionPL).</param>
        /// <returns>A string containing the parameter description.</returns>
        public static string GetDescriptionForSlider(Slider s, IDescriptionProvider provider)
        {
            // Verification of the provided objects
            if (s == null || provider == null) return string.Empty;

            double v = s.Value;

            // Mapping of slider names to specific methods of the description provider
            return s.Name switch
            {
                "S_Performance" => provider.GetPerformanceText(v),
                "S_UI" => provider.GetUIText(v),
                "S_Hardware" => provider.GetHardwareText(v),
                "S_Func" => provider.GetFuncText(v),
                "S_Budget" => provider.GetBudgetText(v),
                "S_Learning" => provider.GetLearningText(v),
                "S_Deadline" => provider.GetDeadlineText(v),
                _ => "Unknown Parameter"
            };
        }
    }
}