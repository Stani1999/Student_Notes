using System;
using System.Collections.Generic;
using System.Text;

namespace Sieci_Neuronowe.Src.Interfaces
{
    /// <summary>
    /// Contract for classes providing technology parameter descriptions.
    /// This allows for easy switching between different description languages.
    /// </summary>
    public interface IDescriptionProvider 
    {
        string GetPerformanceText(double v);
        string GetUIText(double v);
        string GetHardwareText(double v);
        string GetFuncText(double v);
        string GetBudgetText(double v);
        string GetLearningText(double v);
        string GetDeadlineText(double v);
    }
}