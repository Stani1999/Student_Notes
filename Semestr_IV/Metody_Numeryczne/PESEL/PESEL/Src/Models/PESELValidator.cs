using PESEL.Src.Interfaces.Languages;
using PESEL.Src.Validations;
using System;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Represents a request model containing a PESEL (Polish national identification number) value.
    /// </summary>
    /// <returns>Model for PESEL request from input via Interface</returns>
    internal class PESELValidator : IPESELRequest
    {
        private string _pesel;
        private readonly PESELFormatValidator _formatValidator;
        private readonly PESELChecksumValidator _checksumValidator;
        private readonly PESELDateValidator _dateValidator;
        private readonly IErrorsLanguage _errors;

        /// <summary>
        /// Gets or sets the PESEL value.
        /// </summary>
        public string pesel
        {
            get => _pesel;
            set
            {
                // Validate the format of the PESEL value using the format validator
                _formatValidator.Validate(value);

                // Validate the checksum of the PESEL value using the checksum validator
                if (!_checksumValidator.IsValid(value))
                    throw new Exception(_errors.Checksum);

                _pesel = value;
            }
        }

        /// <summary>
        /// Initializes a new instance of the PESELValidator class with the specified input and error messages.
        /// </summary>
        /// <param name="input">The PESEL value to be validated and stored.</param>
        /// <param name="errors">The error messages to be used for validation.</param>
        public PESELValidator(string input, IErrorsLanguage errors)
        {
            // Store the provided error messages for use in validation
            _errors = errors;

            // Initialize validators with the provided error messages
            _formatValidator = new PESELFormatValidator(_errors);
            _checksumValidator = new PESELChecksumValidator();
            _dateValidator = new PESELDateValidator();

            // Set the PESEL value, which will trigger the validation in the setter
            this.pesel = input;
        }

        /// <summary>
        /// Processes validated PESEL and returns a complete data model.
        /// </summary>
        public IPESELData GetValidatedData()
        {
            // Validate the date component of the PESEL value using the date validator
            if (!_dateValidator.TryGetDate(this.pesel, out DateTime dt, out _))
                throw new Exception(_errors.InvalidDate);

            // Return a new PESELModel instance populated with the validated data extracted from the PESEL value
            return new PESELModel
            {
                RawPesel = this.pesel,
                FullDate = dt,
                Year = dt.Year,
                Month = dt.Month,
                Day = dt.Day,
                MonthNumber = int.Parse(dt.ToString("MM")),
                Gender = (this.pesel[9] - '0') % 2 == 1, // if true => male
                GenderShort = (this.pesel[9] - '0') % 2 == 1 // if true => male
            };
        }
    }
}