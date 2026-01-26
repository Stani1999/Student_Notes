public class Panstwo {
    public static void main(String[] args) {
        Stolica polska = new Stolica("Warszawa");
        int d1 = polska.getTablica(0);
        int d2 = polska.getTablica(1);
        int d3 = polska.getTablica(2);
        int d4 = polska.getTablica(3);
        int d5 = polska.getTablica(4);

        int liczSrednia = d1 +d2+ d3+ d4+ d5;
        int srednia = liczSrednia/5;

        System.out.println("Nazwa: " + polska.getNazwa()+
                "\nDzielnica 1: " + d1 +
                "\nDzielnica 2: " + d2 +
                "\nDzielnica 3: " + d3 +
                "\nDzielnica 4: " + d4 +
                "\nDzielnica 5: " + d5
                +"\nŚrednia: " + srednia );
    }
}
