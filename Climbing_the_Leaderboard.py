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
    ranked = list(set(ranked))
    for i in player:
        ranked.append(i)
        ranked.sort(reverse=True)
        New_Rank.append(ranked.index(i)+1)
    return New_Rank
    

print(foo(ranked, player))
print(bar(ranked, player))