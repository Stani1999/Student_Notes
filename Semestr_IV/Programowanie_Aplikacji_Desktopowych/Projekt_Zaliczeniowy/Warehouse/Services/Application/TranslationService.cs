using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace Warehouse.Services.Application
{
    public class TranslationService
    {
        private readonly HttpClient _httpClient;

        public TranslationService()
        {
            _httpClient = new HttpClient();
        }

        public async Task<string> TranslateSpanishToPolishAsync(string text)
        {
            if (string.IsNullOrWhiteSpace(text)) return string.Empty;

            try
            {
                string url = $"https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=pl&dt=t&q={Uri.EscapeDataString(text)}";
                var response = await _httpClient.GetStringAsync(url);

                using var doc = JsonDocument.Parse(response);
                var sb = new StringBuilder();

                foreach (var element in doc.RootElement[0].EnumerateArray())
                {
                    sb.Append(element[0].GetString());
                }

                return sb.ToString();
            }
            catch (Exception ex)
            {
                return $"Błąd API tłumacza: {ex.Message}";
            }
        }
    }
}