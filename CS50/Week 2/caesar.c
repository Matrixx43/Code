#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>


string encrypt(int, string);
int check(string[]);


int main(int argc, string argv[])
{
    if (argc != 2){printf("Usage: ./cesar key\n"); return 1;}
    if (check(argv) != 0){printf("Usage: ./cesar key\n"); return 1;}

    string text = get_string("plaitext: ");
    text = encrypt(atoi(argv[1]), text);
    printf("ciphertext: %s\n", text);

}





int check(string s[]) // Check that it is only integers
{
    int j = 0;
    int l = strlen(s[1]);
    for (int i = 0; i < l; i ++)
    {
        if (s[1][i] < '0' || s[1][i] > '9')
        {
            j++;
            printf("j is not %i\n", j);
        }
    }
    return j;
}

string encrypt(int k, string s)
{
    if (k > 25) {k = k % 26;}
    int l = strlen(s);
    for (int i = 0; i < l; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            for (int j = 0; j < k; j++)
            {
                if (s[i] < 'z') {s[i] += 1;}
                else {s[i] = 'a';}
            }
        }
        else if (s[i] >= 'A' && s[i] <= 'Z')
        {
            for (int j = 0; j < k; j++)
            {
                if (s[i] < 'Z') {s[i] += 1;}
                else {s[i] = 'A';}
            }
        }
    }
    return s;
}