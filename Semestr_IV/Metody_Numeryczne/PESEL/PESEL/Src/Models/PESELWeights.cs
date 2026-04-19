using System;
namespace PESEL.Src.Models
{
    /// <summary>
    /// Stores constant weights values for the PESEL algorithm.
    /// </summary>
    internal class PESELWeights
    {
        /// <summary>
        /// Weights used in the PESEL checksum calculation.
        /// </summary>
        public static readonly int[] Weights = { 1, 3, 7, 9, 1, 3, 7, 9, 1, 3 };
    }
}
