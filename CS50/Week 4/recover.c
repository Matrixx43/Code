#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

int N = 512;
typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    //Check command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    //Open the file "memory card"
    FILE* mc = fopen(argv[1], "r");
    if (mc == NULL)
    {
        printf("Failed to open file");
        return 2;
    }
    int jpeg_count = 0;
    char filename[8] = {'0', '0', '0', '.', 'j', 'p', 'g', '\0'};
    BYTE arr[N];
    FILE* ptr = NULL;
    while (fread(arr, sizeof(arr), 1, mc) != 0)
    {
        //If beginning of new jpeg
        if (arr[0] == 0xff && arr[1] == 0xd8 && arr[2] == 0xff && (arr[3] & 0xf0) == 0xe0)
        {
            //If first jpeg
            if (jpeg_count == 0)
            {
                sprintf(filename, "%03i.jpg", jpeg_count);
                //Open new file to write to
                ptr = fopen(filename, "w");
                //Write to file
                fwrite(arr, sizeof(arr), 1, ptr);
            }
            //If another new jpeg
            else
            {
                //Close previous file
                fclose(ptr);
                sprintf(filename, "%03i.jpg", jpeg_count);
                //Open new file to write to
                ptr = fopen(filename, "w");
                //Write to file
                fwrite(arr, sizeof(arr), 1, ptr);
                
            }
            jpeg_count += 1;
        }
        //If continuation of jpeg
        else if (jpeg_count > 0)
        {
            //Write to file
            fwrite(arr, sizeof(arr), 1, ptr);
        }
    }
    fclose(ptr);
    fclose(mc);
}
