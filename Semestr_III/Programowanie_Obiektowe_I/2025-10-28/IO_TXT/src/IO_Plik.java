import java.util.Scanner;
import java.nio.file.Paths;
import java.io.IOException;

public class IO_Plik {
    public static void main(String[] args) {
        try (Scanner plik = new Scanner(Paths.get("IO_plik.txt"))) {
            if (plik.hasNextLine()) {
                System.out.println(plik.nextLine());
            } else {
                System.out.println("Plik jest pusty.");
            }
        } catch (IOException e) {
            System.err.println("Błąd odczytu pliku: " + e.getMessage());
        }
    }
}
