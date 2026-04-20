namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Defines strictly UI-related strings
    /// </summary>
    internal interface IUILanguage  
    {
        // Main window elements
        string MainWindowTitle { get; }
        string txtWelcome { get; }
        string txtInputPESEL { get; }
        string btnCheck { get; }
        string btnLanguage { get; }
        
        // Result labels
        string txtResult { get; }
        string txtChecksum { get; }
        string txtYear { get; }
        string txtMonth { get; }
        string txtDay { get; }
        string txtMonthNumber { get; }
        string txtBirthday { get; }
        string txtGender { get; }
        string txtGenderShort { get; }
    }
}