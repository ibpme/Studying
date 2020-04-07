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
def sp(x):
    s=0
    for i in range(1,x):
        if prima(i)==1:
            s+=(1/pow(i,1))
    print(s)
