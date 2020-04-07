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

    for i in range(n):
        b = a[i]
        c = i - 1
        while c >= 0 and b < a[c]:
            a[c + 1] = a[c]
            c -= 1
        a[c + 1] = b


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
    """If array is in ascending order this converts the array to descending order"""

    for i in range(int(n / 2)):
        h = int(n - i - 1)
        s = a[i]
        a[i] = a[h]
        a[h] = s
