#include <stdio.h>
#define NUMERO 5

void tabla(int);
int main(void)
{
    for (int i = 1; i <= NUMERO; i++)
    {
        printf("===========\n");
        printf("TABLA DEL %i\n", i);
        printf("===========\n");
        tabla(i);
        printf("\n");
    }
}

void tabla(int n)
{
    for (int i = 0; i < 10; i++)
    {
        printf("%ix%i=%i\n", n, i + 1, n * (i + 1));
    }
}