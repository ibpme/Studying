from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height>0:
        break

for row in range(height+1):
    for spaces in range(height-row):
        print(" ",end='')
    for left in range(row):
        print('#',end='')
    print("  ",end='')
    for right in range(row):
        print('#',end='')
    print()