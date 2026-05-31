using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.ObjectModel;

namespace WpfApp4
{
    internal class Dane
    {
        public string indeks { get; set; }
        public string nazwa { get; set; }
        public int ilosc { get; set; }
        public string miasto { get; set; }

        public Dane(string indeks, string nazwa, int ilosc, string miasto)
        {
            this.indeks = indeks;
            this.nazwa = nazwa;
            this.ilosc = ilosc;
            this.miasto = miasto;
        }

        public override string ToString()
        {
            return String.Format("{0} {1} {2} {3}", indeks, nazwa, ilosc, miasto);
        }
    }
}