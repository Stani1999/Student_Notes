using PESEL.Src.Interfaces;

namespace PESEL.Src.Languages.Errors
{
    /// <summary>
    /// Polish implementation of validation error messages.
    /// </summary>
    internal class ErrorsPL : IErrorsLanguage
    {
        public string Empty => "Pole PESEL nie może być puste!";
        public string Length => "PESEL musi mieć 11 cyfr!";
        public string Digits => "Tylko cyfry 0-9!";
        public string Checksum => "Błędna suma kontrolna!";
    }
}