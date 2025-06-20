A = ["father", "dog", "mother", "apple", "car", "samsung", "cola", "calc"]
C = 'c'

count = sum(1 for s in A if len(s) > 1 and s.startswith(C) and s.endswith(C))

print(f"Количество подходящих элементов: {count}")