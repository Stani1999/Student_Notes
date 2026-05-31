namespace Warehouse.Models
{
    public class InventoryReportRow
    {
        public string ProductName { get; set; } = string.Empty;
        public int Received { get; set; }
        public int Issued { get; set; }
    }
}