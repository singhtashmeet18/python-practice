def fibo(n):                                                           #FIBONACCI SERIES
    if (type(n) is not int):
        return"invalid value!! enter a valid value"

    if n < 0:
        return"invalid value!! enter a valid value"

    if n <= 1:
        fib_list = [0]
    elif n==2:
        fib_list = [0,1]


    else:
        a,b = 0,1
        fib_list = [0,1]
        for i in range (2,n):
            c = a + b
            fib_list.append(c)
            a,b = b,c
            return fib_list

resp = fibo(5)
print(resp)


