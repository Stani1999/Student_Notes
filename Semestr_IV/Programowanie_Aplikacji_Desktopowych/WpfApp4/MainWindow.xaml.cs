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
using System.Collections.ObjectModel;
using System.ComponentModel;

namespace WpfApp4
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
            dane.Add(new Dane("x1", "ACMAMS", 1232, "Płock"));
            dane.Add(new Dane("y1", "CFKKSO", 5, "Warszawa"));
            dane.Add(new Dane("xy", "DDKKSKS", 33, "Kraków"));
            dane.Add(new Dane("z2", "BAAASS", 222222, "Gdańsk"));
            lvLista.ItemsSource = dane;
            CollectionView cv = (CollectionView)CollectionViewSource.GetDefaultView(lvLista.ItemsSource);
            cv.SortDescriptions.Add(new SortDescription("miasto", ListSortDirection.Ascending));
            cv.SortDescriptions.Add(new SortDescription("nazwa", ListSortDirection.Descending));
            cv.Filter = Filtrowanie;
        }

        private bool Filtrowanie(object item)
        {
            if (String.IsNullOrEmpty(Filtr.Text))
                return true;
            else return ((item as Dane).nazwa.IndexOf(Filtr.Text, StringComparison.OrdinalIgnoreCase) >= 0);
        }

        private void Filtr_TextChanged(object sender, TextChangedEventArgs e)
        {
            CollectionViewSource.GetDefaultView(lvLista.ItemsSource).Refresh();
        }

        private void lvLista_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            Window1 w1 = new Window1(this);
            w1.ShowDialog();
        }

        private void Usun_Click(object sender, RoutedEventArgs e)
        {
            Dane d = lvLista.SelectedItem as Dane;
            if (d != null)
            {
                MessageBoxResult mbr = MessageBox.Show("Czy ty o tym wiesz?: " + d.ToString() + "?", "Usuwanie czegokolwie", MessageBoxButton.YesNo, 
                    MessageBoxImage.Question);

                if (mbr == MessageBoxResult.Yes)
                {
                    dane.Remove(d);
                }
            }
        }
    }
}
