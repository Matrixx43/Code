#include <stdio.h>
#define PI 3.1415926535

int main(void)
{
    float nh, ph, r;
    printf("Introduce el numero de horas trabajado, seguido del salario por hora, seguido del porcentaje de retencion: ");
    scanf("%f%f%f", &nh, &ph, &r);
    printf("\n****************\n");
    printf("El salario bruto es %.2f\n", nh * ph);
    printf("El salario neto es %.2f\n", (nh * ph) - (r * (nh * ph) / 100));
}