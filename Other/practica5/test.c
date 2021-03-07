#include <cs50.h>

int main(void)
{
    int vector[10], max = 0;
    for(int i = 1; i < 10; i++)
    {
        if (vector[i] > vector[max])
        {
            max = i;
        }
    }
}