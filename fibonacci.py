def fib(n):
    a,b=1,2
    while a < n:
        print(a, end=" ")
        a,b=b, a+b
    print()
x=input("enter number: ")
fib(int(x))
