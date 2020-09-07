#include <stdio.h>
#include <stdlib.h>

int main()
{
    int integer = 10;
    char character = 'A';
    char * charactersArray = "anArrayOfCharacters";// This type of variable declaration will always give a pointer (memory address)
    double doubleData = 2.1;
    double * p_doubleData = &doubleData; // Declare a pointer to the doubleData Memory adress
    printf("%p\n", p_doubleData); // This will print the memory address (pointer)
    printf("%f\n", *p_doubleData); // This will derefrence the pointer . Derefrence (*) operator can only be applied to a memory address outside of pointer declaration

    
    printf("%p\n", charactersArray);//This variable is a pointer to the first char of the charactersArray string or charactersArray[0] (memoryAdress of the first char)
    printf("%p\n", &charactersArray); // This variable is the memory address of the pointer above (not important)
    printf("%p\n", &charactersArray[0]);// This is the memory address of the first char of the charactersArray string (memoryAdress of the first char)
    printf("%p\n", &charactersArray[1]);// This is the memory adress of the second char of the charactersArray string
    // because charactersArray variable is a pointer (memory address ) to (of) the first char we can access the charactersArray without derefrencing character array
    printf("%s\n", charactersArray); // Because this is a pointer the printf will print the array of chars this pointer is pointing at when applied in the %s 
    printf("%c\n", charactersArray[0]);// This is not good practice to understand because charactersArray is also pointer 
    printf("%c\n", charactersArray[1]);
    //Pointer Arithmetic 
    printf("%c\n", *charactersArray); //When we derefrence this pointer it will give us the first char
    printf("%c\n", *(charactersArray+1)); //When we derefrence this pointer it will give us the second char

    return 0;
}
