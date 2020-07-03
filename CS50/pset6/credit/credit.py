from cs50 import get_int,get_string

number = get_string("Number: ")

validation=[]
for string in range(len(number),2):
    validation.append(int(number[string])*2)
for num in range(len(validation)):
    if validation[num]>=10:
        validation[num] %=10
        validation.append(1)
output=sum(validation)
for string in range(1,len(number),2):
    output += int(number[string])

print(output)

if output%10 ==0:
    print("Valid")
else:
    print("Not Valid")

