#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        printf("Numero: ");
        scanf("%i", &n);
    }
    while (n < 0);
    for (int i = 0; i < n; i += 7)
    {
        printf("%i ", i);
    }
    printf("\n");
    return 0;
}