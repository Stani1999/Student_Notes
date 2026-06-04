using NCalc;
using System;

namespace Kwadratury.Services.Application
{
    public class FunctionParserService
    {
        public Func<double, double> Parse(string expression)
        {
            return x =>
            {
                var e = new Expression(expression);
                e.Parameters["x"] = x;
                return Convert.ToDouble(e.Evaluate());
            };
        }
    }
}