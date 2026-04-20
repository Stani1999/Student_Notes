using PESEL.Src.Interfaces.Languages;

/// <summary>
/// English implementation of output-related language elements, such as month and gender.
/// </summary>

namespace PESEL.Src.Data.Languages.Out
{
    internal class OutEN : IOutLanguage
    {
        public string[] Months => new[]
        {
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        };

        public string Male => "Male";
        public string Female => "Female";

        public string MaleShort => "(M/m)";
        public string FemaleShort => "(F/f)";
    }
}