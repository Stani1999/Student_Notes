using System;
using System.Windows;
using PESEL.Src.Models;
using PESEL.Src.Languages.Errors;
using PESEL.Src.Interfaces;


namespace PESEL
{

    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void B_Check_Click(object sender, RoutedEventArgs e)
        {
            // Decide which provider to use (could be based on a ComboBox)
            IErrorsLanguage provider = new ErrorsPL();
            // or: IErrorsLanguage provider = new ErrorsEN();

            try
            {
                var pModel = new PESELModel(TBX_Pesel.Text.Trim(), provider);
                MessageBox.Show("Poprawny PESEL!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Błąd");
            }
        }
    }
}
