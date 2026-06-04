using FluentValidation;
using Kwadratury.Interfaces;
using Kwadratury.Services.Algorithms;
using Kwadratury.Services.Application;
using Kwadratury.Services.PlottingStrategies;
using Kwadratury.ViewModels;
using Kwadratury.Views;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Windows;

namespace Kwadratury
{
    public partial class App : Application
    {
        private readonly IServiceProvider _serviceProvider;

        public App()
        {
            var services = new ServiceCollection();
            ConfigureServices(services);
            _serviceProvider = services.BuildServiceProvider();
        }

        private void ConfigureServices(IServiceCollection services)
        {
            services.AddSingleton<MainWindow>();
            services.AddTransient<MainViewModel>();

            services.AddTransient<FunctionParserService>();
            services.AddValidatorsFromAssemblyContaining<App>();

            services.AddTransient<IQuadratureMethod, RectangleLeftMethod>();
            services.AddTransient<IQuadratureMethod, RectangleMidMethod>();
            services.AddTransient<IQuadratureMethod, RectangleRightMethod>();
            services.AddTransient<IQuadratureMethod, TrapezoidalMethod>();
            services.AddTransient<IQuadratureMethod, SimpsonMethod>();
            services.AddTransient<IQuadratureMethod, GaussLegendreMethod>();

            services.AddSingleton<IPlottingStrategy, RectangleLeftPlottingStrategy>();
            services.AddSingleton<IPlottingStrategy, RectangleMidPlottingStrategy>();
            services.AddSingleton<IPlottingStrategy, RectangleRightPlottingStrategy>();
            services.AddSingleton<IPlottingStrategy, TrapezoidalPlottingStrategy>();
            services.AddSingleton<IPlottingStrategy, SimpsonPlottingStrategy>();
            services.AddSingleton<IPlottingStrategy, GaussPlottingStrategy>();

            services.AddSingleton<QuadraturePlotService>();
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