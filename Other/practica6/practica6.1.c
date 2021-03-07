#include <stdio.h>
#define NINE 10

int main(void)
{
    int sobra, extra, orden[NINE];
    float pesofrutas[NINE], pesototal[NINE];
    //Leer ficheros
    FILE *entrada2 = NULL;
    FILE *entrada = NULL;
    FILE *salida = NULL;
    entrada = fopen("frutas.txt", "r");
    for (int i = 0; i < NINE; i++)
    {
        fscanf(entrada, "%i%f", &orden[i], &pesofrutas[i]);
    }
    fclose(entrada);
    entrada2 = fopen("kilos.txt", "r");
    for (int i = 0; i < NINE; i++)
    {
        //kilos.txt esta ordenado
        fscanf(entrada, "%i%f", &sobra, &pesototal[i]);
    }
    fclose(entrada2);
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
    return 0;
}