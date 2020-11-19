def BubbleSort(list):
    lenn = len(list)

    for _ in range(lenn):
        for __ in range(0, lenn-_-1):
            if list[__]>list[__+1]:
                list[__], list[__+1] = list[__+1], list[__]
            print(list)
    return list

listem = [1,5,9,2,7]

print(listem)
listem = BubbleSort(listem)
print(listem)
