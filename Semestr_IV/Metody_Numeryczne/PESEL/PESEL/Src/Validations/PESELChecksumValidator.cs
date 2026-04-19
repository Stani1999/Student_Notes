using PESEL.Src.Models;

namespace PESEL.Src.Validations
{
    /// <summary>
    /// Performs checksum validation using externalized weights.
    /// </summary>
    internal class PESELChecksumValidator
    {
        /// <summary>
        /// Validates whether the specified PESEL number has a correct checksum digit.
        /// </summary>
        /// <remarks>This method does not check for other PESEL validity rules, such as valid date
        /// encoding or forbidden number ranges. It only verifies the checksum digit according to the PESEL
        /// specification.</remarks>
        /// <param name="pesel">The PESEL number to validate. Must be an 11-digit string consisting only of numeric characters.</param>
        /// <returns>true if the PESEL number has a valid checksum digit; otherwise, false.</returns>
        public bool IsValid(string pesel)
        {
            int sum = 0;

            for (int i = 0; i < 10; i++)
            {
                // Convert the character to its numeric value (by subtracting '0') and multiply by the corresponding weigh.
                sum += (pesel[i] - '0') * PESELWeights.Weights[i];
            }

            // Take the last digit of the sum. Subtract it from 10. If the result is 10, use 0 otherwise, use the result.
            int expectedChecksum = (10 - (sum % 10)) % 10;

            int actualLastDigit = pesel[10] - '0';

            return actualLastDigit == expectedChecksum;
        }
    }
}
