import java.util.Date;
import java.util.GregorianCalendar;

public class Pracownik_info {

    public static void main(String[] args) {
        //Tabloica x elementowa do przechowywania informacji
        Pracownik[] wol = new Pracownik[3];

        // Inicjalizacja pracowników na żądanych indeksach
        wol[1] = new Pracownik("Prezydent", 15000.0, 1, 5, 2025);
        wol[2] = new Pracownik("Prezydenter", 15000.0, 1, 5, 2025);

        // Pętla for do wyświetlenia pracowników od indeksu 1 do 2
        System.out.println("\n--- Dane Pracowników z Pętli for (indeksy od 1 do 2) ---");
        for (int i = 1; i <= 2; i++) {
            Pracownik p = wol[i]; // Pobieramy pracownika

            System.out.println("\nIndeks: wol[" + i + "]");
            System.out.println("Nazwa: " + p.getNazwa());
            System.out.println("Pensja: " + p.getPensja());
            System.out.println("DZad: " + p.getDZad());
        }
    }
}
class Pracownik {

    private String Nazwa;
    private double Pensja;
    private Date DZad;

    public Pracownik(String n, double p, int d, int m, int r){
        Nazwa = n;
        Pensja = p;

        // Miesiące w GregorianCalendar są liczone od 0
        GregorianCalendar k = new GregorianCalendar(r, m - 1, d);

        DZad = k.getTime();

        int dzien = k.get(GregorianCalendar.DAY_OF_MONTH);
        int miesiac = k.get(GregorianCalendar.MONTH) + 1;
        int rok = k.get(GregorianCalendar.YEAR);

        System.out.println("Data zatrudnienia: " + dzien + "-" + miesiac + "-" + rok);
    }

    public String getNazwa(){
        return Nazwa;
    }

    public double getPensja(){
        return Pensja;
    }

    public Date getDZad(){
        return DZad;
    }
}
