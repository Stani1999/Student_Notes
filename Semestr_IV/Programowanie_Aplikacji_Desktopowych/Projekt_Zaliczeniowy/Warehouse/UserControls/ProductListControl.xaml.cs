using System.Windows.Controls;
using System.Windows.Input;
using Warehouse.ViewModels;

namespace Warehouse.UserControls
{
    public partial class ProductListControl : UserControl
    {
        public ProductListControl()
        {
            InitializeComponent();
        }

        private void DataGrid_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            if (DataContext is MainViewModel mainViewModel && mainViewModel.SelectedProduct != null)
            {
                mainViewModel.ShowEditDetailsCommand.Execute(mainViewModel.SelectedProduct);
            }
        }
    }
}