from csv import reader

comp = []

def main():
    temp = []
    # Open file and read numbers
    with open("pset3.txt", "r") as filein:
        fin = reader(filein)
        for number in fin:
            temp.append(number)
    numbers = []
    for sublist in temp:
        for char in sublist:
            numbers.append(int(char))
    # Choose sorting method
    method = 1
    # Sort
    qsort(numbers, 0, len(numbers) - 1, method)
    n = 0
    for number in comp:
        n += number
    print(n)


def qsort(arr, l, r, method):
    if len(arr[l:r + 1]) < 2:
        return
    else:
        comp.append(r-l)
        ChoosePivot(arr, l, r, method)
        p_pos = partition(arr, l, r)
        qsort(arr, l, p_pos - 1, method) # Left
        qsort(arr, p_pos + 1, r, method) # Right
    return


def partition(arr, l, r):
    i = l
    p = arr[l] # first element will always be the pivot
    for j in range(l, r + 1):
        if arr[j] < p:
            arr[j], arr[i+1] = arr[i+1], arr[j]
            i += 1
    arr[l], arr[i] = arr[i], arr[l]
    return i

def ChoosePivot(arr, l, r, method):
    return

main()