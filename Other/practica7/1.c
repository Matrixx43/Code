#include <stdio.h>

int factorial(int);
int main(void)
{
    int n;
    printf("Numero: ");
    scanf("%i", &n);
    printf("%i\n", factorial(n));
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