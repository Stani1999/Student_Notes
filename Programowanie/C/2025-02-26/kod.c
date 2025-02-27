#include <stdio.h>

int main() {
    int i, j;
    printf("Podaj wartość n: ");
    int n;
    int padding = 1;
    scanf("%d", &n);
    int zakres = n*n;
    while (zakres != 0) {
        zakres /= 10;
        padding++;
        }
    for (i = 1; i <= n; i++) { 
        for (j = 1; j <= n; j++) { 
            printf("%*d ",padding, i * j); 
        }
        printf("\n");
    }

    return 0;
}