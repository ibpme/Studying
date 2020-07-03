from cs50 import get_string

def main():
    text = get_string("Text: ")
    letters=count_letters(text)
    words=count_words(text)
    sentences=count_sentences(text)
    print("Letters:",letters)
    print("Words:",words)
    print("Sentences",sentences)
    index= int(cli(letters,words,sentences))
    if index<1:
        print("Before Grade 1")
    elif index>16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

def count_letters(string):
    text_length = len(string)
    letters=1
    for i in range(text_length):
        if string[i].isalpha():
            letters +=1
    return letters

def count_words(string):
    text_length = len(string)
    space=1
    for i in range(text_length):
        if string[i]==' ':
            space +=1
    return space

def count_sentences(string):
    text_length = len(string)
    periods=0
    for i in range(text_length):
        if string[i] in ['?','!','.']:
            periods +=1
    return periods

def cli(l,w,s):
    L=l*100/w
    S=s*100/w
    index=0.0588 * L - 0.296 * S - 15.8
    return index

if __name__=='__main__':
    main()