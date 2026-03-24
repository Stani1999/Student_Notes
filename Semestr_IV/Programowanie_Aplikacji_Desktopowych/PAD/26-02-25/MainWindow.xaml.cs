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

namespace _26_02_25
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

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            // Monit napewno?
            if (MessageBox.Show("Czy na pewno?", "Pytanie", MessageBoxButton.YesNo, MessageBoxImage.Question) == MessageBoxResult.Yes)
            {
                // Tak
                MessageBox.Show("No dobra");
            }
            else
            {
                // Nie
                MessageBox.Show("aha");
            }
        }

        private void bKliknij2_MouseEnter(object sender, MouseEventArgs e)
        {
            // Wyświetlanie daty systemowej
            DateTime dt = DateTime.Now;
            bKliknij2.Content = dt.ToString("t");
        }

        private void bKliknij2_MouseLeave(object sender, MouseEventArgs e)
        {
            bKliknij2.Content = "YES";
        }

        private void bKliknij_MouseEnter(object sender, MouseEventArgs e)
        {
            bKliknij.Visibility = Visibility.Hidden;
        }

        private void bKliknij2_Click(object sender, RoutedEventArgs e)
        {

        }


    }
}