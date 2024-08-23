def caching_fibonacci():
    cache = {}
    def fibonacchi(n):
        if n<= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n]= fibonacchi(n-1) + fibonacchi(n-2)
        return cache[n]
    return fibonacchi


fib = caching_fibonacci()

print(fib(10)) 
print(fib(15))  