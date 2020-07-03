#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string arr)
{
    int text_length = strlen(arr);
    int num=0;
    for(int i=0; i<text_length;i++)
    {
        if (isalpha(arr[i])){
            num +=1;
        }
    }
    return num;
}

int count_words(string arr)
{
    int text_length = strlen(arr);
    int space=1;
    for(int i=0; i<text_length;i++)
    {
        if (isspace(arr[i])){
            space +=1;
        }
    }
    return space;
}
int count_sentences(string arr)
{
    int text_length = strlen(arr);
    int periods=0;
    for(int i=0; i<text_length;i++)
    {
        if (arr[i]=='?' || arr[i]=='!' || arr[i]=='.'){
            periods +=1;
        }
    }
    return periods;
}

float cli(int l,int w ,int s){

    float L= l*100/w;
    float S= s*100/w;
    float index= 0.0588 * L - 0.296 * S - 15.8;
    return index;
}
int main(void)
{
    string text = get_string("Text:");
    int letters =count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    printf("Letters: %i \n", letters);
    printf("Words: %i \n", words);
    printf("Sentences: %i \n", sentences);
    int index= round(cli(letters, words, sentences));
    if (index < 1){
        printf("Before Grade 1\n");
    }else if (index>16){
        printf("Grade 16+\n");
    }else{
        printf("Grade %i\n",index);
    }
}

