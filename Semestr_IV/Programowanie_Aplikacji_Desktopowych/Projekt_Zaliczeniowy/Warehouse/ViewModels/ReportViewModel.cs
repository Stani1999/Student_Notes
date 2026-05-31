using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using Microsoft.Win32;
using System;
using System.Collections.ObjectModel;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Warehouse.Models;
using Warehouse.Services.Application;

namespace Warehouse.ViewModels
{
    public partial class ReportViewModel : ObservableObject
    {
        private readonly ReportService _reportService;

        [ObservableProperty]
        private ObservableCollection<int> _years = new();

        [ObservableProperty]
        private int _selectedYear;

        [ObservableProperty]
        private ObservableCollection<int> _months = new();

        [ObservableProperty]
        private int _selectedMonth;

        [ObservableProperty]
        private ObservableCollection<InventoryReportRow> _reportData = new();

        public ReportViewModel(ReportService reportService)
        {
            _reportService = reportService;

            var currentYear = DateTime.Now.Year;
            for (int i = currentYear - 5; i <= currentYear; i++)
            {
                Years.Add(i);
            }
            SelectedYear = currentYear;

            for (int i = 1; i <= 12; i++)
            {
                Months.Add(i);
            }
            SelectedMonth = DateTime.Now.Month;
        }

        public async Task InitializeAsync()
        {
            await GenerateReportAsync();
        }

        [RelayCommand]
        private async Task GenerateReportAsync()
        {
            var data = await _reportService.GetMonthlyReportAsync(SelectedYear, SelectedMonth);
            ReportData.Clear();
            foreach (var item in data)
            {
                ReportData.Add(item);
            }
        }

        [RelayCommand]
        private void SaveToFile()
        {
            if (ReportData.Count == 0) return;

            var dialog = new SaveFileDialog
            {
                Filter = "Plik tekstowy (*.txt)|*.txt",
                DefaultExt = ".txt",
                FileName = $"Raport_Magazyn_{SelectedYear}_{SelectedMonth:D2}"
            };

            if (dialog.ShowDialog() == true)
            {
                var sb = new StringBuilder();
                sb.AppendLine($"=== RAPORT MAGAZYNOWY: {SelectedYear}-{SelectedMonth:D2} ===");
                sb.AppendLine($"Data wygenerowania: {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
                sb.AppendLine();
                sb.AppendLine(string.Format("{0,-40} | {1,-10} | {2,-10}", "Produkt", "Przyjeto", "Wydano"));
                sb.AppendLine(new string('-', 68));

                foreach (var row in ReportData)
                {
                    sb.AppendLine(string.Format("{0,-40} | {1,-10} | {2,-10}",
                        row.ProductName.Length > 38 ? row.ProductName.Substring(0, 38) : row.ProductName,
                        row.Received,
                        row.Issued));
                }

                File.WriteAllText(dialog.FileName, sb.ToString());
            }
        }
    }
}