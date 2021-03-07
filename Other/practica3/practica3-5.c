#include <stdio.h>

int main(void)
{
    int edad, anos, accidentes, precio = 300;
    char denegado = 'n';
    FILE *entrada = NULL;
    entrada = fopen("seguro.txt", "r");
    if (entrada == NULL)
    {
        return 1;
    }
    fscanf(entrada, "%i%i%i", &edad, &anos, &accidentes);
    fclose(entrada);
    //Condicion b
    if (anos < 3)
    {
        precio += 200;
    }
    else if (anos < 5)
    {
        precio += 150;
    }
    else if (anos < 10)
    {
        precio += 100;
    }
    //Condicion c
    if (edad < 25)
    {
        precio += 200;
    }
    //Condicion d
    if (accidentes == 1)
    {
        precio += 50;
    }
    else if (accidentes == 2)
    {
        precio += 125;
    }
    else if (accidentes == 3)
    {
        precio += 225;
    }
    else if (accidentes == 4)
    {
        precio += 375;
    }
    else if (accidentes == 5)
    {
        precio += 575;
    }
    else if (accidentes >= 6)
    {
        denegado = 'y';
    }
    //Resultados
    if (denegado == 'y')
    {
        printf("No se asegura\n");
    }
    else
    {
        printf("Precio: %i\n", precio);
    }
    return 0;
}