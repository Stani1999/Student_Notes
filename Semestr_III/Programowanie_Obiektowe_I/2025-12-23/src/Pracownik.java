import java.util.Random;

public class Pracownik implements Comparable<Pracownik>{
    // --Pola--
    //Pole statyczne
    public static int ni;

    static{
        Random r = new Random();
        ni = r.nextInt(10);
    }
    // Pola instancji
    private int sn;
    private String nazwa = "";
    private double pensja;

    // Inicjalizacja instancji
    {
        sn = ni;
        ni++;
    }
    // --Konstruktoru--

    // Główny
    public Pracownik(String n, double p){
        this.nazwa = n;
        this.pensja = p;
    }

    // Drugi do "przeciąrzenia"
    public Pracownik(double p){
        this("Pracownik #" + ni, p);
    }

    // Konstruktor bezargumentowy
    public Pracownik(){
    }

    // --Metody--
    public String getNazwa(){
        return nazwa;
    }
    public int getSN(){
        return sn;
    }
    public double getPensja() {
        return pensja;
    }
    public int compareTo (Pracownik p){
        return Double.compare(pensja, p.pensja);
    }
}