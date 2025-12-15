import java.util.Scanner;
import java.nio.file.*;
import java.io.IOException;

public class IO_Save {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Path sourcePath = Paths.get("IO_plik.txt");
        Path rsicezka = sourcePath.toAbsolutePath();
        System.out.println(sourcePath);
        System.out.println(rsicezka);

        try {

            String content = Files.readString(sourcePath);
            System.out.println(content);
            System.out.print("Podaj nową nazwę pliku (np. nowy_plik.txt): ");
            String newFileName = input.nextLine(); // Po znaku nowej lini przypisz do zmiennej

            Path newPath = Paths.get(newFileName);
            Files.writeString(newPath, content);
            System.out.println("Plik został zapisany jako: " + newFileName);

        } catch (IOException e) {
            System.err.println("Błąd operacji na pliku: " + e.getMessage());
        } finally {
            input.close();
        }
    }
}