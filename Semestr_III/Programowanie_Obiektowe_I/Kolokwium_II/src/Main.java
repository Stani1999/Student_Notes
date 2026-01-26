public static void main(String[] args) {
    Student s1 = new Student("Aro", 3, 8, 1998, 1500.0);

    try {
        Student s2 = s1.clone();

        s2.setRok(1999);
        s2.setStypendium(2000.0);

        System.out.println("Oryginał: " + s1.getDzien() + ", " + s1.getStypendium());

        System.out.println("Kopia: " + s2.getDzien() + ", " + s2.getStypendium());

    } catch (Exception e) {
        throw new RuntimeException("Coś poszło nie tak z klonowaniem", e);
    }
}
