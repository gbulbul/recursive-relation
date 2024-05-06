def Fibonacci(n, k):

    if n < 0:

        print("Incorrect input")

    elif n == 0:

        return 0

    elif n == 1:

        return 1
        
    elif n == 2: 
        
        return k

    elif n <=4:
        
        return Fibonacci(n-1,k) + Fibonacci(n-2,k)
    
    else: 
        
        return Fibonacci(n-1,k) + Fibonacci(n-2,k)*k


print(Fibonacci(5, 3))
