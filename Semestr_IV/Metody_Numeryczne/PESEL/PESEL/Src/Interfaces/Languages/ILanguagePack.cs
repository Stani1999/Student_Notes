namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Defines the structure for a language pack, which includes all user interface components.
    /// </summary>
    internal interface ILanguagePack
    {
        IUILanguage UI { get; }
        IErrorsLanguage Errors { get; }
        IOutLanguage Output { get; }
    }
}
