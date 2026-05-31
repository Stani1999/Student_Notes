using System.Windows;
using Warehouse.ViewModels;

namespace Warehouse.Views
{
    /// <summary>
    /// Interaction logic for ReportWindow.xaml
    /// </summary>
    public partial class ReportWindow : Window
    {
        public ReportWindow(ReportViewModel viewModel)
        {
            InitializeComponent();
            DataContext = viewModel;
        }
    }
}