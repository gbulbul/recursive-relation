#n = number of generation passed, k= number of offsprings which are allowed/determined in each litter.
class recursionClass:
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
           return recursionClass.Fibonacci(n-1,k) + recursionClass.Fibonacci(n-2,k)
        else: 
           return recursionClass.Fibonacci(n-1,k) + recursionClass.Fibonacci(n-2,k)*k


if __name__=="__main__":
    n,k=5,3
    print(recursionClass.Fibonacci(n,k))
