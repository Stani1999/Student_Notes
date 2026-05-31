using Warehouse.Models.Types;

namespace Warehouse.Models
{
    /// <summary>
    /// Represents a monetary value and its associated currency. 
    /// Designed as a Value Object to be embedded directly within product documents.
    /// </summary>
    public class Price
    {
        public decimal Amount { get; set; }
        public Currency Currency { get; set; }
    }
}