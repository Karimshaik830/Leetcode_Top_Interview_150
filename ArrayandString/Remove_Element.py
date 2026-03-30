def remove(arr,val):
    k=0
    for i in range(len(arr)):
        if arr[i]!=val:
            arr[k]=arr[i]
            k+=1
    return k
arr=[2,2,3,3]
val=2
k=remove(arr,val)
print(arr[:k])