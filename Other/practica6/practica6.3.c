#include <stdio.h>
#define NUM_JUGADORES 10
int main(void)
{
    int puntos[NUM_JUGADORES + 1], rebotes[NUM_JUGADORES + 1], tapones[NUM_JUGADORES + 1], partidosjugados[NUM_JUGADORES + 1];
    int jugador, punto, rebote, tapon, mejorjugador = 1;
    for (int i = 0; i < 11; i++)
    {
        puntos[i] = 0;
        rebotes [i] = 0;
        tapones [i] = 0;
        partidosjugados[i] = 0;
    }
    FILE *entrada = NULL;
    entrada = fopen("jugadores.txt", "r");
    if (entrada == NULL)
    {
        return 1;
    }
    while (fscanf(entrada, "%i%i%i%i", &jugador, &punto, &rebote, &tapon) != EOF)
    {
        puntos[jugador] += punto;
        rebotes[jugador] += rebote;
        tapones[jugador] += tapon;
        partidosjugados[jugador]++;
    }
    printf("Jugador 10 tiene %i puntos %i rebotes %i tapones\n", puntos[10], rebotes[10], tapones[10]);
    for (int i = 1; i <= NUM_JUGADORES; i++)
    {
        printf("Valoracion jugador %i: %.2f\n", i, (float)puntos[i] + (float)(1.5 * rebotes[i]) + (float)(2 * tapones[i]));
    }
    for(int i = 2; i < NUM_JUGADORES + 1; i++)
    {
        if(puntos[mejorjugador] < puntos[i])
        {
            mejorjugador = i;
        }
    }
    printf("juagodrmax es %i\n", mejorjugador);
}