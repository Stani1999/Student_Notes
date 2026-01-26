import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Random;

// Klasa Towar
public class Towar {
    //pola
    private String nazwa, waluta = "PLN";
    private double cena;
    private Date dataProdukcji;
    private int id;

    // Statyczna inicjalizaja licznika do zwiększania id
    public static int globalnyLicznik;

    // Blok statyczny do randomowego licznika
    static {
        Random r= new Random();
        globalnyLicznik = r.nextInt(10);
    }
    // Blok instancji do zwiększania licznika
    {
        id = globalnyLicznik;
        globalnyLicznik++;
    }

    // Konstruktor I
    public Towar(String n, double c, int d, int m, int r){
        this.nazwa = n;
        this.cena = c;

        GregorianCalendar g = new GregorianCalendar(r, m-1, d);
        dataProdukcji = g.getTime();
    }
    // Konstruktor II
    public Towar(String n, double c){
        this(n, c,
                new GregorianCalendar().get(GregorianCalendar.DAY_OF_MONTH),
                new GregorianCalendar().get(GregorianCalendar.MONTH) + 1,
                new GregorianCalendar().get(GregorianCalendar.YEAR));
    }
    // Konstruktor III
    public Towar(){
        this("Nieznany", 0.0);
    }

    // Metody
    public String getNazwa(){
        return nazwa;
    }
    public double getCena(){
        return cena;
    }
    public Date getDataProdukcji(){
        return dataProdukcji;
    }
    public int getId(){
        return id;
    }

    public String getDaneTowaru() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        GregorianCalendar gc = new GregorianCalendar();
        gc.setTime(getDataProdukcji());
        String daneTowaru = ("Dane produktu -------" + getId() +  "-------"
                + "\nNazwa: " + getNazwa()
                + "\nCena: " + getCena() + " " +  waluta
                + "\nPrzyjęto dnia: " +  gc.toZonedDateTime().format(dtf)
                );
        return daneTowaru;
    }
}
