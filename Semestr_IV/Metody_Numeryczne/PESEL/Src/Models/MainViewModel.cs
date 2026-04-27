using System.ComponentModel;
using System.Runtime.CompilerServices;
using PESEL.Src.Interfaces.Languages;

namespace PESEL.Src.Models
{
    /// <summary>
    /// Provides current language pack for UI binding
    /// and notifies view about language changes.
    /// </summary>
    internal class MainViewModel : INotifyPropertyChanged
    {
        private readonly ILanguageManager _langManager;

        /// <summary>
        /// Full language pack (UI + Errors + Output)
        /// </summary>
        public ILanguagePack CurrentLanguage => _langManager.Current;

        public MainViewModel()
        {
            _langManager = new LanguageManager();
        }

        /// <summary>
        /// Switch language and notify UI bindings.
        /// </summary>
        public void ChangeLanguage()
        {
            _langManager.ChangeLanguage();
            OnPropertyChanged(nameof(CurrentLanguage));
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged([CallerMemberName] string name = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        }
    }
}