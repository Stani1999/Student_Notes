using Sztuczne_Sieci_Neuronowe.Src.Interfaces;

namespace Sztuczne_Sieci_Neuronowe.Src.Formatters
{
    /// <summary>
    /// Provides localized English descriptions for technology parameters.
    /// Maps numerical slider values to human-readable project requirements.
    /// </summary>
    public class DescriptionEN : IDescriptionProvider
    {
        /// <summary>
        /// Retrieves description for the Performance requirement level.
        /// </summary>
        public string GetPerformanceText(double v) => 
            v <= 1 ? "Minimal" : 
            v <= 3 ? "Low" :
            v <= 5 ? "Standard" : 
            v <= 7 ? "High" :
            v <= 9 ? "Very High" : 
            "Critical (Native)";
        /// <summary>
        /// Retrieves description for the UI/UX complexity level.
        /// </summary>
        public string GetUIText(double v) => 
            v <= 1 ? "Raw/System" : 
            v <= 3 ? "Simple" :
            v <= 5 ? "Standard" : 
            v <= 7 ? "Complex" : 
            v <= 9 ? "Advanced Animations" : 
            "Bespoke/Custom UI";
        /// <summary>
        /// Retrieves description for the Hardware integration depth.
        /// </summary>
        public string GetHardwareText(double v) => 
            v <= 1 ? "None" : 
            v <= 3 ? "Basic" :
            v <= 5 ? "Standard" : 
            v <= 7 ? "Advanced" : 
            v <= 9 ? "Deep Integration" : 
            "IoT/Industrial";
        /// <summary>
        /// Retrieves description for the Functional complexity.
        /// </summary>
        public string GetFuncText(double v) => 
            v <= 1 ? "Simple" : 
            v <= 3 ? "Basic" :
            v <= 5 ? "Moderate" : 
            v <= 7 ? "Extensive" : 
            v <= 9 ? "Complex" : 
            "Heavy Logic";
        /// <summary>
        /// Retrieves description for the Budget availability.
        /// </summary>
        public string GetBudgetText(double v) => v 
            <= 1 ? "Minimal (Hobby)" : 
            v <= 3 ? "Very Small" :
            v <= 5 ? "Standard" : 
            v <= 7 ? "Large" : 
            v <= 9 ? "Enterprise" : 
            "Unlimited";
        /// <summary>
        /// Retrieves description for the Learning curve tolerance.
        /// </summary>
        public string GetLearningText(double v) => 
            v <= 1 ? "Instant" : 
            v <= 3 ? "Easy" :
            v <= 5 ? "Accessible" : 
            v <= 7 ? "Demanding" : 
            v <= 9 ? "Difficult" :
            "High Entry Barrier";
        /// <summary>
        /// Retrieves description for the Time constraints (Deadline).
        /// </summary>
        public string GetDeadlineText(double v) => 
            v <= 1 ? "No Deadline" : 
            v <= 3 ? "Yearly - Relaxed" :
            v <= 5 ? "6 Months" : 
            v <= 7 ? "Tight" : 
            v <= 9 ? "Short" : 
            "Critical (ASAP)";
    }
}