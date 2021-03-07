#include <stdio.h>
#define PI 3.1415926535

int main(void)
{
    float r;
    printf("Radio: ");
    scanf("%f", &r);
    printf("La superficie es %.4f\n", 4 * PI * r * r);
    printf("El volumen es %.4f\n", 4 * PI * r * r * r / 3);
    return 0;
}