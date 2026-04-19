using System;
using PESEL.Src.Interfaces;
using PESEL.Src.Validations;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Represents a request model containing a PESEL (Polish national identification number) value.
    /// </summary>
    /// <returns>Model for PESEL request from input via Interface</returns>
    internal class PESELModel : IPESELRequest
    {
        public string _pesel;
        private readonly IErrorsLanguage _errors;
        private readonly PESELFormatValidator _formatValidator;
        private readonly PESELChecksumValidator _checksumValidator;

        /// <summary>
        /// Gets or sets the PESEL value.
        /// </summary>

        public string pesel
        {
            get => _pesel;
            set 
            {
                _formatValidator.Validate(value);

                if(!_checksumValidator.IsValid(value))
                    throw new Exception(_errors.Checksum);

                _pesel = value;
            }
        }

        /// <summary>
        /// Initializes a new instance of the PESELModel class with the specified input and error messages.
        /// </summary>
        /// <param name="input">The PESEL value to be validated and stored.</param>
        /// <param name="errors">The error messages to be used for validation.</param>
        public PESELModel(string input, IErrorsLanguage errors)
        {
            _errors = errors;
            _formatValidator = new PESELFormatValidator(_errors);
            _checksumValidator = new PESELChecksumValidator();
            this.pesel = input; // This will trigger the validation in the setter
        }
    }
}
