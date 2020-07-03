#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc !=2){
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26){
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    string plain=get_string("plaintext:");
    string keys_upper=argv[1];
    char lower[26];
    for(int k=0;k<26; k++){
        lower[k]=keys_upper[k]+ 32;
    }
    string keys_lower=lower;
    printf("ciphertext:");
    int i=0;
    while(i<strlen(plain)){
        int num=plain[i]- 65;
        if (num<26){
            printf("%c",keys_upper[num]);
        }
        if (num>26){
            num-=32;
            printf("%c",keys_lower[num]);
        }
        i++;
    }
    printf("\n");
    return 0;
}