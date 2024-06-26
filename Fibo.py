def fibo(n):
    n1 = 0
    n2 =1
    print(n1 ,n2, end=" ")
    n3 = n1+n2

    for i in range(3,n+1):
        print(n3, end=" ")
        n1=n2;
        n2=n3;
        n3 = n1+n2

n = int(input("enter a number :"))
fibo(n)
