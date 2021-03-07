#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0

#define ASIENTOS 20

#define LIBRE 0
#define HOMBRE 1
#define MUJER 2
#define NINO 3

#define PRIMER_ASIENTO_PRIMCLASE 0
#define PRIMER_ASIENTO_BUSINESS 4
#define PRIMER_ASIENTO_TURISTA 11

//Prototipos de funciones
void Inicializa_Asientos(int asientos[]);
int Menu();
void Reservar_Plaza(int asientos[]);
void Obtener_asientos_libres(int asientos[], int asientos_libres[], int *num_asientos_libres);
float Calculo_facturacion(int asientos[], float *fac_primera, float *fac_segunda, float *fac_tercera);
int hay_plaza_doble(int asientos[], int *asiento1, int* asiento2);

int main ( )
{
   int opc, asientos[ASIENTOS];
   int asientos_libres[ASIENTOS];
   int num_asientos_libres = 0;
   float fac_primera = 0, fac_segunda = 0, fac_tercera = 0, fac_total;
   bool plaza_doble;
   int asiento1, asiento2;
   // Nuevas variables

   // Inicializamos todos los asientos a LIBRE
   Inicializa_Asientos(asientos);

   do{
      opc = Menu();
      switch(opc)
      {
		case 1:
			// Llamada a la función reservar plaza
			Reservar_Plaza(asientos);
			break;

		case 2:
			// Llamada a la función Obtener_asientos_libres
			Obtener_asientos_libres(asientos, asientos_libres, &num_asientos_libres);

			// Escribir los asientos libres
			printf("Los asientos libres son: ");
			for (int i = 0; i < num_asientos_libres; i++)
			{
				printf("%i, ", asientos_libres[i]);
			}
			printf("\n");

			// Escribir el porcentaje de ocupación del avión
			printf("---%i---\n", num_asientos_libres);
			printf("El porcentaje de ocupacion es %.2f %%\n", (float)(ASIENTOS - num_asientos_libres) * 100 / ASIENTOS);

			break;

		case 3:
			// Llamada a la función  Calculo_facturacion
			fac_total = Calculo_facturacion(asientos, &fac_primera, &fac_segunda, &fac_tercera);

			// Escribir las facturaciones
			printf("La facturacion de la clase primera es %.2f\n", fac_primera);
			printf("La facturacion de la clase business es %.2f\n", fac_segunda);
			printf("La facturacion de la clase turista es %.2f\n", fac_tercera);
			printf("La facturacion total es %.2f\n", fac_total);

			break;

		case 4:
			// Llamada a la función Hay_plaza_doble
			 plaza_doble = hay_plaza_doble(asientos, &asiento1, &asiento2);

			// Escribir las plazas dobles o mensaje de error
			if (plaza_doble)
			{
				printf("Hay al menos una plaza doble, en los sientos %i y %i\n", asiento1, asiento2);
			}
			else
			{
				printf("No se ha encontrado ninguna plaza doble\n");
			}

			break;

      }
   }while (opc != 5);

   return 0;
}

void Inicializa_Asientos(int asientos[])
{
	int i;
	for (i=0;i<ASIENTOS;i++)
		asientos[i]=LIBRE;
}

int Menu()
{
	int opc;

	do{
	   printf("\n");
	   printf("1. Reservar plaza\n");
	   printf("2. Obtener asientos libres\n");
	   printf("3. Facturacion\n");
	   printf("4. Buscar plaza doble\n");
	   printf("5. Salir\n");
	   printf("Seleccione una opcion: ");
	   scanf("%d",&opc);
	}while(opc<1 || opc>5);

	return opc;
}

void Reservar_Plaza(int asientos[])
{
    int plaza, tipo;
    do{
     printf("Que asiento quieres? Entre 0 y %d ",ASIENTOS-1);
     scanf("%d",&plaza);
    }while (plaza<0 || plaza>=ASIENTOS);

    if (asientos[plaza] == LIBRE)
    { // Plaza Libre -> Reservar
        do{
            printf("El viajero es hombre=%d, mujer=%d, ni~no=%d?\n",HOMBRE,MUJER,NINO);
           scanf("%d",&tipo);
        }while (tipo != HOMBRE && tipo != MUJER && tipo != NINO);

        asientos[plaza] = tipo;
        printf("La plaza %d ha quedado reservada\n",plaza);
    }
    else
        printf("Lo sentimos. La plaza %d ya esta reservada\n",plaza);
}

// Obtener asientos libres
void Obtener_asientos_libres(int asientos[], int asientos_libres[], int *num_asientos_libres)
{
	int contador = 0;
	for (int i = 0; i < ASIENTOS; i++)
	{
		if (asientos[i] == LIBRE)
		{
			*num_asientos_libres += 1;
			asientos_libres[contador] = i;
			contador++;
		}
	}
}

// Cálculo de la facturación
float Calculo_facturacion(int asientos[], float *fac_primera, float *fac_segunda, float *fac_tercera)
{
	//Obtener precio de cada plaza
	float pprimera, psegunda, ptercera;
	printf("Precio billete primera clase: ");
	scanf("%f", &pprimera);
	printf("Precio billete segunda clase: ");
	scanf("%f", &psegunda);
	printf("Precio billete tercera clase: ");
	scanf("%f", &ptercera);

	//Calcular la facturacion de cada tipo de plaza
	for (int i = PRIMER_ASIENTO_PRIMCLASE; i < PRIMER_ASIENTO_BUSINESS; i++)
	{
		if (asientos[i] != 0)
		{
			*fac_primera += pprimera;
		}
	}
	for (int i = PRIMER_ASIENTO_BUSINESS; i < PRIMER_ASIENTO_TURISTA; i++)
	{
		if (asientos[i] != 0)
		{
			*fac_segunda += psegunda;
		}
	}
	for (int i = PRIMER_ASIENTO_TURISTA; i < ASIENTOS; i++)
	{
		if (asientos[i] != 0)
		{
			*fac_tercera += ptercera;
		}
	}

	//Devolver fac_total
	return *fac_primera + *fac_segunda + *fac_tercera;
}

// Buscar una plaza doble
bool hay_plaza_doble(int asientos[], int *asiento1, int* asiento2)
{
	for (int i = 0; i < ASIENTOS; i += 2)
	{
		if (asientos[i] == 0 && asientos[i + 1] == 0)
		{
			*asiento1 = i;
			*asiento2 = i + 1;
			printf("Asiento 1 %i, Asiento 2 %i\n", *asiento1, *asiento2);
			return true;
		}
	}
	return false;
}