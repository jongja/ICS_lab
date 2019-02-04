flag = {1:1, 2:1}
def Fibonacci(n):
    if n == 0:
        return 0
    if n not in flag:
        flag[n] = Fibonacci(n-1) + Fibonacci(n-2)
    return flag[n]
    
print(Fibonacci(50))