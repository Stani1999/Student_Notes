namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Defines the contract for PESEL data handling.
    /// </summary>
    internal interface IPESELRequest
    {
        string pesel { get; set; }
    }
}
