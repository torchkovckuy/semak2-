def is_decreasing(n):
    s=str(n)
    return all(s[i] > s[i+1] for i in range(len(s)-1))
print(is_decreasing(9852))