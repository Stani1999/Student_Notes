public class Pracownik_Info {
    public static void main(String[] args) {
        Pracownik[] wol = new Pracownik[3];
        wol[0] = new Pracownik("Bogdan Boner", 1000.0, 10, 20, 2025);
        wol[1] = new Pracownik("", 999.0, 10, 20, 2025);
        wol[2] = new Pracownik("Prezydent", 15000.0, 10, 20, 2025);
        for (Pracownik p : wol) {
            System.out.println(
                    "\nNazwa: " + p.getNazwa() +
                    " \nPensja: " + p.getPensja() +
                    " \nSM: " + p.getSN() +
                    " \nZatrudniony: " + p.getDZad());
        }
    }
}