using FluentValidation;
using Microsoft.Extensions.DependencyInjection;
using Schemat_Hornera.Validators;
using Schemat_Hornera.ViewModels;
using System.Windows;

namespace Schemat_Hornera
{
    public partial class App : Application
    {
        private ServiceProvider _serviceProvider;

        public App()
        {
            var services = new ServiceCollection();

            services.AddValidatorsFromAssemblyContaining<MainViewModelValidator>();

            services.AddTransient<MainViewModel>();
            services.AddTransient<MainWindow>();

            _serviceProvider = services.BuildServiceProvider();
        }

        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            var mainWindow = _serviceProvider.GetRequiredService<MainWindow>();
            mainWindow.DataContext = _serviceProvider.GetRequiredService<MainViewModel>();
            mainWindow.Show();
        }
    }
}