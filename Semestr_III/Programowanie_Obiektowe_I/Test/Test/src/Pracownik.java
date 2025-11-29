import java.util.*;

class Pracownik{
    public static int ni;
    private String Nazwa;
    private double Pensja;

    // Blok statyczny (uruchamiany prze łądowaniu klasy)
    static{
        Random r = new Random();
        ni = r.nextInt(10); // losje wartość 0-10
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
}