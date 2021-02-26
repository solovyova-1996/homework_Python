# __author__* Соловьева Дарья Викторовна
# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор. Например:
# gen1 = iterator_without_yield(11)
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


def gen_odd_number(n):
    gen = (num for num in range(1, (n + 1), 2))
    return gen


gen1 = gen_odd_number(5)


# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# Усложнение(*):
# Без использования ключевого слова yield: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
def gen_odd_number_square(n):
    for num in range(n):
        if num ** 2 >= 200:
            n = num
            break

    gen = (num for num in range(1, n, 2))

    return gen


gen2 = gen_odd_number_square(14)
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
print(next(gen2))
print(next(gen2))
