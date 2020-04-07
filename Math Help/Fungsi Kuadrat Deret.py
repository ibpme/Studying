def fungsikuadrat():
    print("A=")
    A=float(input())
    print("B=")
    B=float(input())
    print("C=")
    C=float(input())
    print("Masukan Hingga n")
    n=int(input())
    for i in range(0,n):
        print(str(A*pow(i,2)+B*i+C))
while True:
    fungsikuadrat()
