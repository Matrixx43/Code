#include <stdio.h>
#define NUMERO 10

int factorial(int);
int main(void)
{
    int n, suma = 0;
    do
    {
        printf("Numero: ");
        scanf("%i", &n);
    }
    while (n < 1 || n > NUMERO);
    for (int i = 0; i < n; i++)
    {
        suma += factorial(n - i);
    }
    printf("%i\n", suma);
}

int factorial(int a)
{
    if (a == 1)
    {
        return 1;
    }
    else
    {
        return (a * factorial(a - 1));
    }
}