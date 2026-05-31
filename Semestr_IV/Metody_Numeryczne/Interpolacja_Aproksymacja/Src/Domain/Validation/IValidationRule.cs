namespace Interpolacja_Aproksymacja.Domain.Validation
{
    public interface IValidationRule<T>
    {
        bool IsValid(T value);
        string ErrorMessage { get; }
    }
}