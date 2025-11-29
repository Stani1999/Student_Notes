public class Pracownik_info_II {

    public static void main(String[] args) {

        Pracownik[] wol = new Pracownik[3];
        wol[0] = new Pracownik("Prezydent", 15000.0);
        wol[1] = new Pracownik(2000.0);
        wol[2] = new Pracownik();

        // Pętla for do wyświetlenia pracowników od indeksu 1 do 2
        System.out.println("\n--- Dane Pracowników ---");
        for (int i = 1; i <= 2; i++) {
            Pracownik p = wol[i]; // Pobieramy pracownika

            System.out.println("\nIndeks: wol[" + i + "]");
            System.out.println("Nazwa: " + p.getNazwa());
            System.out.println("Pensja: " + p.getPensja());
            System.out.println("SN: " + p.getSN());
        }
    }
}