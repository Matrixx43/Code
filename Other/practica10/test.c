#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void)
{
    char *palabra = malloc(20 * sizeof(char) + 1);
    printf("string: ");
    scanf("%s", palabra);
    printf("%s\n", palabra);
    palabra[2] = 'r';
    printf("%s\n", palabra);
}