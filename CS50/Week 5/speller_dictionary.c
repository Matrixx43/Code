// Implements a dictionary's functionality

#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Number of buckets in hash table
const unsigned int N = 26 * 26;

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    //Make a copy of word
    char *string = malloc((LENGTH + 1) * sizeof(char));
    if (string == NULL)
    {
        return false;
    }
    strcpy(string, word);
    //Lowercase string
    int length = LENGTH + 1;
    for (int i = 0; i < length; i++)
    {
        string[i] = tolower(string[i]);
    }
    
    //Get the hash value for string
    int hashvalue = hash(word);
    
    //Search for a match in dictionary
    node *ptr = table[hashvalue];
    while (ptr != NULL)
    {
        if (!strcmp(string, ptr->word))
        {
            return true;
        }
        ptr = ptr->next;
    }
    //If table(hasvalue) is NULL or the search through the list gave no results, it is false
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //Homemade bad hash function
    char letter1 = tolower(word[0]);
    char letter2 = tolower(word[1]);
    if (!isalpha(letter1))
    {
        return 0;
    }
    else if (!isalpha(letter2))
    {
        return(26 * (letter1 - 'a'));
    }
    return(26 * (letter1 - 'a') + (letter2 - 'a'));
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    //Initialize table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    FILE *in = fopen(dictionary, "r");
    if (in == NULL)
    {
        return false;
    }
    char *scannedword = malloc((LENGTH + 1) * sizeof(char));
    if (scannedword == NULL)
    {
        return 1;
    }
    node *ptr = malloc(sizeof(node));
    if (ptr == NULL)
        {
            return false;
        }
    while (fscanf(in, "%s", scannedword) != EOF)
    {
        ptr = malloc(sizeof(node));
        if (ptr == NULL)
        {
            return false;
        }
        //Get hash value
        int hashvalue = hash(scannedword);
        //Set up the node in the hash function
        strcpy(ptr->word, scannedword);
        if(table[hashvalue] == NULL)
        {
            ptr->next = NULL;
            table[hashvalue] = ptr;
        }
        else //The table already has some added nodes for that value
        {
            ptr->next = table[hashvalue];
            table[hashvalue] = ptr;
        }
    }
    fclose(in);
    free(scannedword);
    free(ptr);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int size = 0;
    node *ptr = NULL;
    for (int i = 0; i < N; i++)
    {
        ptr = table[i];
        while (ptr != NULL)
        {
            size++;
            ptr = ptr->next;
        }
    }
    return size;
}

void eliminate(node *ptr);

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
       if (table[i] == NULL)
       {
           
       }
       else
       {
           eliminate(table[i]);
       }
    }
    return true;
}

void eliminate(node* ptr)
{
    if (ptr -> next == NULL)
    {
        free(ptr);
        return;
    }
    else
    {
        eliminate(ptr -> next);
        free(ptr);
    }
}
