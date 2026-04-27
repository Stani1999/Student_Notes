using PESEL.Src.Interfaces.Languages;
using PESEL.Src.Data.Languages.Errors;

namespace PESEL.Src.Data.Languages.UI
{
    /// <summary>
    /// Provides Polish user interface strings and error messages for the PESEL Validator application.
    /// </summary>
    /// <remarks>Implements the IUILanguage interface to supply Polish text for UI elements and error
    /// messages. This class is intended for use when the application's language is set to Polish.</remarks>
    internal class UIPL : IUILanguage
    {
        // UI strings
        public string MainWindowTitle => "Sprawdź PESEL";
        public string txtWelcome => "Witamy w aplikacji do sprawdzania PESEL!";
        public string txtInputPESEL => "Wprowadź PESEL";
        public string btnCheck => "Sprawdź";
        public string btnLanguage => "Zmień język";

        // Labels for result section
        public string txtResult => "Wynik:";
        public string txtChecksum => "Suma kontrolna:";
        public string txtYear => "Rok:";
        public string txtMonth => "Miesiąc:";
        public string txtDay => "Dzień:";
        public string txtMonthNumber => "Numer Miesiąca:";
        public string txtBirthday => "Data urodzenia:";
        public string txtGender => "Płeć:";
        public string txtGenderShort => "Płeć (M/K):";
    }
}