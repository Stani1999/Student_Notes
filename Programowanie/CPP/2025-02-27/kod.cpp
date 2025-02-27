#include <iostream>

using namespace std;

void showBoard(char board[3][3]) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << board[i][j];
            if (j < 2) cout << " | ";
        }
        cout << endl;
        if (i < 2) cout << "---------" << endl;
    }
}

bool isFinished(char board[3][3], char &winner) {
    // Sprawdzanie wierszy i kolumn
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
            winner = board[i][0];
            return true;
        }
        if (board[0][i] != ' ' && board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
            winner = board[0][i];
            return true;
        }
    }

    // Sprawdzanie przekątnych
    if (board[0][0] != ' ' && board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
        winner = board[0][0];
        return true;
    }
    if (board[0][2] != ' ' && board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
        winner = board[0][2];
        return true;
    }

    // Sprawdzanie remisu (czy plansza jest pełna)
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == ' ') {
                return false; // Są jeszcze wolne pola
            }
        }
    }

    winner = 'T'; // Remis (Tie)
    return true;
}

bool setPoint(char board[3][3], unsigned int x, unsigned int y, char player) {
    if (x >= 3 || y >= 3 || board[x][y] != ' ') {
        return false;
    }
    board[x][y] = player;
    return true;
}

void clearBoard(char board[3][3]) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            board[i][j] = ' ';
        }
    }
}

int main() {
    char board[3][3];
    clearBoard(board);
    
    char winner = ' ';
    char playerMove = 'O';
    
    while (!isFinished(board, winner)) {
        showBoard(board);
        
        unsigned int x, y;
        cout << "Gracz " << playerMove << ", podaj wspolrzedne (wiersz i kolumna): ";
        cin >> x >> y;
        
        if (!setPoint(board, x, y, playerMove)) {
            cout << "Nieprawidłowy ruch! Spróbuj ponownie." << endl;
            continue;
        }

        playerMove = (playerMove == 'X') ? 'O' : 'X';
    }
    
    showBoard(board);
    
    if (winner == 'T') {
        cout << "Remis!" << endl;
    } else {
        cout << "Gracz " << winner << " wygrywa!" << endl;
    }

    return 0;
}
