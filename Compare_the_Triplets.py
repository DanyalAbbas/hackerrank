a = [1, 2, 3]
b = [3, 2, 1]

def foo(a : list, b : list):
    values = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            values[0] += 1
        elif b[i] > a[i]:
            values[1] += 1
    return values

print(foo(a,b))


