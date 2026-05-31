using System.Collections.Generic;
using System.IO;
using ExcelDataReader;

namespace Interpolacja_Aproksymacja.Infrastructure
{
    public class ExcelReaderService
    {
        public List<object[]> ReadRows(string filePath, int startRow, int startColumn)
        {
            var rows = new List<object[]>();
            using (var stream = File.Open(filePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
            {
                using (var reader = ExcelReaderFactory.CreateReader(stream))
                {
                    int currentRow = 0;
                    while (reader.Read())
                    {
                        if (currentRow < startRow)
                        {
                            currentRow++;
                            continue;
                        }

                        if (reader.FieldCount > startColumn + 1)
                        {
                            var data = new object[2];
                            data[0] = reader.GetValue(startColumn);
                            data[1] = reader.GetValue(startColumn + 1);
                            rows.Add(data);
                        }
                        currentRow++;
                    }
                }
            }
            return rows;
        }
    }
}