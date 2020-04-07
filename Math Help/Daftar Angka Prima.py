def prima(p): # fungsi ini menguji apabila angka p itu prima 
    k=0
    if p==1:
        return 0
    for i in range(2,int(p)):
        if(p%i==0):
            k+=1
    if(k<=0):
        return 1 #angka tersebut prima
    else:
        return 0 #angka tersebut bukan prima

def main():
    j=0
    a=int(input("Masukan A:"))
    b=int(input("Masukan B:"))
    for n in range (a,b+1):
        if prima(n) == 1 :
            j+=1
            print(n)
    print("total="+str(j))
while True:
    main()
