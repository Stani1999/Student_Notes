using System;
using System.IO;

namespace Interpolacja_Aproksymacja.Domain.Validation
{
    public class ExcelFileValidator : IFileValidator
    {
        public void ValidateFormat(string filePath)
        {
            if (string.IsNullOrWhiteSpace(filePath))
                throw new ArgumentException("Ścieżka do pliku nie może być pusta.");

            if (!File.Exists(filePath))
                throw new FileNotFoundException($"Plik nie istnieje: {filePath}");

            string extension = Path.GetExtension(filePath).ToLower();
            if (extension != ".xls" && extension != ".xlsx")
                throw new InvalidDataException("Nieprawidłowy format. Obsługiwane pliki: .xls, .xlsx");

            try
            {
                using (FileStream stream = File.Open(filePath, FileMode.Open, FileAccess.Read, FileShare.None))
                {

                }
            }
            catch (IOException)
            {
                throw new IOException("Plik jest otwarty w innym programie. Zamknij go przed importem.");
            }
        }

        public bool IsDataRowValid(object valX, object valY)
        {
            if (valX == null || valY == null) return false;
            return double.TryParse(valX.ToString(), out _) && double.TryParse(valY.ToString(), out _);
        }
    }
}