def Fibonacci(n):
        a = [1,1]
        b = int()
        for i in range (1,n):
                b = a[i] + a[i-1]
                a.append(b)
        return a[n - 1]

a = int(input())
a = Fibonacci(a)
print(a)