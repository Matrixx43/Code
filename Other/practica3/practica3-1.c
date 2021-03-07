#include <stdio.h>

int main(void)
{
    float base, altura;
    int tipo;
    /*Conseguir datos*/
    printf("Tipo de figura (1-rectángulo, 2-triángulo): ");
    scanf("%d", &tipo);
    printf("Base de la figura: ");
    scanf("%f", &base);
    printf("Altura de la figura: ");
    scanf("%f", &altura);
    if (tipo == 1)
    {
        printf("Area de la figura: %.2f\n", base * altura);
    }
    else if (tipo == 2)
    {
        printf("Area de la figura: %.2f\n", base * altura / 2);
    }
}