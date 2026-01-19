public class Student extends Intruz {
    private String spec; // spec = specialization

    // Konstruktor
    public Student(String n, String s){
    super (n);
    spec = s;
    }
    // Metody
    public String getOpis() {
        return "Specjalizacja " + spec;
    }
}
