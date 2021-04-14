// For the numbers in the interval [-10000, 10000], compute how many of them have a sum by 2 distinct numbers in a given file.

#include <stdio.h>

#define N 20001
#define max 10000

void lookup(long array[], long i, int sums_exist[], int length);
int bin_search_left(long array[], long i,int length);
int bin_search_right(long array[], long i,int length);

int main(void)
{
    // Read file. All numbers are unique and sorted
    FILE *in = fopen("sorted_2_4.txt", "r");
    if (in == NULL)
        return 1;
    int length;
    fscanf(in, "%i", &length);
    // Store numbers in array
    long array[length];
    for (int i = 0; i < length; i++)
        fscanf(in, "%li", &array[i]);
    // For each number i in the array, look for other numbers in the interval [-10000 - i, 10000 - i] that are in the array.
    // If there are numbers there, tehn they sum one of the interesting values in [-10000, 10000]
    // Keep track of each number to see if it is summed by some numbers in the array
    int sums_exist[N];
    for (int i = 0; i < N; i++)
        sums_exist[i] = 0;
    // Iterate over numbers to see if pairs of them sum in between -10000 and 10000
    for (int i = 0; i < length; i++)
    {
        if (i %10000 == 0)
            printf("%i\n", i);
        lookup(array, array[i], sums_exist, length);
    }
    // Calculate numbers in sums_exist that have values greater than 0
    int good_sums = 0;
    for (int i = 0; i < N; i++)
    {
        if (sums_exist[i] > 0)
            good_sums += 1;
    }
    printf("%i sums were found\n", good_sums);
    
}

void lookup(long array[], long i, int sums_exist[], int length)
{
    int lower_bound_pos, upper_bound_pos;
    // Binary search for pos_left: position of number in array that is equal or greater than -10000 - i
    lower_bound_pos = bin_search_left(array,(long) -max - i, length);
    upper_bound_pos = bin_search_right(array,(long) max - i, length);
    // Make sure that there will be valid solutions
    if (lower_bound_pos < length && upper_bound_pos >= 0)
    {
        for (int j = lower_bound_pos; j <= upper_bound_pos; j++)
        {
            // Compute number that they sum. This will be between -10000 and 10000
            sums_exist[max + i + array[j]] += 1;
        }
    }
    return;
    

}

int bin_search_left(long array[], long i,int length)
{
    // If the number is found, return its position in array[].
    // Otherwise, return the position of closest number above it.
    int p_left = 0;
    int p_right = length - 1;
    while (p_right - p_left > 0)
    {
        int mid = (p_right + p_left)/2;
        if (array[mid] > i)
        {
            p_right = mid - 1;
        }
        else if (array[mid] < i)
        {
            p_left = mid + 1;
        }
        else // mid is the position of wanted number
        {
            return mid;
        }
    }
    // Make sure it returns the position of the first number above i
    if (array[p_left] < i)
        p_left++; // Note that it could go above the array limit, in such case meaning that no numbers in the array satisfy the conditions
    return p_left;
}

int bin_search_right(long array[], long i,int length)
{
    // If the number is found, return its position in array[].
    // Otherwise, return the position of closest number below it.
    int p_left = 0;
    int p_right = length - 1;
    while (p_right - p_left > 0)
    {
        int mid = (p_right + p_left)/2;
        if (array[mid] > i)
        {
            p_right = mid - 1;
        }
        else if (array[mid] < i)
        {
            p_left = mid + 1;
        }
        else // mid is the position of wanted number
        {
            return mid;
        }
    }
    // Make sure it returns the position of the first number below i
    if (array[p_right] > i)
        p_right--;
    return p_right;
}