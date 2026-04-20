using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Data.Languages.Errors
{
    /// <summary>
    /// English implementation of validation error messages.
    /// </summary>
    internal class ErrorsEN : IErrorsLanguage
    {
        // Validation errors
        public string Title => "Error!";
        public string Empty => "PESEL field cannot be empty!";
        public string Length => "PESEL must be 11 digits!";
        public string Digits => "Only digits 0-9 are allowed!";
        public string Checksum => "Invalid checksum!";
        public string InvalidDate => "Invalid date!";
    }
}