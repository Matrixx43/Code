#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int dia, mes, ano, p1, p2, p3, p4;
    printf("Introduce dia mes año: ");
    scanf("%i%i%i", &dia, &mes, &ano);
    p1 = ((dia - dia%10) / 10 + (dia%10)) % 10;
    p2 = ((mes - mes%10) / 10 + (mes%10)) % 10;
    p3 = ((ano % 10) + (ano - ano % 1000) / 1000) % 10;
    p4 = ((ano % 100 - ano % 10) / 10 + (ano % 1000 - ano % 100) / 100) % 10;
    printf("\nPIN: %i%i%i%i\n", p1, p2, p3, p4);
}