// Własna klasa dodana do kodu dla testu subClass
public class Kierownik extends Pracownik{
    private String stopień;

    public Kierownik(String stopien, String nazwa, double pensja){
        this.stopień = stopien;
        setNazwa(nazwa);
        setPensja(pensja);
    }

    public String getStopień(){
        return stopień;
    }

}