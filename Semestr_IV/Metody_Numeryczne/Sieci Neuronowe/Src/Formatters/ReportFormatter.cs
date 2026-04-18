using System.Collections.Generic;
using System.Text;

namespace Sieci_Neuronowe.Src.Formatters
{
    /// <summary>
    /// Provides methods for formatting analysis results into human-readable reports.
    /// Handles the visual representation of the technology ranking.
    /// </summary>
    public static class ReportFormatter
    {
        /// <summary>
        /// Generates a formatted string representing the technology ranking table.
        /// Organizes data into columns for better readability.
        /// </summary>
        /// <param name="results">A list of tuples containing technology names and their compatibility scores.</param>
        /// <returns>A formatted string containing the ranking table.</returns>
        public static string CreateRankingTable(List<(string Name, double Score)> results)
        {
            StringBuilder sb = new StringBuilder();

            // Header construction
            sb.AppendLine("Ranking technologii:");
            sb.AppendLine("------------------------------------------------------------");
            sb.AppendLine($"{"Nazwa technologi".PadRight(25)} | {"Wynik"}");
            sb.AppendLine("------------------------------------------------------------");

            // Iterative row generation
            foreach (var r in results)
            {
                // Alignment and precision formatting
                sb.AppendLine(string.Format("{0,-20} | {1,8:F2} pts",
                    r.Name.Length > 20 ? r.Name.Substring(0, 17) + "..." : r.Name, r.Score));
            }

            sb.AppendLine("------------------------------------------------------------");

            return sb.ToString();
        }
    }
}