using System;

namespace PESEL.Src.Interfaces.Languages
{
    /// <summary>
    /// Defines the contract for accessing parsed data from a PESEL (Polish national identification number).
    /// </summary>
    /// <remarks>Implementations provide access to individual components of a PESEL, such as the raw value,
    /// date of birth, and gender information. This interface is intended for internal use within components that
    /// process or validate PESEL numbers.</remarks>
    internal interface IPESELData
    {
        string RawPesel { get; }
        int Year { get; }
        int Month { get; }
        int MonthNumber { get; }
        int Day { get; }
        DateTime FullDate { get; }
        bool Gender { get; }
        bool GenderShort { get; }
    }
}