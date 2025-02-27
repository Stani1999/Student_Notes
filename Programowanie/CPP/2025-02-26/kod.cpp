#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    int opcja;

    do {
        cout << "\nMenu programu:" << endl;
        cout << "1. Wypisz ilosc argumentow programu" << endl;
        cout << "2. Wypisz wybrany argument programu" << endl;
        cout << "3. Wypisz wszystkie argumenty programu" << endl;
        cout << "4. Zakoncz program" << endl;
        cout << "Wybierz opcje: ";
        cin >> opcja;

        switch (opcja) {
            case 1:
                cout << "Ilosc argumentow programu: " << argc << endl;
                break;
            case 2: {
                int index;
                cout << "Podaj indeks argumentu: ";
                cin >> index;
                if (index >= 0 && index < argc) {
                    cout << "Argument [" << index << "]: " << argv[index] << endl;
                } else {
                    cerr << "Blad: Nieprawidlowy indeks argumentu!" << endl;
                }
                break;
            }
            case 3:
                cout << "Wszystkie argumenty programu:" << endl;
                for (int i = 0; i < argc; i++) {
                    cout << "argv[" << i << "]: " << argv[i] << endl;
                }
                break;
            case 4:
                cout << "Koniec programu." << endl;
                break;
            default:
                cerr << "Blad: Nieprawidlowa opcja!" << endl;
        }

    } while (opcja != 4); // Jeżeli opcja inna niż 4 wroc do pocztu petli

    return 0;
}