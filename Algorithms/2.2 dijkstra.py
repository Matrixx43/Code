# Dijkstra's shortest path algorithm

# Constants
N = 200

def main():
    # Load the graph. graph[1] is for node 1, etc
    graph = [[]]
    with open("pset_2_2.txt", "r") as fo:
        for line in fo.readlines():
            edges = []
            for edge in line.split()[1:]:
                l = edge.split(',')
                l = [int(i) for i in l]
                edges.append(l)
            graph.append(edges)
    # List of visited vertices so far. For this program, let 1 be the root vertex
    X = [1]
    # List of shortest path distances computed so far. If a path does not exist, let it be 10^6
    A = (N + 1)*[1000000]
    A[1] = 0
    # Main loop
    while len(X) < N:
        # Compute the dijkstra score of each vertex from X to outside of X and increase X by adding that outside vertex to X
        scores = []
        for visited_vertex in X:
            for edge in graph[visited_vertex]:
                # If they have not been visited yet
                if edge[0] not in X:
                    # Score = distance from root to visited_vertex + the distance to the new vertex
                    scores.append([A[visited_vertex] + edge[1], edge[0]]) # Append [distance, dest vertex]
        # Calculate vertex that minimizes the Dijkstra's score, and add it to X
        min_score = scores[0]
        for score in scores:
            if score[0] < min_score[0]:
                min_score = score
        X.append(min_score[1])
        A[min_score[1]] = min_score[0]
        
    # Display some results, as asked
    print(f"{A[7]},{A[37]},{A[59]},{A[82]},{A[99]},{A[115]},{A[133]},{A[165]},{A[188]},{A[197]}")
        


    
            






main()