using Microsoft.Win32;

namespace Interpolacja_Aproksymacja.ViewModels
{
    public class DialogService
    {
        public string OpenExcelFileDialog()
        {
            var dialog = new OpenFileDialog { Filter = "Excel Files|*.xls;*.xlsx" };
            return dialog.ShowDialog() == true ? dialog.FileName : null;
        }
    }
}