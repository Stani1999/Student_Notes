using System;

namespace PESEL.Src.Validations
{
    internal class PESELDateValidator
    {
        /// <summary>
        /// Data validation method that extracts the date of birth from the PESEL number and determines the century.
        /// </summary>
        /// <param name="pesel"></param>
        /// <param name="date"></param>
        /// <param name="century"></param>
        /// <returns></returns>
        public bool TryGetDate(string pesel, out DateTime date, out int century)
        {
            // Initialize output parameters
            date = default;
            century = 0;

            // Extract the year, month, and day components from the PESEL string
            int year = int.Parse(pesel.Substring(0, 2));
            int month = int.Parse(pesel.Substring(2, 2));
            int day = int.Parse(pesel.Substring(4, 2));
            bool GendrFlag = int.Parse(pesel.Substring(9, 1)) % 2 == 0;
            bool GendrFlagShort = int.Parse(pesel.Substring(9, 1)) % 2 == 0; 

            // Determine the century based on the month value and adjust the month accordingly
            if (month > 80) { century = 1800; month -= 80; }
            else if (month > 60) { century = 2200; month -= 60; }
            else if (month > 40) { century = 2100; month -= 40; }
            else if (month > 20) { century = 2000; month -= 20; }
            else { century = 1900; }

            // Validate the date using DateTime.TryParse to ensure it's a valid calendar date
            return DateTime.TryParse($"{century + year}-{month:D2}-{day:D2}", out date);
        }
    }
}