#include <stdio.h>

int main(void)
{
    float base, altura, area;
    int tipo;
    FILE *entrada = NULL;
    FILE *salida = NULL;
    /*Conseguir datos*/
    entrada = fopen("datos.txt", "r");
    if (entrada == NULL)
    {
        return 1;
        printf("Error fopen\n");
    }
    fscanf(entrada, "%i", &tipo);
    fscanf(entrada, "%f", &base);
    fscanf(entrada, "%f", &altura);
    fclose(entrada);
    //Procesar datos
    if (tipo == 1)
    {
        area =  base * altura;
    }
    else if (tipo == 2)
    {
        area = base * altura / 2;
    }
    //Salida
    salida = fopen("area.txt", "w");
    if (salida == NULL)
    {
        return 1;
        printf("Error fopen\n");
    }
    fprintf(salida, "%.2f\n", area);
    fclose(salida);
    return 0;

}