def count_pos(nums):
    return sum(x>0 for x in nums)
print(count_pos([1, -2, 7, 4, 5, 6, 7, -3, -5]))