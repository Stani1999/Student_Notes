using System;
using System.Collections.Generic;
using System.Text;

namespace Sieci_Neuronowe.Src.Models
{
    /// <summary>
    /// Represents a specific technology candidate within the decision matrix.
    /// Stores the characteristic profile used for compatibility calculations.
    /// </summary>
    public class Technology
    {
        /// <summary>
        /// Gets or sets the display name of the technology.
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// Gets or sets the vector of weights representing technology attributes.
        /// Each index corresponds to a specific project requirement factor.
        /// </summary>
        public double[] Weights { get; set; }
    }
}