#include <stdio.h>

// Some functions
void merge_sort(int main_arr[], int change1[], int change2[], int N);
void sort(int arr[], int pl, int pr, int change1[], int change2[]);
void merge(int arr[], int limit_l, int start_r, int limit_r, int change1[], int change2[]);

int main(void)
{
    // Read file and store information in arrays
    // numbers.txt
    FILE *in = fopen("pset_3_1_1.txt", "r");
    if (in == NULL)
        return 1;
    int N;
    fscanf(in, "%i", &N);
    int weight[N], length[N], scores[N];
    for (int i = 0; i < N; i++)
    {
        fscanf(in, "%i %i", &weight[i], &length[i]);
        // Compute score according to formula: weight - length
        scores[i] = weight[i] - length[i];
    }
    fclose(in);
    // Sort scores in DECREASING order, with ever change done there also applied to weight and length
    merge_sort(scores, weight, length, N);
    // Compute the wieighted sum, accumulating the lengths
    int acc_length = 0;
    long long int sum = 0;
    // DEBUG file
    FILE *fout = fopen("c_out.txt", "w");
    if (fout == NULL)
        return 2;
    for (int i = 0; i < N; i++)
    {
        acc_length +=  length[i];
        sum += (long long) weight[i] * acc_length;
        fprintf(fout, "%lli\n", sum);
    }
    fclose(fout);
    // Print results
    printf("%lli\n", sum);
}

void merge_sort(int main_arr[], int change1[], int change2[], int N)
{
    // Sort left, right, and merge
    sort(main_arr, 0, N/2 - 1, change1, change2);
    sort(main_arr, N/2, N - 1, change1, change2);
    merge(main_arr, 0, N/2, N - 1, change1, change2);
}

void sort(int arr[], int pl, int pr, int change1[], int change2[])
{
    if (pr - pl < 1)
        return;
    else
    {
        sort(arr, pl, (pr + pl)/ 2, change1, change2);
        sort(arr, ((pr + pl)/ 2) + 1, pr, change1, change2);
        merge(arr, pl, ((pr + pl)/ 2) + 1, pr, change1, change2);
    }
}

void merge(int arr[], int limit_l, int start_r, int limit_r, int change1[], int change2[])
{
    int pl = limit_l;
    int pr = start_r;
    int length = (limit_r - limit_l) + 1;
    int extra1[length], extra2[length], extra3[length];
    int p = 0;
    // Start comparing and filling extra[]
    while (pl < start_r && pr <= limit_r)
    {
        // If left is bigger
        if (arr[pl] > arr[pr])
        {
            extra1[p] = arr[pl];
            extra2[p] = change1[pl];
            extra3[p] = change2[pl];
            pl++;
        }
        // If right is bigger
        else if (arr[pl] < arr[pr])
        {
            extra1[p] = arr[pr];
            extra2[p] = change1[pr];
            extra3[p] = change2[pr];
            pr++;
        }
        // If there is a tie, then put the one with higher weight first
        else // arr[pl] == arr[pr]
        {
            // Weith[] is passed in as change1
            if (change1[pl] >= change1[pr])
            {
                extra1[p] = arr[pl];
                extra2[p] = change1[pl];
                extra3[p] = change2[pl];
                pl++;
            }
            else // change1[pl] < change1[pr]
            {
                extra1[p] = arr[pr];
                extra2[p] = change1[pr];
                extra3[p] = change2[pr];
                pr++;
            }
        }
        p++;
    }
    // Complete filling the array by copying elements remaining
    // If left half is unfinished
    if (pl < start_r)
    {
        int repeat = start_r - pl;
        for(int i = 0; i < repeat; i++)
        {
            extra1[p] = arr[pl];
            extra2[p] = change1[pl];
            extra3[p] = change2[pl];
            pl++;
            p++;
        }
    }
    // Else if right half unfinished
    else if (pr < limit_r + 1)
    {
        int repeat = limit_r - pr + 1;
        for(int i = 0; i < repeat; i++)
        {
            extra1[p] = arr[pr];
            extra2[p] = change1[pr];
            extra3[p] = change2[pr];
            pr++;
            p++;
        }
    }
    // Copy array back
    int eleft = limit_l;
    for (int i = 0; i < length; i++)
    {
        arr[eleft] = extra1[i];
        change1[eleft] = extra2[i];
        change2[eleft] = extra3[i];
        eleft++;
    }
    return;
}