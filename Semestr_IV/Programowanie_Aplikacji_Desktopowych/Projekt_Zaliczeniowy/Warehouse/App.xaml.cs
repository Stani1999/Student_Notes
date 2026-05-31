using System;
using System.Windows;
using FluentValidation;
using Microsoft.Extensions.DependencyInjection;
using Warehouse.Services.Application;
using Warehouse.Services.Infrastructure;
using Warehouse.Validators;
using Warehouse.ViewModels;
using Warehouse.Views;

namespace Warehouse
{
    public partial class App : Application
    {
        public new static App Current => (App)Application.Current;
        public IServiceProvider Services { get; }

        public App()
        {
            Services = ConfigureServices();
        }

        private static IServiceProvider ConfigureServices()
        {
            var services = new ServiceCollection();

            services.AddSingleton<IMongoService, MongoService>();

            services.AddTransient<CategoryService>();
            services.AddTransient<ProductService>();
            services.AddTransient<InventoryService>();
            services.AddTransient<ReportService>();
            services.AddTransient<OcrService>();
            services.AddTransient<TranslationService>();

            services.AddValidatorsFromAssemblyContaining<ProductValidator>();

            services.AddTransient<CategorySelectionViewModel>();
            services.AddTransient<MainViewModel>();
            services.AddTransient<ProductDetailsViewModel>();
            services.AddTransient<ReportViewModel>();

            services.AddTransient<MainWindow>();
            services.AddTransient<ReportWindow>();

            return services.BuildServiceProvider();
        }

        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            var mainWindow = Services.GetRequiredService<MainWindow>();
            mainWindow.Show();
        }
    }
}