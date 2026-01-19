import java.util.Scanner;

public class Choinka {

    public static final String RESET = "\u001B[0m";
    public static final String ZIELONY = "\u001B[32m";
    public static final String ZOLTY = "\u001B[33m"; // Użyjemy dla pnia i gwiazdy
    public static final String CZERWONY = "\u001B[31m";

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Podaj jak wysoka choinka wariacie? ");
        int ileMaszCM = input.nextInt();

        if (ileMaszCM > 10) {
            System.out.println("Te odczyty nie mieszczą się w skali ucinam do 10");
            ileMaszCM = 10;
        }
        if (ileMaszCM < 2) {
            System.out.println("Takich małych nie sprzedajemy masz 3");
            ileMaszCM = 3;
        }
        for (int i = 0; i < ileMaszCM; i++) {
            for (int j = 0; j < ileMaszCM - i - 1; j++) {
                System.out.print(" ");
            }
            System.out.print(ZIELONY);

            for (int k = 0; k < i; k++) {
                System.out.print("*");
            }

            if (i == 0) {
                System.out.print(ZOLTY + "*" + ZIELONY);
            } else {
                System.out.print("|");
            }

            for (int k = 0; k < i; k++) {
                System.out.print("*");
            }
            System.out.println(RESET);
        }
        for (int i = 0; i < ileMaszCM - 2; i++) {
            System.out.print(" ");
        }
        System.out.println(ZOLTY + "| |" + RESET);
    }
}