#include <stdio.h>
#define TEN 10

int main(void)
{
    int terminaciones[TEN], i, cursormas = 0, cursormenos = 0;
    FILE *ptr = NULL;
    ptr = fopen("lotto.txt", "r");
    if(ptr == NULL)
    {
        return 1;
    }
    for(i = 0; i < TEN; i++)
    {
        fscanf(ptr, "%i", &terminaciones[i]);
        fscanf(ptr, "%i", &terminaciones[i]);
    }
    fclose(ptr);
    for(i = 0; i < TEN; i++)
    {
        if(terminaciones[i] > terminaciones[cursormas])
        {
            cursormas = i;
        }
        if(terminaciones[i] < terminaciones[cursormenos])
        {
            cursormenos = i;
        }
    }
    printf("La terminacion mas repetida es %i (%i veces)\n", cursormas, terminaciones[cursormas]);
    printf("La terminacion menos repetida es %i (%i veces)\n", cursormenos, terminaciones[cursormenos]);
    return 0;
}