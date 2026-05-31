namespace Interpolacja_Aproksymacja.Domain.Validation
{
    public class IsNumericRule : IValidationRule<object>
    {
        public string ErrorMessage => "Wartość nie jest liczbą.";
        public bool IsValid(object value) => double.TryParse(value?.ToString(), out _);
    }

    public class NotNullRule : IValidationRule<object>
    {
        public string ErrorMessage => "Wartość jest pusta.";
        public bool IsValid(object value) => value != null;
    }
}