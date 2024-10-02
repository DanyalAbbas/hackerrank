arr = [  [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]   ]


def foo(arr : list[int]) -> int:
    add1 = 0
    add2 = 0
    for pos, i in enumerate(arr):
        add1 += i[pos]
    for pos, i in enumerate(arr[::-1]):
        add2 += i[pos]
    
    return abs(add1 - add2)


print(foo(arr))