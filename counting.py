def count(arr):
    sizee = len(arr)
    output = [0] *sizee

    count =  [0]*10

    for _ in range(0, sizee):
        count[arr[_]] +=1 
    
    for _ in range(1, 10):
        count[_] += count[_ - 1]

    _ = sizee - 1 
    while _>=0:
        output[count[arr[_]] - 1] = arr[_]
        count[arr[_]] -=1
        _ -= 1
    
    for _ in range(0, sizee):
        arr[_] = output[_]

    return arr

data = [5, 6, 8, 1, 5, 5, 7]
data = count(data)

print(data)

