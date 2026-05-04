using PESEL.Src.Data.Languages.Errors;
using PESEL.Src.Data.Languages.Out;
using PESEL.Src.Data.Languages.UI;
using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Data.Languages.Packs
{
    /// <summary>
    /// Polish language pack (UI + Errors + Output)
    /// Combines the user interface, error messages, and output messages for the Polish language.
    /// </summary>
    internal class LanguagePL : ILanguagePack
    {
        public IUILanguage UI { get; } = new UIPL();
        public IErrorsLanguage Errors { get; } = new ErrorsPL();
        public IOutLanguage Output { get; } = new OutPL();
    }
}