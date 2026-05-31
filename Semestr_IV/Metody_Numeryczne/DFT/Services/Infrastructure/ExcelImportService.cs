using DFT.Models;
using ExcelDataReader;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

namespace DFT.Services.Infrastructure
{
    public static class ExcelImportService
    {
        public static List<NoisySignalModel> ImportData(string filePath, int sheetIndex, string startCell)
        {
            System.Text.Encoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);
            var resultList = new List<NoisySignalModel>();

            ParseCellAddress(startCell, out int startRow, out int startCol);

            using var stream = File.Open(filePath, FileMode.Open, FileAccess.Read);
            using var reader = ExcelReaderFactory.CreateReader(stream);
            var dataSet = reader.AsDataSet();

            if (sheetIndex >= dataSet.Tables.Count) return resultList;

            var table = dataSet.Tables[sheetIndex];
            int nIndex = 0;

            for (int r = startRow; r < table.Rows.Count; r++)
            {
                var cellValue = table.Rows[r][startCol]?.ToString();
                if (double.TryParse(cellValue, out double val))
                {
                    resultList.Add(new NoisySignalModel { N = nIndex++, OriginalX = val });
                }
            }

            return resultList;
        }

        private static void ParseCellAddress(string cellAddress, out int row, out int col)
        {
            var match = Regex.Match(cellAddress.ToUpper(), @"([A-Z]+)(\d+)");
            if (!match.Success)
            {
                row = 0;
                col = 0;
                return;
            }

            string colStr = match.Groups[1].Value;
            int colIndex = 0;
            for (int i = 0; i < colStr.Length; i++)
            {
                colIndex = colIndex * 26 + (colStr[i] - 'A' + 1);
            }
            col = colIndex - 1;
            row = int.Parse(match.Groups[2].Value) - 1;
        }
    }
}