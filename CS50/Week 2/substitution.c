#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int L = 26; //Number of letters in the alphabet
int number(int, string);
string encrypt(string, string[]);
int check(string[]);

int main(int argc, string argv[])
{
    if (argc != 2) //Check if the number of command-line arguments is 2
    {
        printf("Usage: ./substitution key\n");
        return 1;

    }
    int c = check(argv); //Check the number of characters, if they are letters and if they are repeated
    if (c != 0)
    {
        printf("Error: invalid key. Please type 26 characters (letters)\n");
        return 1;

    }
    string t = get_string("plaintext: "); //Ask for the text to encrypt
    t = encrypt(t, argv); //Encrypt the text
    printf("ciphertext: %s\n", t);
}

int check(string s[])
{
    int j = 0;
    if (strlen(s[1]) != L) //Check if the number of characters in key is correct
    {
        j++;
    }
    for (int i = 0; i < L; i++) //Check if all chatacters are letters
    {
        if (s[1][i] >= 'a' && s[1][i] <= 'z') {}
        else if (s[1][i] >= 'A' && s[1][i] <= 'Z') {}
        else
        {
            j++;

        }
    }
    for (int i = 0; i < L; i++) //Check if any character is repeated
    {
        char a = 97 + i;
        int y = -1;
        for (int r = 0; r < L; r++)
        {
            if (tolower(s[1][r]) == a)
            {
                y++;

            }
        }
        if (y > 0)
        {
            j++;

        }
    }
    return j;
}

string encrypt(string t, string k[]) //Encryption process
{
    int l = strlen(t);
    for (int i = 0; i < l; i++)
    {
        int j = number(i, t);
        if (t[i] >= 'a' && t[i] <= 'z')
        {
            t[i] = tolower(k[1][j]);
        }
        else if (t[i] >= 'A' && t[i] <= 'Z')
        {
            t[i] = toupper(k[1][j]);
        }
    }
    return t;
}

int number(int i, string t) //Get the position number of a letter in the alphabet
{
    int n = 0;
    if (t[i] >= 'a')
    {
        n = t[i] - 'a';
    }
    else
    {
        n = t[i] - 'A';
    }
    return n;
}