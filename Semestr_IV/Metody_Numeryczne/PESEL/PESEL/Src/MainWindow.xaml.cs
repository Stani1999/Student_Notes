using PESEL.Src.Interfaces.Languages;
using PESEL.Src.Models;
using System;
using System.Windows;
using System.Windows.Input;

namespace PESEL.Src
{
    /// <summary>
    /// Main application window.
    /// Responsible for coordinating user interactions,
    /// validation workflow, and delegating UI updates to the presenter.
    /// </summary>
    public partial class MainWindow : Window
    {
        private readonly MainViewModel _viewModel;
        private readonly PESELPresenter _presenter;

        /// <summary>
        /// Initializes the main window, sets up data binding,
        /// creates presenter and initializes default language to prevent null reference issues.
        /// </summary>
        public MainWindow()
        {
            _viewModel = new MainViewModel();
            this.DataContext = _viewModel;

            InitializeComponent();

            // Presenter is responsible only for displaying formatted output in UI controls
            _presenter = new PESELPresenter(
                outChecksum,
                outYear,
                outMonth,
                outDay,
                outMonthNumber,
                outFullDate,
                outGender,
                outGenderS
            );

            // IMPORTANT:
            // Initialize presenter with default language at startup
            // to avoid null reference on first display
            _presenter.SetLanguage(_viewModel.CurrentLanguage.Output);
        }

        /// <summary>
        /// Handles PESEL validation triggered by user action.
        /// Uses current language pack for validation and output formatting.
        /// </summary>
        private void btnCheck_Click(object sender, RoutedEventArgs e)
        {
            ILanguagePack lang = _viewModel.CurrentLanguage;
            IErrorsLanguage errors = lang.Errors;

            try
            {
                var validator = new PESELValidator(tbxPesel.Text.Trim(), errors);

                IPESELData data = validator.GetValidatedData();

                // Inject correct output language before displaying data
                _presenter.SetLanguage(lang.Output);
                _presenter.Display(data);
            }
            catch (Exception ex)
            {
                _presenter.ClearControls();

                MessageBox.Show(
                    ex.Message,
                    errors.Title,
                    MessageBoxButton.OK,
                    MessageBoxImage.Error
                );
            }
        }

        /// <summary>
        /// Toggles application language (PL / EN).
        /// UI bindings update automatically via ViewModel.
        /// </summary>
        private void btnLanguage_Click(object sender, RoutedEventArgs e)
        {
            _viewModel.ChangeLanguage();

            // Ensure presenter is updated after language switch
            _presenter.SetLanguage(_viewModel.CurrentLanguage.Output);

            // Clear previous output to avoid confusion after language change
            _presenter.ClearControls();

        }
    }
}