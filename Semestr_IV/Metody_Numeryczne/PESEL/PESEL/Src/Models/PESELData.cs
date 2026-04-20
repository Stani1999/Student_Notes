using System;
using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Represents the extracted data from a PESEL number, including raw PESEL, birth date
    /// </summary>
    internal class PESELData : IPESELData
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