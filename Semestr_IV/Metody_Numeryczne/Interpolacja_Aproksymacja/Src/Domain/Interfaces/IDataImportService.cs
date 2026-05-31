using OxyPlot;
using System.Collections.Generic;

namespace Interpolacja_Aproksymacja.Domain.Interfaces
{
    public interface IDataImportService
    {
        List<DataPoint> ImportFromExcel(string filePath, string startAddress);
    }
}