public class Kierownik extends Pracownik{
    private  double dodatek;
    public Kierownik(String n, double p, int r, int m, int d) {
        super(n, p, r, m, d);
        dodatek = 0;
    }
    public double getPensja(){
        double p = super.getPensja();
        return p + dodatek;
    }
    public void setDodatek(double d){
        dodatek = d;
    }
}

