using System;
using System.Linq;
using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Validations
{
    /// <summary>
    /// Provides methods for PESEL format and checksum 
    /// </summary>
    internal class PESELFormatValidator
    {
        // Dependency on error messages, injected via constructor
        private readonly IErrorsLanguage _errors;

        /// <summary>
        /// Initializes a new instance of the PESELFormatValidator class with the specified error messages.
        /// </summary>
        /// <param name="errors"></param>
        public PESELFormatValidator(IErrorsLanguage errors) => _errors = errors;
        public void Validate(string pesel)
        {
            // Direct mapping to error interface properties
            string error = string.IsNullOrEmpty(pesel) ? _errors.Empty :
                pesel.Length != 11 ? _errors.Length :
                !pesel.All(char.IsDigit) ? _errors.Digits :
                null;

            // Throwing exception if any error is found
            if (error != null) throw new Exception(error);
        }
    }
}
