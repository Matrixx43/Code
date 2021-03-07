#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool search(int loser, int winner);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (!strcmp(name, candidates[i]))
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int preference = 1; preference < candidate_count; preference++)
    {
        for (int j = 0; j < candidate_count - preference; j++)
        {
            preferences[ranks [preference - 1]][ranks[preference + j]] += 1;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    int n = 0;
    for (int i = 1; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count - i; j++)
        {
            if ((preferences[i-1][i + j] > preferences[i + j][i-1]))
            {
                pairs[n].winner = (i - 1);
                pairs[n].loser = (i + j);
                n++;
            }
            else if ((preferences[i-1][i + j] < preferences[i + j][i-1]))
            {
                pairs[n].winner = (i + j);
                pairs[n].loser = (i - 1);
                n++;
            }
        }
    }
    pair_count = n;
    printf("There are %i pairs\n", pair_count);
    for (int i = 0; i < pair_count; i++)
    {
        printf("Winner of pair %i is %s with %i votes\n", i + 1, candidates[pairs[i].winner], preferences[pairs[i].winner][ pairs[i].loser]);
        printf("Loser of pair %i is %s with %i votes\n", i + 1, candidates[pairs[i].loser], preferences[pairs[i].loser][ pairs[i].winner]);
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int n;
    do
    {
        n = 0;
        for (int i = 0; i < pair_count - 1; i++)
        {
            pair extra;
            if (preferences[pairs[i].winner][pairs[i].loser] < preferences[pairs[i + 1].winner][pairs[i + 1].loser])
            {
                extra.winner = pairs[i].winner;
                extra.loser = pairs[i].loser;
                pairs[i].winner = pairs[i + 1].winner;
                pairs[i].loser = pairs[i + 1].loser;
                pairs[i + 1].winner = extra.winner;
                pairs[i + 1].loser = extra.loser;
                n++;
            }
        }

    }
    while (n != 0);
    for (int j = 0; j < pair_count; j++)
    {
        printf("The winner of pair #%i is %s with %i votes\n", j + 1, candidates[pairs[j].winner], preferences[pairs[j].winner][pairs[j].loser]);
        printf("The loser of pair #%i is %s with %i votes\n", j + 1, candidates[pairs[j].loser], preferences[pairs[j].loser][pairs[j].winner]);
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        if (!search(pairs[i].loser, pairs[i].winner))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        int n = 0;
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i])
            {
                n += 1;
                break;
            }
        }
        if ( n == 0)
        {
            printf("%s", candidates[i]);
        }
    }
}

// Search for a path that would create a loop
bool search(int loser, int winner)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[loser][i])
        {
            if (search(i, winner))
            {
                return true;
            }
        }
    }
    return false;
}

