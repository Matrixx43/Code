def product(x, y):
    # Select the maximum length
    L = int(len(x))
    if int(len(y)) > L:
        L = int(len(y))
    if L == 1:
        return int(int(x) * int(y));
    else:
        # Select l where l = n/2
        if L % 2 == 0:
            l = int(L/2)
        else:
            # Round it up
            l = int(L/2) + 1
        n = 2*l
        # Set b and d to l digits
        list1 = split(x, l)
        a = list1[0]
        b = list1[1]
        list2 = split(y, l)
        c = list2[0]
        d = list2[1]
        n1 = product(a, c)
        n2 = product(b, d)
        n3 = product(str(int(a) + int(b)), str(int(c) + int(d)))
        n4 = str(int(n3) - int(n2) - int(n1))
        return str((int(n1) * (10 ** n) + int(n2) + int(n4) * (10 ** l)))

def split(n, digits):
    # Get a number n as a string and how many digits has to have in the right part.
    # Returns strings. If there are not enough numbers, they are replaced with 0.
    # If left part is empty, it is replaced with 0.
    list = []
    if len(n) > digits:
        cut = len(n) - digits
        list.append(n[:cut])
        list.append(n[cut:])
    else:
        list.append('0')
        add = len(n) - digits
        for i in range (add):
            n = '0' + n
        list.append(n)
    return list

while (True):
    print("Number 1: ")
    n1 = input()
    print("Number 2: ")
    n2 = input()
    result = product(n1, n2)
    print(result)
    if(int(result) == int(n1) * int(n2)):
        print("YES!")