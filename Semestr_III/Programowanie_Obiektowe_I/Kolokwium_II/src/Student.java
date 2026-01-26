public class Student implements Cloneable{
    private String nazwa;
    private int dzien;
    private int miesionc;
    private int rok ;
    private double stypendium;

    public Student(String nazwa, int dzien, int miesionc, int rok, double stypendium) {
        this.nazwa = nazwa;
        this.dzien = dzien;
        this.miesionc = miesionc;
        this.rok = rok;
        this.stypendium = stypendium;
    }

    public Student(String nazwa, int dzien, int miesionc, int rok, double stypendium, int premia) {
        this.nazwa = nazwa;
        this.dzien = dzien;
        this.miesionc = miesionc;
        this.rok = rok;
        this.stypendium = stypendium * premia /100;
    }

    public String getNazwa() {
        return nazwa;
    }

    public int getDzien() {
        return dzien;
    }

    public int getMiesionc() {
        return miesionc;
    }

    public int getRok() {
        return rok;
    }

    public double getStypendium() {
        return stypendium;
    }

    public void setDzien(int dzien) {
        this.dzien = dzien;
    }

    public void setMiesionc(int miesionc) {
        this.miesionc = miesionc;
    }

    public void setRok(int rok) {
        this.rok = rok;
    }

    public void setStypendium(double stypendium) {
        this.stypendium = stypendium;
    }

    @Override
    public Student clone() {
        try {
            return (Student) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException("Coś poszło nie tak z klonowaniem", e);
        }
    }
}