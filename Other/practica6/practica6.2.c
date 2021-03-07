#include <stdio.h>
#define NINE 9

int main(void)
{
    int sobra, extra, orden[NINE], masvendido = 0;
    float pesofrutas[NINE], pesototal[NINE];
    //Leer ficheros
    FILE *entrada = NULL;
    FILE *salida = NULL;
    entrada = fopen("frutas.txt", "r");
    for (int i = 0; i < NINE; i++)
    {
        fscanf(entrada, "%i%f", &orden[i], &pesofrutas[i]);
    }
    fclose(entrada);
    //Saber mas vendido
    for(int i = 1; i < NINE; i++)
    {
        if (pesofrutas[i] > pesofrutas[masvendido])
        {
            masvendido = i;
        }
    }
    entrada = fopen("kilos.txt", "r");
    for (int i = 0; i < NINE; i++)
    {
        //kilos.txt esta ordenado
        fscanf(entrada, "%i%f", &sobra, &pesototal[i]);
    }
    fclose(entrada);
    //Hacer el calculo
    for (int i = 0; i < NINE; i++)
    {
        pesototal[orden[i] - 1] += pesofrutas[i];
    }
    //Imprimir
    salida = fopen("kilos.txt", "w");
    for (int i = 0; i < NINE; i++)
    {
        fprintf(salida, "%i %.2f\n", i + 1, pesototal[i]);
    }
    fclose(salida);
    printf("El mas vendido ha sido el %i\n", orden[masvendido]);
    return 0;
}