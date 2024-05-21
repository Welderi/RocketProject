using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Media.Media3D;
using System.Windows.Data;
using MathNet.Symbolics;
using OxyPlot;
using OxyPlot.Series;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;    

namespace Code
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public PlotModel MyModel { get; private set; }

        public MainWindow()
        {
            InitializeComponent();
            SetupModel();
            DataContext = this;
        }

        public void CreateGraf(object sender, RoutedEventArgs e)
        {
            MyModel.Series.Clear();

            var series = new LineSeries
            {
                Title = "f(x) = x^2",
                StrokeThickness = 2,
                MarkerType = MarkerType.Circle,
                MarkerSize = 3,
                MarkerStroke = OxyColors.DarkRed
            };

            for (int x = -10; x <= 10; x++)
            {
                double y = Math.Pow(x, 2);
                series.Points.Add(new DataPoint(x, y));
            }

            MyModel.Series.Add(series);

            MyModel.InvalidatePlot(true);
        }

        private void SetupModel()
        {
            MyModel = new PlotModel { Title = "Graph of the Function" };
        }
    }
}
