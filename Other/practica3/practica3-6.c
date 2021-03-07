#include <stdio.h>

int main(void)
{
    int dia, mes, ano;
    char bisiesto = 'n', correcto = 'y';
    FILE *entrada = NULL;
    entrada = fopen("fecha.txt", "r");
    if (entrada == NULL)
    {
        return 1;
        printf("error fopen\n");
    }
    fscanf(entrada, "%i%i%i", &dia, &mes, &ano);
    fclose(entrada);
    //Comprobar dia, mes ano
    if (dia < 0 || dia > 31)
    {
        correcto = 'n';
    }
    if (mes < 1 || mes > 12)
    {
        correcto = 'n';
    }
    if (ano < 1)
    {
        correcto = 'n';
    }
    //Comprobar mes
    if (mes == 4 || mes == 6 || mes == 9 || mes == 11)
    {
        if (dia > 30)
        {
            correcto = 'n';
        }
    }
    else if (mes == 2)
    {
        //Ano bisiesto?
        if (ano % 4 == 0 && ano % 100 != 0)
        {
            bisiesto = 'y';
        }
        else if (ano % 400 == 0)
        {
            bisiesto = 'y';
        }
        if (bisiesto == 'n')
        {
            if (dia > 28)
            {
                correcto = 'n';
            }
        }
        else if (bisiesto == 'y')
        {
            if (dia > 29)
            {
                correcto = 'n';
            }
        }
    }
    if (correcto == 'y')
    {
        printf("Correcto\n");
    }
    else
    {
        printf("Incorrecto\n");
    }
    return 0;
}