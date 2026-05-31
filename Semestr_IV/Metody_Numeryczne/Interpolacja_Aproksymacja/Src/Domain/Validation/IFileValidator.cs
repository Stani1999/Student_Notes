namespace Interpolacja_Aproksymacja.Domain.Validation
{
    public interface IFileValidator
    {
        void ValidateFormat(string filePath);
        bool IsDataRowValid(object valX, object valY);
    }
}