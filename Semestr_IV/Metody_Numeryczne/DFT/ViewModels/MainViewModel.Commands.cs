using CommunityToolkit.Mvvm.Input;
using DFT.Models;
using DFT.Services.Application;
using DFT.Services.Infrastructure;
using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
using System.Windows;

namespace DFT.ViewModels
{
    public partial class MainViewModel
    {
        [RelayCommand]
        private void BrowseFile()
        {
            var dialog = new OpenFileDialog { Filter = "Excel Files|*.xls;*.xlsx" };
            if (dialog.ShowDialog() == true)
            {
                ExcelFilePath = dialog.FileName;
            }
        }

        [RelayCommand]
        private void AnalyzeData()
        {
            ClearErrors();

            var validationResult = _validator.Validate(this);

            if (!validationResult.IsValid)
            {
                foreach (var error in validationResult.Errors)
                {
                    AddError(error.PropertyName, error.ErrorMessage);
                }
                return;
            }

            List<NoisySignalModel> importedData;

            try
            {
                importedData = ExcelImportService.ImportData(ExcelFilePath, SheetIndex, StartCell);
            }
            catch (IOException)
            {
                MessageBox.Show("Plik jest aktualnie niedostępny. Prawdopodobnie jest otwarty w innym programie lub został usunięty.\nProszę go zamknąć lub wybrać inny.", "Brak dostępu do pliku", MessageBoxButton.OK, MessageBoxImage.Warning);
                return;
            }
            catch (Exception)
            {
                MessageBox.Show("Wystąpił nieoczekiwany błąd podczas wczytywania pliku.", "Błąd", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            string currentDataSource = $"{ExcelFilePath}|{SheetIndex}|{StartCell}";

            if (importedData.Count > 0 && currentDataSource != _lastDataSource)
            {
                NoiseThreshold = ThresholdCalculationService.CalculateDefaultThreshold(importedData.Count);
                _lastDataSource = currentDataSource;
            }

            DftCalculationService.CalculateDft(importedData);

            var filteredData = SpectrumThresholdService.FilterSpectrum(importedData, NoiseThreshold);

            IdftCalculationService.CalculateIdft(filteredData);

            SignalReconstructionService.ExtractRealSignal(filteredData);

            NoisySignals.Clear();
            foreach (var item in importedData) NoisySignals.Add(item);

            DenoisedSignals.Clear();
            foreach (var item in filteredData) DenoisedSignals.Add(item);

            Plots.SpectrumPlot = PlotGeneratorService.GenerateSpectrumPlot(importedData, filteredData);
            Plots.ComparisonPlot = ComparisonPlotGenerator.GenerateComparisonPlot(importedData, filteredData);

            IsSettingsChangedInfoVisible = false;
        }
    }
}