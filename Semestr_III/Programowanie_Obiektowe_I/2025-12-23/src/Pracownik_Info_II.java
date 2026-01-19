import java.util.Arrays;

public class Pracownik_Info_II {
    public static void main(String[] args) {
        Pracownik[] wol = new Pracownik[3];
        wol[0] = new Pracownik("Jan", 2000.0);
        wol[1] = new Pracownik("John", 2022);
        wol[2] = new Pracownik("Jeży", 2001);


        for (Pracownik p : wol) {
            System.out.println("Nazwa: " + p.getNazwa() + " Pensja: " + String.format("%.2f", p.getPensja()));
        }
        Arrays.sort(wol);
        System.out.println();
        for (Pracownik p : wol) {
            System.out.println("Nazwa: " + p.getNazwa() + " Pensja: " + String.format("%.2f", p.getPensja()));
        }
    }
}