# Даны два списка чисел. Посчитайте, сколько различных
# чисел содержится одновременно как в первом списке,
# так и во втором.
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [2, 4, 6, 7, 8, 9]
lst1.extend(lst2)
print(len(set(lst1)))
