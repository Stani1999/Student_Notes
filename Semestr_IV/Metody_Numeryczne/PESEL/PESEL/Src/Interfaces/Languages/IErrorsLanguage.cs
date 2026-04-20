namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Defines strictly validation-related error messages.
    /// </summary>
    internal interface IErrorsLanguage
    {
        // Pop-up error messages for validation failures
        string Title { get; }
        string Empty { get; }
        string Length { get; }
        string Digits { get; }
        string Checksum { get; }
        string InvalidDate { get; }
    }
}