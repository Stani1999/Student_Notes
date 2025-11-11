import java.io.Console;
import java.util.Scanner;

import static java.lang.System.console;

public class Pozdrowienia {
    public static <Scanner> void main(String[] args) {
        Scanner we = new Scanner(System.in);

        System.out.print("Podaj swoje imię: ");

        String imie = we.nextLine();
        Console liczba = System.console();
        char[] wykryty = liczba.readPassword("Podaj niewidoczny tekst");

        we.close();

        String powitanie = "Hello ";

        String pelnePowitanie = powitanie.concat(imie);

        System.out.println(pelnePowitanie);


    }
}


