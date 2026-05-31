using System;
using System.Collections.Generic;
using System.Linq;
using OxyPlot;
using Interpolacja_Aproksymacja.Domain.Interfaces;
using Interpolacja_Aproksymacja.Domain.Validation;

namespace Interpolacja_Aproksymacja.Infrastructure
{
    public class ExcelDataImportService : IDataImportService
    {
        private readonly IFileValidator _fileValidator;
        private readonly ExcelReaderService _reader;

        public ExcelDataImportService(IFileValidator fileValidator, ExcelReaderService reader)
        {
            _fileValidator = fileValidator;
            _reader = reader;
        }

        public List<DataPoint> ImportFromExcel(string filePath, string startAddress)
        {
            _fileValidator.ValidateFormat(filePath);

            var (startRow, startCol) = ParseAddress(startAddress);
            var rawData = _reader.ReadRows(filePath, startRow, startCol);

            var points = new List<DataPoint>();
            foreach (var row in rawData)
            {
                if (double.TryParse(row[0]?.ToString(), out double x) &&
                    double.TryParse(row[1]?.ToString(), out double y))
                {
                    points.Add(new DataPoint(x, y));
                }
            }
            return points;
        }

        private (int row, int col) ParseAddress(string address)
        {
            try
            {
                string colPart = new string(address.Where(char.IsLetter).ToArray()).ToUpper();
                string rowPart = new string(address.Where(char.IsDigit).ToArray());
                int col = 0;
                foreach (char c in colPart) col = col * 26 + (c - 'A' + 1);
                return (int.Parse(rowPart) - 1, col - 1);
            }
            catch { return (0, 0); }
        }
    }
}