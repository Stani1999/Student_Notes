using System.Collections.Generic;
using System.Linq;

namespace Interpolacja_Aproksymacja.Domain.Validation
{
    public class DataValidator<T>
    {
        private readonly List<IValidationRule<T>> _rules = new List<IValidationRule<T>>();

        public void RegisterRule(IValidationRule<T> rule) => _rules.Add(rule);

        public (bool IsValid, List<string> Errors) Validate(T value)
        {
            var errors = _rules
                .Where(r => !r.IsValid(value))
                .Select(r => r.ErrorMessage)
                .ToList();

            return (errors.Count == 0, errors);
        }
    }
}