using PESEL.Src.Interfaces;

namespace PESEL.Src.Languages.Errors
{
    /// <summary>
    /// Polish implementation of validation error messages.
    /// </summary>
    internal class ErrorsEN : IErrorsLanguage
    {
        public string Empty => "PESEL field cannot be empty!";
        public string Length => "PESEL must be 11 digits!";
        public string Digits => "Only digits 0-9 are allowed!";
        public string Checksum => "Invalid checksum!";
    }
}