n = 4

def foo(n : int):
    for i in range(1, n+1):
        print(" "*(n-i) + "#"*i)


foo(n)