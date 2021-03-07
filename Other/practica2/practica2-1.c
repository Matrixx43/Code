#include <stdio.h>

/*Declaracion de constantes*/
#define PI 3.14159

int main(void)
{
    float largo, radio, circunf;
    printf("Introduce la longitud de la manguera y el radio: ");
    scanf("%f%f", &largo, &radio);
    circunf = 2 * PI * radio;
    printf("Vueltas:%1i Restante: %.2f\n", largo / circunf, largo - (circunf * (largo / circunf)));
    return 0;
}