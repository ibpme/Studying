#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * data;
int * enc;


int main (int argc , char *argv[]){
    data = malloc(sizeof(char) * strlen(argv[1])+1);
    enc = malloc(sizeof(int) * strlen(argv[1])+1);
    strcpy(data, argv[1]);
    // unsigned long num=1;

    for (int i= 0; i < strlen(data) -1; i++)
    {
        enc[i] = (int)data[i]*(int)data[i+1];

        // printf("data index %d: %d\n",i,data[i]);
        // printf("%d\n",enc[i]);
    }
    int j = strlen(data)-1;
    enc[j]=(int)data[0]*(int)data[j];

    // printf("data index %d: %d\n",j,data[j]);
    // printf("%d\n",enc[j]);

    int new;
    for (int k = 0; k < strlen(data); k++)
    {
        enc[k] = (enc[k] % 94 + 33) % 94;
        printf("%c",enc[k]);
    }
    free(data);
    free(enc);
    return 0;
}

