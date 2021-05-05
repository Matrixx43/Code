# Huffman algorithm on an alphabet

def main():
    # pset_3_3_1.txt
    with open("pset_3_3_1.txt", "r") as fi:
        # Read number of characters in the alphabet
        chars = int(fi.readline())
        # Store the weigth of each character and keep track of their depth
        depths = chars * [1]
        alphabet = []
        for i in range(chars):
            # Each node is represented as [ [chars of this node], combined weigth of the chars]
            alphabet.append([[[i]], int(fi.readline())])
        while len(alphabet) > 2:
            merge(alphabet, depths)
        print(f"Maximum depth is {max(depths)}. Minimum is {min(depths)}")

def merge(alphabet, depths):
    # Select the two smallest nodes by weigth, and merge them. Increase the depth of each participating char by 1
    # Find smallest weigth element
    alphabet.sort(key=lambda x:x[1], reverse=True)
    # Remove smallest element and append it to the second smallest
    a = alphabet.pop()
    if len(a[0]) == 1:
        alphabet[len(alphabet)-1][0].append(a[0][0])
    else:
        alphabet[len(alphabet)-1][0].append(a[0])
    alphabet[len(alphabet)-1][1] += a[1]
    update_depths(alphabet[len(alphabet)-1][0], depths)

def update_depths(node_list, depths):
    for element in node_list:
        if len(element) == 1:
            depths[element[0]] += 1
        else:
            update_depths(element, depths)


main()