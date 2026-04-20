using PESEL.Src.Interfaces.Languages;
using PESEL.Src.Data.Languages.Errors;

namespace PESEL.Src.Data.Languages.UI
{
    /// <summary>
    /// Provides English user interface strings and error messages for the PESEL Validator application.
    /// </summary>
    /// <remarks>Implements the IUILanguage interface to supply English text for UI elements and error
    /// messages. This class is intended for use when the application's language is set to English.</remarks>
    internal class UIEN : IUILanguage
    {
        // UI strings
        public string MainWindowTitle => "PESEL Validator";
        public string txtWelcome => "Welcome to the PESEL Validator application!";
        public string txtInputPESEL => "Enter PESEL:";
        public string btnCheck => "Verify";
        public string btnLanguage => "Change Language";

        // Labels for result section
        public string txtResult => "Result:";
        public string txtChecksum => "Checksum:";
        public string txtYear => "Year:";
        public string txtDay => "Day:";
        public string txtMonth => "Month:";
        public string txtBirthday => "Birth date:";
        public string txtMonthNumber => "Month Number:";
        public string txtGender => "Gender:";
        public string txtGenderShort => "Gender (M/F):";
    }
}