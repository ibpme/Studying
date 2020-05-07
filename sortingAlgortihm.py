import random

# sorting algorithm
n = int(input("Number of Array: "))
a = [random.randint(1, 100) for i in range(n)]
print(a)


def bubble_sort():
    """ Complexity :
    Best = O(n)
    Average = O(n^2)
    Worst = O(n^2)
    Memmory = 1 """

    while True :
        swap = 0
        for i in range(n-1):
            b = a[i]
            j = i + 1
            if a[j] < b:
                a[i] = a[j]
                a[j] = b
                swap=1
        if swap==0:
            break


def selection_sort():
    """ Complexity :
        Best = O(n^2)
        Average = O(n^2)
        Worst = O(n^2)
        Memmory = 1 """
    for j in range(n):
        min_idx = a[j]
        for i in range(j, n):
            if a[i] < min_idx:
                min_idx = a[i]
                a[i] = a[j]
                a[j] = min_idx


def insertion_sort():
    """ Complexity :
        Best = O(n)
        Average = O(n^2)
        Worst = O(n^2)
        Memmory = 1 """
    i = 1
    while i < n:
        j = i
        while j > 0 and a[j - 1] > a[j]:
            t = a[j - 1]
            a[j - 1] = a[j]
            a[j] = t
            j = j - 1
        i += 1


def ascend_to_descend():
    """If array is in ascending order this converts
    the array to descending order"""

    for i in range(int(n / 2)):
        h = int(n - i - 1)
        s = a[i]
        a[i] = a[h]
        a[h] = s
