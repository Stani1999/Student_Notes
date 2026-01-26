import java.util.Random;

public class Stolica {
    private String nazwa;
    private int[] tablica = new int[5]; //
    Random losuj = new Random();

    public Stolica(String n) {
        this.nazwa = n;

        for (int i = 0; i < tablica.length; i++) {
            tablica[i] = losuj.nextInt(19)+1; //
        }
    }


    public String getNazwa() {
        return nazwa;
    }
    public int getTablica(int i){
        return tablica[i];
    }
}