using System;
using System.IO;
using Tesseract;

namespace Warehouse.Services.Application
{
    public class OcrService
    {
        public string ExtractTextFromImage(byte[] imageBytes)
        {
            if (imageBytes == null || imageBytes.Length == 0) return string.Empty;

            var tessDataPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "tessdata");
            if (!Directory.Exists(tessDataPath)) return "Brak folderu tessdata z plikami językowymi.";

            try
            {
                using var engine = new TesseractEngine(tessDataPath, "spa", EngineMode.Default);
                using var img = Pix.LoadFromMemory(imageBytes);
                using var page = engine.Process(img);
                return page.GetText();
            }
            catch (Exception ex)
            {
                return $"Błąd OCR: {ex.Message}";
            }
        }
    }
}