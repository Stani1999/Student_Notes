namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Interface for output-related language elements, such as month and gender.
    /// </summary>
    internal interface IOutLanguage
    {
        string[] Months { get; }

        string Male { get; }
        string Female { get; }

        string MaleShort { get; }
        string FemaleShort { get; }
    }
}