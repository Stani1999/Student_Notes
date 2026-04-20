using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Data.Languages.Errors
{
    /// <summary>
    /// Polish implementation of validation error messages.
    /// </summary>
    internal class ErrorsPL : IErrorsLanguage
    {
        // Validation errors
        public string Title => "Błąd!";
        public string Empty => "Pole PESEL nie może być puste!";
        public string Length => "PESEL musi mieć 11 cyfr!";
        public string Digits => "Tylko cyfry 0-9!";
        public string Checksum => "Błędna suma kontrolna!";
        public string InvalidDate => "Nieprawidłowa data!";
    }
}