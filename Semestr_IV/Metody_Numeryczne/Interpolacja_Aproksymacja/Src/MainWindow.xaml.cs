using System.Windows;
using Interpolacja_Aproksymacja.ViewModels;

namespace Interpolacja_Aproksymacja
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DataContext = new MainViewModel();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
        }
    }
}