// Kosaraju's graph algorithm for computing SCC's

#include <stdio.h>
#include <stdlib.h>

// Number of nodes
#define N 875714

// Define a node struct to create linked lists
typedef struct node
{
    int number;
    struct node *next;
}
node;

// Some functions
void dfs_loop(node *graph[], int ftime[], int leader[]);
void dfs(node *graph[], int *i, int *t, int *s, int visited[], int ftime[], int leader[]);
void clear(node *graph[]);
void del(node *ptr);
void maximum(int leader[], int max[]);



int main(void)
{
    // Create the graph as an adjacency list
    // Node numbers start at 1, so graph[0] will not be used
    node *graph[N + 1];
    for (int i = 0; i <= N; i++)
        graph[i] = NULL;
    // Store the finish time and leader information
    int ftime[N + 1], leader[N + 1];
    // First pass: G is reversed, run dfs_loop to compute finishing times
    // Load graph, in REVERSED order
    FILE *in = fopen("pset_2_1.txt", "r");
    if(in == NULL)
    {
        printf("Error opening file on pass 1\n");
        return 1;
    }
    int origin;
    int dest;
    // Read in reversed order, so a -> b ==> a = dest, b = origin
    while(fscanf(in, "%i %i", &dest, &origin) != EOF)
    {
        // Create a new node
        node *new_node = malloc(sizeof(node));
        if(new_node == NULL)
        {
            printf("Error allocating memory to nodes on pass 1\n");
            return 2;
        }
        new_node->number = dest;
        new_node->next = NULL;
        // Attach it to the list at the END, so as to respect the order given in the .txt
        if(graph[origin] == NULL)
        {
            graph[origin] = new_node;
        }
        else
        {
            node *ptr = graph[origin];
            // Search for last element in the list
            while (ptr->next != NULL)
            {
                ptr = ptr->next;
            }
            // Append the new_node at the end
            ptr->next = new_node;
        }
    }
    fclose(in);
    // Run dfs_loop for the first time
    dfs_loop(graph, ftime, leader);
    // Second Pass: G is not reversed, run dfs_loop to compute leaders
    // Clear graph to reload it
    clear(graph);
    printf("Starting second pass\n");
    for (int i = 0; i <= N; i++)
        graph[i] = NULL;
    // Reload graph, but this time the number of the nodes is ftime[number], and the order of the graph is not reversed
    in = fopen("pset_2_1.txt", "r");
    if (in == NULL)
    {
        printf("Error opening file on pass 2\n");
        return 3;
    }
    // Read in reversed order, so a -> b ==> a = dest, b = origin
    while(fscanf(in, "%i %i", &origin, &dest) != EOF)
    {
        // Change the numbers so that ftimes are used
        origin = ftime[origin];
        dest = ftime[dest];
        // Create a new node
        node *new_node = malloc(sizeof(node));
        if(new_node == NULL)
        {
            printf("Error allocating memory to nodes on pass 2\n");
            return 4;
        }
        new_node->number = dest;
        new_node->next = NULL;
        // Attach it to the list at the END, so as to respect the order given in the .txt
        if (graph[origin] == NULL)
        {
            graph[origin] = new_node;
        }
        else
        {
            node *ptr = graph[origin];
            // Search for last element in the list
            while (ptr->next != NULL)
            {
                ptr = ptr->next;
            }
            // Append the new_node at the end
            ptr->next = new_node;
        }
    }
    fclose(in);
    // Run dfs_loop for the second time
    dfs_loop(graph, ftime, leader);
    // Done with the graph
    clear(graph);
    // Compute the 5 maximum SCC using the leaders
    int max[5];
    maximum(leader, max);
    // Display results
    for (int i = 0; i < 5; i++)
    {
        printf("%i  ", max[i]);
    }
    printf("\n");
    // Run successfully
    return 0;

}

void dfs_loop(node *graph[], int ftime[], int leader[])
{
    // Keep track of visited nodes
    int visited[N + 1];
    for (int i = 0; i <= N; i++)
        visited[i] = 0;
    // Keep track of the number of nodes processed so far. t will assign the ftime's. Used in 1st pass
    int t = 0;
    // Keep track of current source vertex. s will assign the leader's. Used in 2nd pass
    int s;
    // Visit all nodes, backwards
    for (int i = N; i >= 1; i--)
    {
        // If node not yet visited
        if (visited[i] == 0)
        {
            s = i;
            dfs(graph, &i, &t, &s, visited, ftime, leader);
        }
    }
}

void dfs(node *graph[], int *i, int *t, int *s, int visited[], int ftime[], int leader[])
{
    // Now the node is visited
    visited[*i] = 1;
    // Its leader is node s
    leader[*i] = *s;
    // For every edge coming out of i, if not explored, recurse on it (DFS)
    node *ptr = graph[*i];
    while (ptr != NULL)
    {
        if (visited[ptr->number] == 0)
            dfs(graph, &(ptr->number), t, s, visited, ftime, leader);
        ptr = ptr->next;
    }
    *t += 1;
    ftime[*i] = *t;
    return;
}

void clear(node *graph[])
{
    // We know that the length is N + 1
    for (int i = 0; i <= N; i++)
    {
        if (graph[i] != NULL)
            del(graph[i]);
    }
}

void del(node *ptr)
{
    if (ptr->next == NULL)
    {
        free(ptr);
        return;
    }
    else
    {
        del(ptr->next);
        free(ptr);
        return;
    }
}

void maximum(int leader[], int max[])
{
    // Create an extra array to compute the repetitions of each leader
    int repe[N + 1];
    for (int i = 0; i <= N; i++)
    {
        repe[i] = 0;
    }
    // Iterate leader, and count their number in repe[]
    for (int i = 1; i <= N; i++)
    {
        repe[leader[i]] += 1;
    }
    // For five times, find the maximum in the repe[] and store their #repetitions in max[]
    for (int i = 0; i < 5; i++)
    {
        int m_pos = 0;
        for (int j = 1; j <= N; j++)
        {
            if (repe[j] > repe[m_pos])
                m_pos = j;
        }
        // Store value
        max[i] = repe[m_pos];
        // Set repe[m_pos] = 0 so that we can find 2nd, 3rd, etc maximums
        repe[m_pos] = 0;
    }
    return;
}