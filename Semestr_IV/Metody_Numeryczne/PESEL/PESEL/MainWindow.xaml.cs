using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace PESEL
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void B_Check_Click(object sender, RoutedEventArgs e)
        {
            string pesel = TBX_Pesel.Text.Trim().Replace(" ", "");
                try
                {
                string error = string.IsNullOrEmpty(pesel) ? "Pole PESEL nie może być puste!\nJak obietnice wyborcze..." :
                    pesel.Length !=11 ? "Czy widziałeś, kiedyś jak wygląda Pesel?\nMusi się składać z 11 cyfr" :
                    !pesel.All(char.IsDigit) ? "Tylko liczby 0-9,\nRzymskie IV oraz zanki specjalne nie przejdą..." :
                    null;

                if (error != null) throw new Exception(error);
            }

                catch (Exception error) 
                {
                    MessageBox.Show(error.Message, "Błąd", MessageBoxButton.OK, MessageBoxImage.Error);
                }
        }
    }
}
