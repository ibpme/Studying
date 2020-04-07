def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)
def sumto(n):
    e=0
    for i in range(n):
        e+=(1/fact(i))
    print(e)


    
        
    

