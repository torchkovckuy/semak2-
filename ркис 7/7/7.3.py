numbers = [52, -17, 12, 78, -23, 88, 45, 99, -10]
two_digit_pos = sorted([x for x in numbers if 10 <= x <= 99])

print(f"Двузначные положительные числа: {two_digit_pos}")