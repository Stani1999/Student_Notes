public abstract class Intruz{
    // pola
    public abstract String getOpis();
    private String nazwa;
    // konstruktor
    public Intruz(String n){
        nazwa = n;
    }
    //
    public String getNazwa(){
        return nazwa;
    }
}
