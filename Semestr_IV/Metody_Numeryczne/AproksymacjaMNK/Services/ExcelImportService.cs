using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using ExcelDataReader;
using OxyPlot;
using AproksymacjaMNK.Core.Interfaces;

namespace AproksymacjaMNK.Services
{
    public class ExcelImportService : IExcelImportService
    {
        public List<DataPoint> ImportFromExcel(string filePath, string startAddress)
        {
            var points = new List<DataPoint>();

            using (var stream = File.Open(filePath, FileMode.Open, FileAccess.Read))
            {
                using (var reader = ExcelReaderFactory.CreateReader(stream))
                {
                    var result = reader.AsDataSet();

                    if (result.Tables.Count == 0)
                        throw new Exception("Plik Excel jest pusty.");

                    var table = result.Tables[0];

                    int startRow = int.Parse(new string(startAddress.Where(char.IsDigit).ToArray())) - 1;
                    int startCol = startAddress.ToUpper().First(c => c >= 'A' && c <= 'Z') - 'A';

                    for (int i = startRow; i < table.Rows.Count; i++)
                    {
                        var row = table.Rows[i];

                        if (row[startCol] == DBNull.Value || row[startCol + 1] == DBNull.Value)
                            break;

                        try
                        {
                            double x = Convert.ToDouble(row[startCol]);
                            double y = Convert.ToDouble(row[startCol + 1]);
                            points.Add(new DataPoint(x, y));
                        }
                        catch
                        {
                            break;
                        }
                    }
                }
            }

            if (points.Count < 2)
                throw new Exception("Wczytano za mało punktów (minimum 2), aby przeprowadzić regresję.");

            return points;
        }
    }
}