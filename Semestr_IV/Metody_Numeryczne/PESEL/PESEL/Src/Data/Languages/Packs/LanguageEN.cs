using PESEL.Src.Interfaces.Languages;
using PESEL.Src.Data.Languages.Errors;
using PESEL.Src.Data.Languages.Out;
using PESEL.Src.Data.Languages.UI;


namespace PESEL.Src.Data.Languages.Packs
{
    /// <summary>
    /// English language pack (UI + Errors + Output)
    /// Combines the user interface, error messages, and output messages for the English language.
    /// </summary>
    internal class LanguageEN : ILanguagePack
    {
        public IUILanguage UI { get; } = new UIEN();
        public IErrorsLanguage Errors { get; } = new ErrorsEN();
        public IOutLanguage Output { get; } = new OutEN();
    }
}