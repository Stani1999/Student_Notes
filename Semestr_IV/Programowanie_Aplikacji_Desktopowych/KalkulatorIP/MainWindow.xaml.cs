using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Net;

namespace KalkulatorIP
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        private void B_Oblicz_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                IPNetwork2 ipn2 = IPNetwork2.Parse(TBX_InputIP.Text.Trim());

                TB_Result.Text = "";
                TB_Result.Text += "Adres Sieci: " + ipn2.Network.ToString() + "\n";
                TB_Result.Text += "Broadcast: " + ipn2.Broadcast.ToString() + "\n";
                TB_Result.Text += "Maska: " + ipn2.Netmask.ToString() + "\n";
                TB_Result.Text += "Pierwszy dostępny adres: " + ipn2.FirstUsable.ToString() + "\n";
                TB_Result.Text += "Ostatni dostępny adres: " + ipn2.LastUsable.ToString() + "\n";
                TB_Result.Text += "Liczba hostów: " + ipn2.Usable.ToString() + "\n";
                TB_Result.Text += "CIDR: " + ipn2.Cidr.ToString() + "\n";
            }
            catch (Exception ex)
            {
                TB_Result.Text = "Błąd: " + ex.Message;
            }
        }
    }
}