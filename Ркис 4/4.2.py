arr=[int(input(f"Введите элемент {i+1}:")) for i in range(14)]
arr.append(sum(arr))
for num in arr:
    print(num, end=" ")