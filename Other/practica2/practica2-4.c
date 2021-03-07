#include <stdio.h>

#define enttot 110
#define entno 100
#define entdi 10

int main(void)
{
    FILE *fout = NULL;
    fout = fopen("ocupacion.txt", "w");
    if (fout == NULL)
    {
        return 1;
    }
    int ent_no = entno, ent_di = entdi, ent_vno, ent_vdi, ent_v;
    int no[3], di[3];
    for (int i = 0; i < 3; i++)
    {
        printf("Numero de entradas no discapacitados (libres: %i): ", ent_no);
        scanf("%i", &no[i]);
        printf("Numero de entradas discapacitados (libres: %i): ", ent_di);
        scanf("%i", &di[i]);
        ent_no -= no[i];
        ent_di -= di[i];
    }
    ent_vno = entno - ent_no;
    ent_vdi = entdi - ent_di;
    ent_v = ent_vno + ent_vdi;
    fprintf(fout, "Entradas vendidas: %i ", ent_v);
    fprintf(fout, "(No discapacitados: %i Discapacitados: %i)\n", ent_vno, ent_vdi);
    fprintf(fout, "Porcentaje de ocupacion del teatro: %.2f%% ", 100 * (float)ent_v / (float)enttot);
    fprintf(fout, "(No discapacitados: %.2f%% Discapacitados: %.2f%%)\n", 100 * (float)ent_vno / (float)entno, 100 * (float)ent_vdi / (float)entdi);
    fclose(fout);
    return 0;
}