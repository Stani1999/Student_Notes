using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
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
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Komponent
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private ObservableCollection<Dane> dane = null;
        public MainWindow()
        {
            InitializeComponent();
            Wiazanie();
        }

        private void Wiazanie()
        {
            dane = new ObservableCollection<Dane>();
            dane.Add(new Dane("x1", "okno1", 1, "Płock"));
            dane.Add(new Dane("y1", "okno2", 5, "Warszawa"));
            dane.Add(new Dane("xy", "okno3", 3, "Kraków"));
            dane.Add(new Dane("z2", "okno4", 2, "Gdańsk"));
            lvLista.ItemsSource = dane;
        }
    }
}
