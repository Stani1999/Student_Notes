using PESEL.Src.Interfaces.Languages;

/// <summary>
/// Polish implementation of output-related language elements, such as month and gender.
/// </summary>
namespace PESEL.Src.Data.Languages.Out
{
    internal class OutPL : IOutLanguage
    {
        public string[] Months => new[]
        {
            "Styczeń", "Luty", "Marzec", "Kwiecień",
            "Maj", "Czerwiec", "Lipiec", "Sierpień",
            "Wrzesień", "Październik", "Listopad", "Grudzień"
        };

        public string Male => "Mężczyzna";
        public string Female => "Kobieta";

        public string MaleShort => "(M/m)";
        public string FemaleShort => "(K/k)";
    }
}