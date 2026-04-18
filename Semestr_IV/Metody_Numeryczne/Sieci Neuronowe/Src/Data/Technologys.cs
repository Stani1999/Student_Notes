using System.Collections.Generic;
using Sieci_Neuronowe.Src.Models;

namespace Sieci_Neuronowe.Src.Data
{
    /// <summary>
    /// Global repository for technology weights and definitions.
    /// Order of weights in the array:
    /// [0] Performance - High value means high performance requirements.
    /// [1] UI/UX       - Complexity of animations and custom interface.
    /// [2] Hardware     - Access to Bluetooth, sensors, GPS, etc.
    /// [3] Functional   - Heavy background processing or local data management.
    /// [4] Budget       - Financial resources (positive = expensive tech, negative = cost-effective).
    /// [5] Learning     - Ease of entry for a new developer.
    /// [6] Deadline     - Time pressure (positive = fast dev, negative = long-term project).
    /// [7] Android      - Native platform preference.
    /// [8] iOS          - Native platform preference.
    /// </summary>

    public static class Technologys
    {
        public static List<Technology> GetDefaultTechnologies()
        {
            return new List<Technology>
            {
                /* * Template for adding new technologies:
                 * new Technology
                 * {
                 * Name = "Technology Name",
                 * Weights = new double[] { Perf, UI, Hard, Func, Budg, Learn, Dead, Andr, iOS, MultiPlatform }
                 * Weights in range [-5, 5], where: -5 = very low, 0 = neutral, 5 = very high
                 * }
                 */
                new Technology
                {
                    Name = "Swift (iOS Native)",
                    Weights = new double[] {
                        5.0,    // Performance
                        5.0,    // UI/UX
                        5.0,    // Hardware
                        5.0,    // Functional
                        4.0,    // Budget 
                        0.0,    // Learning 
                        -2.0,   // Deadline 
                        -5.0,   // Android
                        5.0,    // iOS
                        -5.0    // MultiPlatform
                    }
                },
                new Technology
                {
                    Name = "Kotlin (Android Native)",
                    Weights = new double[] {
                        5.0,    // Performance
                        5.0,    // UI/UX
                        5.0,    // Hardware
                        5.0,    // Functional
                        3.5,    // Budget
                        0.0,    // Learning
                        -2.0,   // Deadline
                        5.0,    // Android
                        -5.0,   // iOS
                        -5.0    // MultiPlatform
                    }
                },
                new Technology
                {
                    Name = "Swift + Kotlin (Dual-Native)",
                    Weights = new double[] {
                        5.0,    // Performance
                        5.0,    // UI/UX
                        5.0,    // Hardware
                        5.0,    // Functional
                        5.0,    // Budget
                        5.0,    // Learning
                        -5.0,   // Deadline
                        5.0,    // Android
                        5.0,    // iOS
                        5.0     // MultiPlatform
                    }
                },
                new Technology
                {
                    Name = "Flutter",
                    Weights = new double[] {
                        4.0,    // Performance
                        4.0,    // UI/UX
                        2.0,    // Hardware
                        4.0,    // Functional
                        0.0,    // Budget
                        1.0,   // Learning
                        2.0,    // Deadline
                        2.0,    // Android
                        -2.0,    // iOS
                        4.0     // MultiPlatform
                    }
                },
                new Technology
                {
                    Name = "React Native",
                    Weights = new double[] {
                        3.0,    // Performance
                        2.0,    // UI/UX
                        1.0,    // Hardware
                        0.0,    // Functional
                        -2.0,   // Budget
                        1.0,    // Learning
                        4.0,    // Deadline
                        -2.0,    // Android
                        2.0,    // iOS
                        4.0     // MultiPlatform
                    }
                },
                new Technology
                {
                    Name = "Kotlin Multiplatform",
                    Weights = new double[] {
                        4.0,    // Performance
                        1.0,    // UI/UX
                        4.0,    // Hardware
                        5.0,    // Functional   
                        2.0,    // Budget
                        0.0,    // Learning
                        0.0,    // Deadline
                        3.0,    // Android
                        1.0,    // iOS
                        4.0     // MultiPlatform
                    }
                },
                new Technology
                {
                    Name = "PWA",
                    Weights = new double[] {
                        -3.0,   // Performance
                        -3.0,   // UI/UX
                        -5.0,   // Hardware
                        -3.0,   // Func
                        -5.0,   // Budget
                        -5.0,   // Learning
                        5.0,    // Deadline
                        -3.0,   // Android
                        -4.0,   // iOS
                        5.0     // MultiPlatform
                    }
                }
            };
        }
    }
}