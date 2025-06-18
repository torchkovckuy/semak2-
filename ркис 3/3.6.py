def prod_add(arr):
    p=1
    for i in range(0, len(arr), 2):
        p*=arr[i]
    return p
print(prod_add([1,2,3,4,5]))