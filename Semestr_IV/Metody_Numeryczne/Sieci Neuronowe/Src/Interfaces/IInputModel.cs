using System;

namespace Sieci_Neuronowe.Src.Interfaces
{
    /// <summary>
    /// Defines a contractual obligation for input data structures within the system.
    /// Ensures that implementing models can provide a numerical vector representation 
    /// required for weighted sum calculations and neural network-like analysis.
    /// </summary>
    public interface IInputModel
    {
        /// <summary>
        /// Transforms the internal state of the implementing object into a standardized double array.
        /// This vector serves as the mathematical input for the technology selection algorithm.
        /// </summary>
        /// <returns>A double array (vector) containing normalized and calculated project features.</returns>
        double[] ToVector();
    }
}