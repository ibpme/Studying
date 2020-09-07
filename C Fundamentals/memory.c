#include <stdio.h>
#include <stdlib.h>

int main()
{   
    int integer = 10;
    printf("%p\n", &integer); // Double Qoutes are essential to printing pointers
    integer = 11;
    printf("%p\n",&integer);

    return 0;
}