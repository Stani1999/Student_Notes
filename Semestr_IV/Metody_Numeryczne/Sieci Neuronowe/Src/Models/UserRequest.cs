using System;
using System.Collections.Generic;
using System.Text;
using Sieci_Neuronowe.Src.Interfaces;

namespace Sieci_Neuronowe.Src.Models
{
    /// <summary>
    /// Represents an analysis request containing user-defined parameters.
    /// Handles the transformation of raw UI values into a mathematical vector.
    /// </summary>
    public class UserRequest : IInputModel
    {
        // Parameter properties derived from UI sliders (range 0-10)
        public double Performance { get; set; }
        public double UI { get; set; }
        public double Hardware { get; set; }
        public double Func { get; set; }
        public double Budget { get; set; }
        public double Learning { get; set; }
        public double Deadline { get; set; }

        // Platform preference value (range -5 to 5)
        public double PlatformValue { get; set; }

        /// <summary>
        /// Converts the request object into a numerical vector for the analysis engine.
        /// Performs normalization to a -5 to 5 range and calculates the multiplatformity feature.
        /// </summary>
        /// <returns>A double array representing the weighted input vector.</returns>
        public double[] ToVector()
        {
            // Calculation of multiplatformity: peak value (5.0) occurs when PlatformValue is 0.0
            double multiPlatform = 5.0 - Math.Abs(PlatformValue);

            return new double[]
            {
                Performance - 5.0,  // Index 0: Performance requirement
                UI - 5.0,           // Index 1: UI/UX importance
                Hardware - 5.0,     // Index 2: Hardware access needs
                Func - 5.0,         // Index 3: Functional complexity
                Budget - 5.0,       // Index 4: Budget availability
                Learning - 5.0,     // Index 5: Learning curve tolerance
                Deadline - 5.0,     // Index 6: Time constraints
                -PlatformValue,     // Index 7: Android preference weight (negative if iOS is preferred)
                PlatformValue,      // Index 8: iOS preference weight (positive if iOS is preferred)
                multiPlatform       // Index 9: Multiplatformity demand (Calculated)
            };
        }
    }
}
