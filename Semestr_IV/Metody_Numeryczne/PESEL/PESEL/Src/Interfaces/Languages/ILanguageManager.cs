using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Manages application language state using full language pack.
    /// </summary>
    internal interface ILanguageManager
    {
        ILanguagePack Current { get; }

        void ChangeLanguage();
    }
}