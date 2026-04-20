using PESEL.Src.Data.Languages.UI;
using PESEL.Src.Interfaces;
using PESEL.Src.Interfaces.Languages;
using System.Windows.Controls;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Manages UI output controls by maintaining permanent references assigned during initialization.
    /// Eliminates the need to pass control arguments to individual display or clear methods.
    /// </summary>
    internal class PESELPresenter
    {
       
        private IOutLanguage _lang;
        // Private fields to store control references
        private readonly TextBox _outChecksum;
        private readonly TextBox _outYear;
        private readonly TextBox _outMonth;
        private readonly TextBox _outDay;
        private readonly TextBox _outMonthNumber;
        private readonly TextBox _outFullDate;
        private readonly TextBox _outGender;
        private readonly TextBox _outGenderS;

        /// <summary>
        /// Initializes a new instance of the PESELPresenter class with permanent control mappings.
        /// </summary>
        public PESELPresenter(
            TextBox outChecksum, TextBox outYear, TextBox outMonth,
            TextBox outDay, TextBox outMonthNumber, TextBox outFullDate,
            TextBox outGender, TextBox outGenderS)
        {
            _outChecksum = outChecksum;
            _outYear = outYear;
            _outMonth = outMonth;
            _outDay = outDay;
            _outMonthNumber = outMonthNumber;
            _outFullDate = outFullDate;
            _outGender = outGender;
            _outGenderS = outGenderS;
        }

        /// <summary>
        /// Populates the assigned UI controls with validated PESEL data.
        /// </summary>
        public void Display(IPESELData data)
        {
            _outChecksum.Text = data.RawPesel[10].ToString();
            _outYear.Text = data.Year.ToString();
            _outDay.Text = data.Day.ToString();
            _outMonth.Text = _lang.Months[data.Month - 1];
            _outMonthNumber.Text = data.MonthNumber.ToString("D2");
            _outFullDate.Text = data.FullDate.ToShortDateString();
            _outGender.Text = data.Gender ? _lang.Male : _lang.Female;
            _outGenderS.Text = data.GenderShort ? _lang.MaleShort : _lang.FemaleShort;
        }

        public void SetLanguage(IOutLanguage lang)
        {
            _lang = lang;
        }

        /// <summary>
        /// Resets all assigned output TextBox controls to an empty state.
        /// </summary>
        public void ClearControls()
        {
            _outChecksum.Text = string.Empty;
            _outYear.Text = string.Empty;
            _outMonth.Text = string.Empty;
            _outDay.Text = string.Empty;
            _outMonthNumber.Text = string.Empty;
            _outFullDate.Text = string.Empty;
            _outGender.Text = string.Empty;
            _outGenderS.Text = string.Empty;
        }
    }
}