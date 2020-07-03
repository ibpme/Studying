import csv
import sys

if len(sys.argv) != 3:
    print("usage error, dna.py sequence.txt database.csv")
    sys.exit()

# read the dna sequence from the file
with open(sys.argv[2]) as dnafile:
    sequence = dnafile.readline()

# extract the sequences from the database into a list

with open(sys.argv[1]) as databasefile:
    database = csv.reader(databasefile)
    for STR in database:
        dnaSequences = STR
        break
    dnaSequences.pop(0)

countSequences={}

for STR in dnaSequences:
    countSequences[STR]=1

for genes in dnaSequences:
    genes_len=len(genes)
    count=0
    countMax=0

    for i in range(len(sequence)):
        while count>0:
            count -=1
            continue

        if sequence[i:i+genes_len]== genes:
            while sequence[i-genes_len:i]==sequence[i:i+genes_len]:
                count+=1
                i+=genes_len

            if count>countMax:
                countMax = count

    countSequences[genes]+=countMax

with open(sys.argv[1],newline='') as peoplefile:
    people = csv.DictReader(peoplefile)
    for person in people:
        match = 0
        # compares the sequences to every person and prints name before leaving the program if there is a match
        for dna in countSequences:
            if countSequences[dna] == int(person[dna]):
                match += 1
        if match == len(countSequences):
            print(person['name'])
            exit()

    print("No match")


