#include <stdio.h>

int main(void)
{
    int num;
    printf("Introduce un numero (0...9): ");
    scanf("%i", &num);
    printf("Los tres numeros siguientes a %i son %i %i %i\n", num, (num + 1) % 10, (num + 2) % 10, (num + 3) % 10);
    return 0;
}