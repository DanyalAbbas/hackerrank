arr = [1,1,0,-1,-1]

def foo(arr : list[int]):
    Positive = 0
    Zero = 0
    Negative = 0
    for i in arr:
        if i > 0:
            Positive += 1
        elif i < 0:
            Negative += 1
        else:
            Zero += 1
    print(Positive/len(arr))
    print(Negative/len(arr))
    print(Zero/len(arr))

foo(arr)