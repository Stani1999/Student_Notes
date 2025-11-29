import java.util.*;

public class Pracownik_Info_II {
    public static void main(String[] args) {
        Pracownik[] wol = new Pracownik[3];
        wol[0] = new Pracownik("Prezydent", 15000.0);
        wol[1] = new Pracownik(2000.0);
        wol[2] = new Pracownik();
        for (Pracownik p : wol) {
            System.out.println("Nazwa: " + p.getNazwa() + " Pensja: " + p.getPensja() + " SM: " + p.getSN());
        }
    }
}