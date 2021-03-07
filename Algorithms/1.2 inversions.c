#include <stdio.h>

int mergesort(int[], int, int);
int merge(int[], int, int, int);
int main(void)
{
    //Abrir fichero
    int n = 0;
    FILE *entrada = fopen("pset2.txt", "r");
    if (entrada == NULL)
    {
        return 1;
    }
    int sobra;
    while (fscanf(entrada, "%i", &sobra) != EOF)
    {
        n++;
    }
    fclose(entrada);
    printf("Hay %i elementos\n", n);
    int lista[n];
    entrada = fopen("pset2.txt", "r");
    if (entrada == NULL)
    {
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        fscanf(entrada, "%i", &lista[i]);
    }
    fclose(entrada);
    int l = 0, m, r = n - 1;
    m = (l + r) / 2;
    long inv = 0;
    int a = mergesort(lista, l, m);
    inv += a;
    a = mergesort(lista, m + 1, r);
    inv += a;
    a = merge(lista, l, m, r);
    printf("a = %i\n", a);
    inv += a;
    if (inv < 0 )
        printf("error3");
    //Imprimir resultados
    printf("Inversions: %li\n", inv);
    FILE *salida = fopen("salida.txt", "w");
    if (salida == NULL)
        return 1;
    for (int i = 0; i < n; i++)
        fprintf(salida, "%i\n", lista[i]);
    return 0;
}

int mergesort(int arr[], int l, int r)
{
    int inv = 0;
    int m = (l + r) / 2;
    if (m == r && m == l)
    {
        return 0;
    }
    int a = mergesort(arr, l, m);
    inv += a;
    a = mergesort(arr, m + 1, r);
    inv += a;
    a = merge(arr, l, m, r);
    inv += a;
    return inv;
}

int merge(int arr[], int l, int m, int r)
{
    int length = r - l + 1, pointer = 0, pr = m + 1, pl = l; //pr = pointer right
    int extrarr[length];
    int inv = 0;
    while (pl <= m && pr <= r)
    {
        if (arr[pl] <= arr[pr])
        {
            extrarr[pointer] = arr[pl];
            pl++;
            pointer++;
        }
        else //arr[pr] < arr[pl]
        {
            extrarr[pointer] = arr[pr];
            pr++;
            pointer++;
            inv += m - pl + 1;
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
    return inv;
}