names = ["Алексей", "Мария", "Анна", "Иван", "Арина", "Дмитрий", "Алиса", "Сергей", "Андрей", "Ольга"]

names_with_a = [name for name in names if name.startswith(('А', 'A'))]

print(names_with_a)