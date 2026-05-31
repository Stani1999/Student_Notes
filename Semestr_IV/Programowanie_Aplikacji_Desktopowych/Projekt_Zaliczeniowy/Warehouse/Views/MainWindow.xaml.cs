using System;
using System.Windows;
using Microsoft.Extensions.DependencyInjection;
using Warehouse.ViewModels;

namespace Warehouse.Views
{
    public partial class MainWindow : Window
    {
        private readonly IServiceProvider _serviceProvider;

        public MainWindow(MainViewModel viewModel, IServiceProvider serviceProvider)
        {
            InitializeComponent();
            DataContext = viewModel;
            _serviceProvider = serviceProvider;
        }

        private void OpenReports_Click(object sender, RoutedEventArgs e)
        {
            var window = _serviceProvider.GetRequiredService<ReportWindow>();
            if (window.DataContext is ReportViewModel vm)
            {
                _ = vm.InitializeAsync();
            }
            window.ShowDialog();
        }
    }
}