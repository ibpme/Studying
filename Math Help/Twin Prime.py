def prima(p): # fungsi ini menguji apabila angka p itu prima 
    k=0
    if p==1:
        return 0
    for i in range(2,int(p)):
        if(p%i==0):
            k+=1
    if p>=1000 :
        if (p%2==0):
            return 0
        for i in range(3,int((pow(p,0,5)//1)+2),2):
            if(p%i==0):
                k+=1
    if(k<=0):
        return 1 #angka tersebut prima
    else:
        return 0 #angka tersebut bukan prima

def twin(x):
    if (prima(x)==1 and (prima(x+2)==1)):
        return 1

def main():
    j=0
    a=int(input("Masukan A:"))
    b=int(input("Masukan B:"))
    for n in range (a,b+1):
        if twin(n) == 1 :
            j+=1
            print(n,n+2)
    print("total="+str(j))
while True:
    main()
