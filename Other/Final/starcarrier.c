#include <stdio.h>

//Definir bool
#define true 1
#define false 0

//Definir numero de envios
#define NE 100

//Declarar funciones auxiliares
int lee_datos(int[], float[], float[]);
int menu(void);
void envios_puerto(int[], float[], float[]);
void envios_ruinosos(int[], float[], float[]);
void continentes_mas_menos_beneficio(int[], float[], float[]);
int continente_de_puerto(int);
void muestra_continente(int);
float calcular_beneficio_continente(int[], float[], float[], int);
int envios_por_continente(int[], float[], float[]);

int main(void)
{
    //Declarar vectores
    int vorigen[100];
    float vcoste[100], vingreso[100];

    //Leer el fichero y cargar datos
    int abrir = lee_datos(vorigen, vcoste, vingreso);
    if (abrir == false)
    {
        printf("Error al abrir fichero\n");
        return 1;
    }

    //Iniciar loop hasta que el usuario acabe el programa
    while(1)
    {
        int opcion = menu();
        printf("\n\n");

        //Establecer que hacer en cada caso
        if (opcion == 1)
        {
            envios_puerto(vorigen, vcoste, vingreso);
        }
        else if (opcion == 2)
        {
            envios_ruinosos(vorigen, vcoste, vingreso);
        }
        else if (opcion == 3)
        {
            continentes_mas_menos_beneficio(vorigen, vcoste, vingreso);
        }
        else if (opcion == 4)
        {
            int archivos_generados = envios_por_continente(vorigen, vcoste, vingreso);

            //Comprobar si ha sido correcto
            if (archivos_generados == false)
            {
                printf("Error al generar ficheros\n");
                return 1;
            }

            //Indicar que se ha ejecutado satisfactoriamente
            printf("Ficheros de envios por continente creados correctamente\n");
        }
        else //Si no es 1-4, debe ser 0
        {
            break;
        }

        //Imprimir espacios para facilitar lectura
        printf("\n\n\n");
    }
}

int lee_datos(int vorigen[], float vcoste[], float vingreso[])
{
    //Abrir fichero
    FILE *entrada = fopen("envios.txt", "r");
    if (entrada == NULL)
    {
        printf("Error al abrir fichero");
        return false;
    }

    //Leer los datos
    int codigo;
    float coste, ingreso;
    for (int i = 0; i < NE; i++)
    {
        fscanf(entrada, "%i%f%f", &codigo, &coste, &ingreso);
        vorigen[i] = codigo;
        vcoste[i] = coste;
        vingreso[i] = ingreso;
    }

    //Cerrar fichero
    fclose(entrada);
    return true;
}

int menu(void)
{
    int opcion;

    //Repetir hasta que el valor sea correcto
    do{
        //Hacer los printf del menu
        printf("--------------- Menu de opciones ----------------\n1. Envios desde un puerto.\n2. Envios ruinosos.\n3. Continentes con mayores y menores beneficios.\n4. Envios por continente.\n0. Finalizar.\n-------------------------------------------------\nElige una opcion (0-4): ");

        //Escanear valor
        scanf("%i", &opcion);
    }
    while (opcion > 4 || opcion < 0);

    //Devolver valor
    return opcion;
}

void envios_puerto(int vorigen[], float vcoste[], float vingreso[])
{
    //Solicitar el codigo del puerto
    int codigo;
    do
    {
        printf("Puerto de salida: ");
        scanf("%i", &codigo);
    }
    while (codigo > 4999 || codigo < 0);

    //Calcular el total de ingresos menos costes de ese puerto
    float suma = 0;
    int envios = 0;
    for (int i = 0; i < NE; i++)
    {
        if (vorigen[i] == codigo)
        {
            suma += vingreso[i];
            suma -= vcoste[i];
            envios ++;
        }
    }

    //Imprimir los resultados
    printf("Envios realizados desde el puerto %i: %i\n", codigo, envios);
    printf("Resultado de los envios del puerto %i: %.2f euros\n", codigo, suma);
}

void envios_ruinosos(int vorigen[], float vcoste[], float vingreso[])
{
    //Preparar para imprimir envios ruinosos
    printf("ENVIOS RUINOSOS:\n");

    int contador = 0;
    for (int i = 0; i < NE; i++)
    {
        if (vcoste[i] >= vingreso[i])
        {
            printf("Envio desde puerto %i. Balance de la operacion: %.2f\n", vorigen[i], vingreso[i] - vcoste[i]);
            contador ++;
        }
    }
    printf("\n\nTotal de envios ruinosos: %i\n", contador);
}

void continentes_mas_menos_beneficio(int vorigen[], float vcoste[], float vingreso[])
{
    //Calcular el beneficio de cada continente
    float beneficios[5];
    for (int i = 0; i < 5; i++)
    {
        beneficios[i] = calcular_beneficio_continente(vorigen, vcoste, vingreso, i);
    }

    //Seleccionar el mayor
    int mayor = 0;
    for (int i = 0; i < 5; i++)
    {
        if (beneficios[i] > beneficios[mayor])
        {
            mayor = i;
        }
    }

    //Seleccionar el menor
    int menor = 0;
    for (int i = 0; i < 5; i++)
    {
        if (beneficios[i] < beneficios[menor])
        {
            menor = i;
        }
    }

    //Imprimir resultados mayor
    printf("Continente de origen con mas beneficio: ");
    muestra_continente(mayor);
    printf("\n");

    //Imprimir resultados menor
    printf("Continente de origen con menos beneficio: ");
    muestra_continente(menor);
    printf("\n");
}

float calcular_beneficio_continente(int vorigen[], float vcoste[], float vingreso[], int continente) //Funcion auxiliar
{
    float beneficios = 0;
    for (int i = 0; i < NE; i++)
    {
        if(continente_de_puerto(vorigen[i]) == continente)
        {
            beneficios += vingreso[i];
            beneficios -= vcoste[i];
        }
    }
    return beneficios;
}

int continente_de_puerto(int codigo) //Funcion auxiliar
{
    if (codigo >= 0 && codigo < 1000) //Europa
    {
        return 0;
    }
    else if (codigo >= 1000 && codigo < 2000) //Asia
    {
        return 1;
    }
    else if (codigo >= 2000 && codigo < 3000) //America
    {
        return 2;
    }
    else if (codigo >= 3000 && codigo < 4000) //Africa
    {
        return 3;
    }
    else //Codigo < 5000 Oceania
    {
        return 4;
    }
}

void muestra_continente(int num_continente) //Funcion auxiliar
{
    if (num_continente == 0)
    {
        printf("Europa");
    }
    else if (num_continente == 1)
    {
        printf("Asia");
    }
    else if (num_continente == 2)
    {
        printf("America");
    }
    else if (num_continente == 3)
    {
        printf("Africa");
    }
    else //Numero debe ser 4
    {
        printf("Oceania");
    }
}

int envios_por_continente(int vorigen[], float vcoste[], float vingreso[])
{
    //Crear ficheros para imprimir
    FILE *europa = fopen("europa.txt", "w");
    if (europa == NULL)
    {
        return false;
    }

    FILE *asia = fopen("asia.txt", "w");
    if (asia == NULL)
    {
        fclose(europa);
        return false;
    }

    FILE *america = fopen("america.txt", "w");
    if (america == NULL)
    {
        fclose(europa);
        fclose(asia);
        return false;
    }

    FILE *africa = fopen("africa.txt", "w");
    if (africa == NULL)
    {
        fclose(europa);
        fclose(asia);
        fclose(america);
        return false;
    }

    FILE *oceania = fopen("oceania.txt", "w");
    if (oceania == NULL)
    {
        fclose(europa);
        fclose(asia);
        fclose(america);
        fclose(africa);
        return false;
    }

    //Imprimir en los ficheros
    for (int i = 0; i < NE; i++)
    {
        //Obtener el continente del envio
        int codigo = continente_de_puerto(vorigen[i]);

        //Imprimir en el fichero que corresponda segun continente
        if (codigo == 0) //Europa
        {
            fprintf(europa, "%i %.2f %.2f\n", vorigen[i], vcoste[i], vingreso[i]);
        }
        else if (codigo == 1) //Asia
        {
            fprintf(asia, "%i %.2f %.2f\n", vorigen[i], vcoste[i], vingreso[i]);
        }
        else if (codigo == 2) //America
        {
            fprintf(america, "%i %.2f %.2f\n", vorigen[i], vcoste[i], vingreso[i]);
        }
        else if (codigo == 3) //Africa
        {
            fprintf(africa, "%i %.2f %.2f\n", vorigen[i], vcoste[i], vingreso[i]);
        }
        else //Oceania (4)
        {
            fprintf(oceania, "%i %.2f %.2f\n", vorigen[i], vcoste[i], vingreso[i]);
        }
    }

    //Cerrar ficheros
    fclose(europa);
    fclose(asia);
    fclose(america);
    fclose(africa);
    fclose(oceania);

    //Ejecutado satisfactoriamente
    return true;
}
