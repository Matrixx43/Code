#include <stdio.h>

void mergesort(int[], int, int);
void merge(int[], int, int, int);
int main(void)
{
    //Abrir fichero y contar numero elementos
    int n = 0, extra;
    FILE *entrada = NULL;
    entrada = fopen("ConjuntoA.txt", "r");
    if (entrada == NULL)
    {
        return 1;
    }
    while (fscanf(entrada, "%i", &extra) != EOF)
    {
        n++;
    }
    fclose(entrada);
    //Reabrir fichero
    int lista[n];
    entrada = fopen("ConjuntoA.txt", "r");
    if (entrada == NULL)
    {
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        fscanf(entrada, "%i", &lista[i]);
    }
    fclose(entrada);
    int l = 0, m, r = n;
    m = (l + r) / 2;
    mergesort(lista, l, m);
    mergesort(lista, m + 1, r);
    merge(lista, l, m, r);
    //Imprimir resultados
    FILE *salida = NULL;
    salida = fopen("ordenado.txt", "w");
    if (salida == NULL)
    {
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        fprintf(salida, "%i\n", lista[i]);
    }
    fclose(salida);
    return 0;
}

void mergesort(int arr[], int l, int r)
{
    int m = (l + r) / 2;
    if (m == r && m == l)
    {
        return;
    }
    mergesort(arr, l, m);
    mergesort(arr, m + 1, r);
    merge(arr, l, m, r);
}

void merge(int arr[], int l, int m, int r)
{
    int length = r - l + 1, pointer = 0, pr = m + 1, pl = l; //pr = pointer right
    int extrarr[length];
    while (pl <= m && pr <= r)
    {
        if (arr[pl] <= arr[pr])
        {
            extrarr[pointer] = arr[pl];
            pl++;
            pointer++;
        }
        else //arr[pr < arr[pl
        {
            extrarr[pointer] = arr[pr];
            pr++;
            pointer++;
        }
    }
    //Copy remaining values
    {
        if (pl <= m)
        {
            int a = m - pl + 1;
            for (int i = 0; i < a; i++)
            {
                extrarr[pointer] = arr[pl];
                pl++;
                pointer++;
            }
        }
        else if (pr <= r)
        {
            int a = r - pr + 1;
            for (int i = 0; i < a; i++)
            {
                extrarr[pointer] = arr[pr];
                pr++;
                pointer++;
            }
        }
    }
    //Copy values back
    for (int i = 0 ; i< length; i++)
    {
        arr[l + i] = extrarr[i];
    }
}