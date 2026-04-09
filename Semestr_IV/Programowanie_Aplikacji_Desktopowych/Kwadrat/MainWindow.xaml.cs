using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace Kwadrat
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void tbBok_TextChanged(object sender, TextChangedEventArgs e)
        {
            if (double.TryParse(tbBok.Text, out double a))
            {
                if (a >= 0)
                {
                    tbObwod.Text = (4 * a).ToString();
                    tbPole.Text = (a * a).ToString();
                    labelWorning.Visibility = Visibility.Hidden;
                }
                else
                {
                    tbObwod.Text = string.Empty;
                    tbPole.Text = string.Empty;
                    labelWorning.Content = "Czy ty kiedyś widziałeś bok ujemny?";
                    labelWorning.Visibility = Visibility.Visible;
                }
            }
            else
            {
                tbObwod.Text = string.Empty;
                tbPole.Text = string.Empty;

                if (!string.IsNullOrEmpty(tbBok.Text))
                {
                    labelWorning.Content = "Co ty p!";
                    labelWorning.Visibility = Visibility.Visible;
                }
                else
                {
                    labelWorning.Visibility = Visibility.Hidden;
                }
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            tbBok.Text = string.Empty;
            tbObwod.Text = string.Empty;
            tbPole.Text = string.Empty;
            labelWorning.Visibility = Visibility.Hidden;
            rectKwadrat.Width = 0;
            rectKwadrat.Height = 0;
        }

        private void btnRysuj_Click(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(tbBok.Text, out double a))
            {
                if (a >= 1 && a <= 300)
                {
                    rectKwadrat.Width = a;
                    rectKwadrat.Height = a;
                    labelWorning.Visibility = Visibility.Hidden;
                }
                else
                {
                    labelWorning.Content = "Zakres rysowania: 1 - 300 px";
                    labelWorning.Visibility = Visibility.Visible;
                }
            }
        }

        private void CheckBox_Checked(object sender, RoutedEventArgs e)
        {
            if (rectKwadrat != null && sliderPrzezroczystosc != null)
            {
                rectKwadrat.Opacity = (cbPrzezroczystosc.IsChecked == true) ? sliderPrzezroczystosc.Value : 1.0;
            }
        }

        private void ComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if (rectKwadrat == null) return;

            var selectedItem = (ComboBoxItem)cbKolor.SelectedItem;
            string kolor = selectedItem.Content.ToString();

            switch (kolor)
            {
                case "Red": rectKwadrat.Fill = Brushes.Red; break;
                case "Green": rectKwadrat.Fill = Brushes.Green; break;
                case "Blue": rectKwadrat.Fill = Brushes.Blue; break;
            }
        }

        private void sliderPrzezroczystosc_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (rectKwadrat != null && cbPrzezroczystosc.IsChecked == true)
            {
                rectKwadrat.Opacity = sliderPrzezroczystosc.Value;
            }
        }
    }
}