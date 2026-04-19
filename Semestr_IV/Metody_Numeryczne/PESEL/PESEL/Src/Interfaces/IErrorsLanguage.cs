namespace PESEL.Src.Interfaces
{
    /// <summary>
    /// Defines strictly validation-related error messages.
    /// </summary>
    internal interface IErrorsLanguage
    {
        string Empty { get; }
        string Length { get; }
        string Digits { get; }
        string Checksum { get; }
    }
}