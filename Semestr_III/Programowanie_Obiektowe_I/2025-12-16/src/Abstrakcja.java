public class Abstrakcja {
    public static void main(String[] args) {
        Intruz[] i = new Intruz[2];
        i[0] = new Pracownik("JK", 2000, 1, 1, 2001);
        i[1] = new Student("Maciej", "Promptolodzia");
            for (Intruz t: i){
                System.out.println(t.getNazwa() + " " + t.getOpis());
            }
    }
}