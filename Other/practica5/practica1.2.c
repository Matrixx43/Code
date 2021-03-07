#include <stdio.h>

int main(void)
{
    int a, b, sum = 0;
    do
    {
        printf("Limite inferior: ");
        scanf("%i", &a);
        printf("Limite superior: ");
        scanf("%i", &b);
    }
    while (a >= b);
    while(a <= b)
    {
        sum += a;
        a++;
    }
    FILE *ptr = NULL;
    ptr = fopen("suma.txt", "w");
    if (ptr == NULL)
    {
        return 1;
    }
    fprintf(ptr, "%i", sum);
    fclose(ptr);
    return 0;
}