from csv import reader
import random

def main():
    # Read file and create list with all the edges, not repeated eg (1,2) and (2,1)
    with open("pset4.txt","r") as data:
        Oedges = []
        line = data.read().strip().split("\n")
        for element in line:
            line_list = list(map(int, element.strip().split("\t")))
            first = int(line_list[0])
            for vertex in line_list[1:]:
                if int(vertex) > first:
                    Oedges.append([first, int(vertex)])
        mincuts = []
        repeat = 150
        for i in range(repeat):
            print(f"iteration {i + 1} of {repeat}")
            # Copy
            edges = []
            for i in range(len(Oedges)):
                edges.append(Oedges[i].copy())
            # COunt the number of different vertices
            vertices = []
            for sublist in edges:
                for element in sublist:
                    if element not in vertices:
                        vertices.append(element)
            nver = len(vertices)
            while nver > 2:
                contract(edges)
                nver -= 1
            mincuts.append(len(edges))
        print(min(mincuts))

def contract(edges):
    # Select random edge
    nedge = random.randint(0, len(edges) - 1)
    # Store vertices that are merged
    v1 = edges[nedge][0]
    v2 = edges[nedge][1]
    # Remove edges to avoid self loops
    del edges[nedge]
    count = 0
    for Edge in edges:
        if Edge == [v1, v2]:
            count += 1 
    for i in range(count):
        edges.remove([v1, v2])
    count = 0
    for Edge in edges:
        if Edge == [v2, v1]:
            count += 1
    for i in range(count):
        edges.remove([v2, v1])
    # Equal all remaining elements to v1 or v2 -> Merge the vertices
    v = min(v1, v2)
    for i in range(len(edges)):
        for j in range(2):
            if edges[i][j] == v1 or edges[i][j] == v2:
                edges[i][j] = v
    #print(f"contracted {edges}")
    return
    
            

            




main()