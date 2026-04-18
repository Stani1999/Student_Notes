using System;
using System.Collections.Generic;
using System.Text;
using Sieci_Neuronowe.Src.Models;

namespace Sieci_Neuronowe.Src.Logic
{
    /// <summary>
    /// Provides mathematical operations for technology evaluation.
    /// Contains core logic for calculating compatibility scores between requirements and technologies.
    /// </summary>
    public static class TechnologyLogic
    {
        /// <summary>
        /// Calculates the total compatibility score for a given technology.
        /// Performs a weighted sum calculation (dot product) of input values and technology weights.
        /// </summary>
        /// <param name="tech">The technology object containing the weight vector.</param>
        /// <param name="input">The input vector representing user requirements.</param>
        /// <returns>A double representing the calculated matching score.</returns>
        public static double Calculate(Technology tech, double[] input)
        {
            double score = 0;

            // Determination of the minimum length to prevent IndexOutOfRangeException
            int length = Math.Min(input.Length, tech.Weights.Length);

            // Iterative multiplication and accumulation of values (Weighted Sum)
            for (int i = 0; i < length; i++)
            {
                // Core calculation: input factor multiplied by the corresponding technology weight
                score += input[i] * tech.Weights[i];
            }

            return score;
        }
    }
}