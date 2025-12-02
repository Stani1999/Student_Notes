import java.io.IOException;
import java.nio.file.*;
import java.util.Scanner;

public class Magazyn {
    public static void main(String[] args){

        // Tworzenie instancji kalsy Towar
        Towar[] item = new Towar[3];
        item[0] =  new Towar("Banan Prutas", 2.99,20,2,2022);
        item[1] =  new Towar("Globuz Polzgi", 102.23);
        item[2] =  new Towar();

        // Łańcuch na raport
        String raport_dane = "";


        // Wypisz wszystkie elementy (item) z tablicy towar "typu (kalsy) Towar"
        for (Towar t: item){ // Przykład pętli for each
            raport_dane += t.getDaneTowaru()+"\n"; // sumowanie raportów
        }

        // Alternatywna iteracja w zakresie od do
        int odNum = 1, doNum = 3;
        System.out.println("Zwykła pętla for:\n");
        for(int i=--odNum; i<doNum; i++) {
            Towar t = item[i];
            System.out.println(t.getDaneTowaru()+"\n");
        }
        Scanner scan = new Scanner(System.in);

        System.out.print("Podaj nazwę poprzedniego lub pomiń (enter) ");
        String prevRaportName = scan.nextLine();
        if (prevRaportName != "") {
            Path pervSource = Paths.get(prevRaportName);
            try {
                String prevRaport = Files.readString(pervSource);
                System.out.print(prevRaport);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        else System.out.println("Pominięto poprzedni raport.");

        System.out.print("Podaj nazwę do raportu: ");
        String raportName = scan.nextLine();
        
        Path sourcePath = Paths.get(raportName);
        try {
            Files.writeString(sourcePath, raport_dane);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        Path rPath = sourcePath.toAbsolutePath();
        System.out.println(sourcePath);
        System.out.println("Plik zostanie zapisany do: " + rPath);
    }
}