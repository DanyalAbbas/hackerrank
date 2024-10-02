def BinarySearch(rank, sc):
    start, end = 0, len(rank) -1

    while start <= end:
        middle = (start + end)// 2
        if rank[middle] == sc:
            return middle
        elif rank[middle] < sc:
            end = middle -1
        else:
            start = middle + 1

    return start
ranked = [100,90,90,80]
player = [70,80,105]

def foo(ranked : list, player : list) -> list:
    CollectiveList = ranked + player
    CollectiveList = list(set(CollectiveList))
    CollectiveList.sort(reverse=True)
    print(CollectiveList)
    return [CollectiveList.index(i)+1 for i in player]

def bar(ranked : list, player : list) -> list:
    New_Rank =[]
    ranked = sorted(list(set(ranked)), reverse=True)
    for i in player:
        ranked.append(i)
        ranked.sort(reverse=True)
        New_Rank.append(ranked.index(i)+1)
    return New_Rank


def climbingLeaderboard(ranked, player):

    ranked = list(set(ranked))
    ranked = sorted(ranked, reverse= True)
    res = []
    index = 0
    for i in player:
        index = BinarySearch(ranked, i)
        res.append(index +  1)


    return res

    

print(foo(ranked, player))
print(bar(ranked, player))
print(climbingLeaderboard(ranked, player))