using PESEL.Src.Interfaces.Languages;
using PESEL.Src.Data.Languages.Packs;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Manages current application language state.
    /// Stores full language pack (UI + Errors + Output).
    /// </summary>
    internal class LanguageManager : ILanguageManager
    {
        public ILanguagePack Current { get; private set; }

            /// <summary>
            /// Default language is Polish at application start.
            /// </summary>
            public LanguageManager()
        {
            Current = new LanguagePL();
        }

        /// <summary>
        /// Switches between supported languages (PL / EN).
        /// </summary>
        public void ChangeLanguage()
        {
            if (Current is LanguagePL)
                Current = new LanguageEN();
            else
                Current = new LanguagePL();
        }
    }
}