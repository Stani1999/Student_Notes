using Sztuczne_Sieci_Neuronowe.Src.Models;
using Sztuczne_Sieci_Neuronowe.Src.Data;
using Sztuczne_Sieci_Neuronowe.Src.Interfaces;

namespace Sztuczne_Sieci_Neuronowe.Src.Logic
{
    /// <summary>
    /// Handles the core logic of ranking technologies based on input requirements.
    /// Utilizes a weighted sum model to determine the best architectural fit.
    /// </summary>
    public class TechnologyAnalyzer
    {
        private readonly List<Technology> _technologies;

        public TechnologyAnalyzer()
        {
            // Initialization of the default technology dataset
            _technologies = Technologys.GetDefaultTechnologies();
        }

        /// <summary>
        /// Generates a sorted list of technologies based on the provided input model.
        /// </summary>
        /// <param name="request">An object implementing IInputModel containing project parameters.</param>
        /// <returns>A collection of technology names and their corresponding compatibility scores.</returns>
        public List<(string Name, double Score)> GetRanking(IInputModel request)
        {
            // Conversion of the request model into a mathematical vector
            double[] vector = request.ToVector();

            return _technologies
                .Select(t => (
                    t.Name,
                    // Execution of the dot product calculation (SUMA.ILOCZYNÓW)
                    Score: TechnologyLogic.Calculate(t, vector)
                ))
                .OrderByDescending(r => r.Score)
                .ToList();
        }
    }
}