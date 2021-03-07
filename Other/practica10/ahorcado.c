#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAXPAL 31
#define NPALABRAS 26457
#define MAXFALLOS 60

//Prototipos de funciones
int numpal();
int seleccionar_palabra(char []);
void inicializa_palabra(char*, int);
int busca_letra(char pal_oculta[], char *palabra, char letra, int length);
char menu(int fallos, char *palabra);

int main()
{
  char *palabra, pal_oculta[MAXPAL];

  /* leemos de fichero la palabra oculta -> función selecciona_palabra */
  int seleccion = seleccionar_palabra(pal_oculta);

  /* si hay error en la lectura -> finalizar el programa */
  if (seleccion != 0)
  {
    printf("Error abriendo ficehro\n");
    return seleccion;
  }

  /* calculamos el tamaño de la palabra oculta */
  int length = strlen(pal_oculta);

  /* creamos el vector palabra dinámicamente -> función malloc */
  palabra = malloc((length + 1) * sizeof(char));


  /* si no se puede crear -> finalizar programa*/
  if (palabra == NULL)
  {
    printf("Error abriendo palabra\n");
    return 1;
  }

  /* inicializamos la palabra a una cadena de subrayados '_' -> función inicializa_palabra */
  inicializa_palabra(palabra, length);

  /* mientras el número de aciertos sea menor que el tamaño
     de la palabra oculta y el número de fallos menor que el
     máximo de fallos -> el juego continúa */
  int aciertos = 0, fallos = 0;

  while (aciertos < length && fallos < MAXFALLOS)
  {
    char letra = menu(fallos, palabra);

    /* se busca la letra en la palabra oculta -> invocar a la función busca_letra */
    int buscar = busca_letra(pal_oculta, palabra, letra, length);

    /* Según el resultado de la búsqueda indicar si se ha acertado, se ha fallado
       o se ha introducido una letra ya adivinada -> Actualizar contadores de fallos y aciertos */
    if (buscar == -1)
    {
      printf("Ya has encontrado esta palabra antes\n");
    }
    else if (buscar == 0)
    {
      printf("Ooops, no se ha encontrado coincidencia\n");
      fallos++;
      //Comprobar si se ha alcanzado maximo de fallos
      if (fallos == MAXFALLOS)
      {
        printf("Has alcanzado los %i fallos maximos. Mas suerte la proxima!\n", MAXFALLOS);
        printf("La palabra buscada era %s\n", pal_oculta);
      }
    }
    else //Se ha encontrado coincidencia
    {
      printf("Has acertado %i letras!\n", buscar);
      aciertos += buscar;
      if (aciertos == length)
      {
        printf("Enhorabuena, has acertado la palabra %s!!!\n", palabra);
      }
    }

  }

/* Indicar el resultado del juego -> Se ha ganado o perdido */
/* Si se pierde mostrar la palabra oculta */
/* Si se gana mostrar el número de fallos realizados */

return 0;
}

/* Función numpal */
int numpal()
{

  srand(time(NULL));

  return (rand()%NPALABRAS);

}

/* Escribe la función selecciona_palabra */
int seleccionar_palabra(char pal_oculta[])
{
  int n = numpal() - 1;
  FILE *entrada = fopen("palabras.txt", "r");
  if (entrada == NULL)
  {
    return -1;
  }
  char string[MAXPAL];
  for (int i = 0; i < n; i++)
  {
    fscanf(entrada, "%s", string);
  }
  fscanf(entrada, "%s", pal_oculta);
  fclose(entrada);
  return 0;

}

/* Escribe la función busca_letra */
int busca_letra(char pal_oculta[], char *palabra, char letra, int length)
{
  int coincidencias = 0;
  //Comprobar si ya habia sido adivinada
  for (int i = 0; i < length; i++)
  {
    if (letra == palabra[i])
    {
      coincidencias++;
    }
  }
  if (coincidencias != 0)
  {
    return -1;
  }
  //Comprobar si letra esta en palabra_oculta
  coincidencias = 0;
  for (int i = 0; i < length; i++)
  {
    if (letra == pal_oculta[i])
    {
      coincidencias++;
      palabra[i] = letra;
    }
  }
  return coincidencias;
}


/* Escribe la función inicializa_palabra */
void inicializa_palabra(char* palabra, int length)
{
  char string[length + 1];
  for (int i = 0; i < length; i++)
  {
    string[i] = '_';
  }
  string[length] = '\0';
  strcpy(palabra, string);
}

char menu(int fallos, char *palabra)
{
  /* se muestra el número de fallos que se lleva acumulados */
    /* y los que todavía se pueden realizar */
    printf("============================================\n");
    printf("Llevas %i fallos, luego tienes %i intentos mas\n", fallos, MAXFALLOS - fallos);
    printf("============================================\n");

    /* Se muestra el vector palabra */
    printf("====  %s  ====\n", palabra);

    /* se lee la letra con la que se juega por teclado */
    char letra;
    printf("Introduce la letra: ");
    scanf(" %c", &letra);
    return letra;
}