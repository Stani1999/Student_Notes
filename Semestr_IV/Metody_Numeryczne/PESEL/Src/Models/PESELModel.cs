using System;
using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Represents the parsed data extracted from a PESEL (Polish national identification number).
    /// </summary>
    /// <remarks>This model provides access to individual components of a PESEL number, such as date of birth
    /// and gender information, after parsing. It is intended for internal use within PESEL processing
    /// workflows.</remarks>
    internal class PESELModel : IPESELData
    {
        public string RawPesel { get; set; }
        public int Year { get; set; }
        public int Month { get; set; }
        public int MonthNumber { get; set; }
        public int Day { get; set; }
        public DateTime FullDate { get; set; }
        public bool Gender { get; set; } 
        public bool GenderShort { get; set; }
    }
}