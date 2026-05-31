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
using System.Windows.Shapes;

namespace WpfApp4
{
    /// <summary>
    /// Logika interakcji dla klasy Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        private MainWindow mw = null;
        public Window1(MainWindow mw)
        {
            InitializeComponent();
            this.mw = mw;
            Wiazanie();
        }
        private void Wiazanie()
        {
            Dane d = mw.lvLista.SelectedItem as Dane;
            if (d != null)
            {
                GEdycja.DataContext = d;
            }
        }

        private void Zapisz_Click(object sender, RoutedEventArgs e)
        {
            this.DialogResult = true;
        }
        // dodac przycisk do usuwania danych zaznaczonych wybrana pozycja i dodawanie nowej pozycji
    }
}
