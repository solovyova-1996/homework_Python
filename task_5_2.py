# __author__* Соловьева Дарья Викторовна
# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя
# ключевое слово yield. Полностью истощить генератор. Например:
# gen1 = iterator_with_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
def gen_odd_number_yield(n):
    for num in range(1, (n + 1), 2):
        yield num


gen1 = gen_odd_number_yield(10)


# print(list(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
def gen_odd_number_yield1(n):
    for num in range(1, (n + 1), 2):
        if num ** 2 < 200:
            yield num


gen2 = gen_odd_number_yield1(100)
print(list(gen2))


# Усложнение(**):
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму
# этого и предыдущих чисел. Например:
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
def gen_odd_number_yield2(n):
    sum = 0
    for num in range(1, (n + 1), 2):
        if num ** 2 < 200:
            sum = sum + num
            yield num, sum


gen2 = gen_odd_number_yield2(100)
# print(list(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
