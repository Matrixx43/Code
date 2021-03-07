#include <stdio.h>

int main(void)
{
    FILE *entrada = NULL;
    FILE *salida = NULL;
    int edad, sexo;
    float masa, altura, imc;
    //Conseguir datos
    entrada = fopen("entrada.txt", "r");
    fscanf(entrada, "%i %f %f %i", &edad, &masa, &altura, &sexo);
    fclose(entrada);
    //Calcular el imc
    imc = masa / (altura * altura);
    salida = fopen("salida.txt", "w");
    //Si es hombre
    if (sexo == 1)
    {
        if (edad < 31)
        {
            //Lower imc bound
            if (imc < 15)
            {
                fprintf(salida, "Riesgo de delgadez\n");
            }
            //Upper imc bound
            else if (imc > 21)
            {
                fprintf(salida, "Riesgo de sobrepeso\n");
            }
            else
            {
                fprintf(salida, "Peso adecuado\n");
            }
        }
        else if (edad > 50)
        {
            //Lower imc bound
            if (imc < 24)
            {
                fprintf(salida, "Riesgo de delgadez\n");
            }
            //Upper imc bound
            else if (imc > 25)
            {
                fprintf(salida, "Riesgo de sobrepeso\n");
            }
            else
            {
                fprintf(salida, "Peso adecuado\n");
            }
        }
        else
        {
            //Lower imc bound
            if (imc < 20)
            {
                fprintf(salida, "Riesgo de delgadez\n");
            }
            //Upper imc bound
            else if (imc > 23)
            {
                fprintf(salida, "Riesgo de sobrepeso\n");
            }
            else
            {
                fprintf(salida, "Peso adecuado\n");
            }
        }
    }
    //Si es mujer
    else if (sexo == 2)
    {
        if (edad < 31)
        {
            //Lower imc bound
            if (imc < 18)
            {
                fprintf(salida, "Riesgo de delgadez\n");
            }
            //Upper imc bound
            else if (imc > 23)
            {
                fprintf(salida, "Riesgo de sobrepeso\n");
            }
            else
            {
                fprintf(salida, "Peso adecuado\n");
            }
        }
        else if (edad > 50)
        {
            //Lower imc bound
            if (imc < 30)
            {
                fprintf(salida, "Riesgo de delgadez\n");
            }
            //Upper imc bound
            else if (imc > 31)
            {
                fprintf(salida, "Riesgo de sobrepeso\n");
            }
            else
            {
                fprintf(salida, "Peso adecuado\n");
            }
        }
        else
        {
            //Lower imc bound
            if (imc < 24)
            {
                fprintf(salida, "Riesgo de delgadez\n");
            }
            //Upper imc bound
            else if (imc > 29)
            {
                fprintf(salida, "Riesgo de sobrepeso\n");
            }
            else
            {
                fprintf(salida, "Peso adecuado\n");
            }
        }
    }
    fclose(salida);
    return 0;
}