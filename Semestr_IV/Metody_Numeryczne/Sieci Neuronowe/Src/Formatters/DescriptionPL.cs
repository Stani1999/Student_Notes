using System;
using Sieci_Neuronowe.Src.Interfaces;

namespace Sieci_Neuronowe.Src.Formatters
{
    /// <summary>
    /// Provides localized Polish descriptions for technology parameters.
    /// Maps numerical slider values to human-readable project requirements.
    /// </summary>
    public class DescriptionPL : IDescriptionProvider
    {
        /// <summary>
        /// Retrieves description for the Performance requirement level.
        /// </summary>
        public string GetPerformanceText(double v) =>
            v <= 1 ? "Minimalna" : v <= 3 ? "Niska" :
            v <= 5 ? "Standardowa" :
            v <= 7 ? "Wysoka" :
            v <= 9 ? "Bardzo wysoka" :
            "Natywna, wszystko co się da";

        /// <summary>
        /// Retrieves description for the UI/UX complexity level.
        /// </summary>
        public string GetUIText(double v) =>
            v <= 1 ? "Surowy/Systemowy" :
            v <= 3 ? "Prosty" :
            v <= 5 ? "Standardowe" :
            v <= 7 ? "Złożone" :
            v <= 9 ? "Zaawansowane animacje" :
            "Custom pod klienta";

        /// <summary>
        /// Retrieves description for the Hardware integration depth.
        /// </summary>
        public string GetHardwareText(double v) =>
            v <= 1 ? "Brak" : v <= 3 ? "Podstawowe" :
            v <= 5 ? "Standardowe" :
            v <= 7 ? "Zaawansowane" :
            v <= 9 ? "Głęboka integracja" :
            "Nieograniczony dostęp (Do galerii?)";

        /// <summary>
        /// Retrieves description for the Functional complexity.
        /// </summary>
        public string GetFuncText(double v) =>
            v <= 1 ? "Prosta" :
            v <= 3 ? "Podstawowa" :
            v <= 5 ? "Umiarkowana" :
            v <= 7 ? "Rozbudowana" :
            v <= 9 ? "Złożona" : 
            "Inżynierski Full-wypas";

        /// <summary>
        /// Retrieves description for the Budget availability.
        /// </summary>
        public string GetBudgetText(double v) =>
            v <= 1 ? "Minimalny (Hobby)" :
            v <= 3 ? "Bardzo mały" :
            v <= 5 ? "Standardowy" :
            v <= 7 ? "Duży" :
            v <= 9 ? "Bardzo duży" :
            "Wszelkie koszty po stronie Inwestora";

        /// <summary>
        /// Retrieves description for the Learning curve tolerance.
        /// </summary>
        public string GetLearningText(double v) =>
            v <= 1 ? "Błyskawiczny" :
            v <= 3 ? "Łatwy" :
            v <= 5 ? "Przystępny" :
            v <= 7 ? "Wymagający" :
            v <= 9 ? "Trudny" : 
            "Dla Magistra Inżyniera";

        /// <summary>
        /// Retrieves description for the Time constraints (Deadline).
        /// </summary>
        public string GetDeadlineText(double v) =>
            v <= 1 ? "Brak terminu" :
            v <= 3 ? "Rok - Dużo czasu" :
            v <= 5 ? "Półroku" :
            v <= 7 ? "Napięty (\"Na Maj\")" :
            v <= 9 ? "Krótki" : 
            "Na wczoraj (ASAP)";
    }
}