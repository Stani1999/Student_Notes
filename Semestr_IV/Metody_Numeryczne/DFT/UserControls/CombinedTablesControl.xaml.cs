using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace DFT.UserControls
{
    /// <summary>
    /// Interaction logic for CombinedTablesControl.xaml
    /// </summary>
    public partial class CombinedTablesControl : UserControl
    {
        public CombinedTablesControl()
        {
            InitializeComponent();
        }

        private void UserControl_Loaded(object sender, RoutedEventArgs e)
        {
            var sv1 = GetScrollViewer(NoisyData);
            var sv2 = GetScrollViewer(DenoisedData);

            if (sv1 != null && sv2 != null)
            {
                sv1.ScrollChanged += (s, args) =>
                {
                    if (args.VerticalChange != 0)
                        sv2.ScrollToVerticalOffset(args.VerticalOffset);
                };

                sv2.ScrollChanged += (s, args) =>
                {
                    if (args.VerticalChange != 0)
                        sv1.ScrollToVerticalOffset(args.VerticalOffset);
                };
            }
        }

        private ScrollViewer? GetScrollViewer(DependencyObject depObj)
        {
            if (depObj is ScrollViewer scrollViewer) return scrollViewer;

            for (int i = 0; i < VisualTreeHelper.GetChildrenCount(depObj); i++)
            {
                var child = VisualTreeHelper.GetChild(depObj, i);
                var result = GetScrollViewer(child);
                if (result != null) return result;
            }
            return null;
        }
    }
}