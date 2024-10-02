arr = [  [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]   ]


def foo(arr : list[int]) -> int:
    add1 = 0
    add2 = 0
    for i in range(len(arr)):
        add1 += arr[i][i]
        add2 += arr[i][len(arr)-1-i]
    
    return abs(add1 - add2)


print(foo(arr))