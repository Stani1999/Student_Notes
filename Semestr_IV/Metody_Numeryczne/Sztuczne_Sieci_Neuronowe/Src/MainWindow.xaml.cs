using System.Collections.Generic;
using System.Windows;
using System.Windows.Controls;
using Sztuczne_Sieci_Neuronowe.Src.Logic;
using Sztuczne_Sieci_Neuronowe.Src.Models;
using Sztuczne_Sieci_Neuronowe.Src.Interfaces;
using Sztuczne_Sieci_Neuronowe.Src.Formatters;

namespace Sztuczne_Sieci_Neuronowe.Src
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml.
    /// Serves as the View Controller, delegating business logic to the TechnologyAnalyzer.
    /// </summary>
    public partial class MainWindow : Window
    {
        /// <summary>
        /// Synchronizes the platform distribution display.
        /// Shows the numerical split between Android and iOS preferences.
        /// </summary>
        private void S_Platform_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (R_Android_Pts == null || R_iOS_Pts == null) return;

            // Visualization of the 10-point scale split centered at 5
            R_Android_Pts.Text = (5 - e.NewValue).ToString("0");
            R_iOS_Pts.Text = (5 + e.NewValue).ToString("0");
        }

        // Internal services for analysis and localized descriptions
        private readonly TechnologyAnalyzer _analyzer = new TechnologyAnalyzer();
        private readonly IDescriptionProvider _descriptions = new DescriptionPL();

        // Field storing the results of the latest analysis to avoid redundant calculations
        private List<(string Name, double Score)> _lastResults;

        public MainWindow()
        {
            InitializeComponent();
            // At startup, the details button is locked
            B_Details.IsEnabled = false;
            B_Details.Opacity = 0.5;
        }

        /// <summary>
        /// Orchestrates the analysis process by collecting UI data and displaying results.
        /// Utilizes the IInputModel abstraction to maintain decoupling.
        /// </summary>
        private void B_Analyze_Click(object sender, RoutedEventArgs e)
        {
            // Packaging of UI state into a standardized request model
            IInputModel request = new UserRequest
            {
                Performance = S_Performance.Value,
                UI = S_UI.Value,
                Hardware = S_Hardware.Value,
                Func = S_Func.Value,
                Budget = S_Budget.Value,
                Learning = S_Learning.Value,
                Deadline = S_Deadline.Value,
                PlatformValue = S_Platform.Value
            };

            // Retrieval of the technology ranking based on the provided request and storage in field
            _lastResults = _analyzer.GetRanking(request);

            // Update of the primary result label
            if (_lastResults != null && _lastResults.Count > 0)
            {
                L_Test.Content = $"Status: Rekomendacja: {_lastResults[0].Name} ({_lastResults[0].Score:F1} pts)";

                // Activation of the details button after successful analysis
                B_Details.IsEnabled = true;
                B_Details.Opacity = 1.0;
            }
        }

        /// <summary>
        /// Generates and displays a detailed ranking table in a separate window/message box.
        /// </summary>
        private void B_Details_Click(object sender, RoutedEventArgs e)
        {
            // Verification if results exist before showing details
            if (_lastResults == null) return;

            // Usage of cached results instead of re-running the analysis
            string report = ReportFormatter.CreateRankingTable(_lastResults);

            MessageBox.Show(report, "Raport szczegółowy");
        }

        /// <summary>
        /// Updates dynamic description labels whenever slider values change.
        /// </summary>
        private void Slider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            // Verification of UI element initialization
            if (sender is Slider s && L_Perf_Desc != null)
            {
                // Retrieval of localized text from the formatting service
                string text = SliderFormatter.GetDescriptionForSlider(s, _descriptions);

                // Assignment of descriptions to specific UI labels based on slider identity
                switch (s.Name)
                {
                    case "S_Performance": L_Perf_Desc.Text = text; break;
                    case "S_UI": L_UI_Desc.Text = text; break;
                    case "S_Hardware": L_Hard_Desc.Text = text; break;
                    case "S_Func": L_Func_Desc.Text = text; break;
                    case "S_Budget": L_Budget_Desc.Text = text; break;
                    case "S_Learning": L_Learning_Desc.Text = text; break;
                    case "S_Deadline": L_Deadline_Desc.Text = text; break;
                }
            }
        }
    }
}