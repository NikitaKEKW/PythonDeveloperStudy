# 1. Что подразумевается под «упаковкой (packing)» в Python и как она реализуется?
# В контексте Python термин "упаковка" (packing) относится к процессу, при котором значения
# собираются в структуру данных, такую как кортеж (tuple) или список (list). Упаковка позволяет
# создавать структуры данных из нескольких элементов, которые могут быть обработаны как единое целое.
# Упаковка
my_cortezh = 1, 2, 3

# Распаковка
a, b, c = my_cortezh

print(a)  # Вывод: 1
print(b)  # Вывод: 2
print(c)  # Вывод: 3
