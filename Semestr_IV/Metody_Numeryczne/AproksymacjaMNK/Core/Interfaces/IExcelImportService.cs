using System.Collections.Generic;
using OxyPlot;

namespace AproksymacjaMNK.Core.Interfaces
{
    public interface IExcelImportService
    {
        List<DataPoint> ImportFromExcel(string filePath, string startAddress);
    }
}