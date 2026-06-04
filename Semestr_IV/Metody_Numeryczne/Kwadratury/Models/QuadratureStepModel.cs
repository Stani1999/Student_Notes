namespace Kwadratury.Models
{
    public class QuadratureStepModel
    {
        public int StepIndex { get; set; }
        public double X { get; set; }
        public double Y { get; set; }
        public double? X_Mid { get; set; }
        public double? Y_Mid { get; set; }
        public string StepDetails { get; set; } = string.Empty;
    }
}