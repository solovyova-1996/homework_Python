numbers = [1, 2,6, 5, 8,4]
print(sorted(numbers))
print(sorted(numbers, reverse = True))
cities = [("Москва", 1000), ("Лас- Вегас", 500), ("Антверпен",20000)]
print(sorted(cities))
def by_cont(city):
    return city[1]
print(sorted(cities, key = by_cont))
print(sorted(cities, key = lambda city: city[1]))
number = (1, 2,6, 5, 8,4)
def is_even(number):
    return number % 2 == 0
result = filter(is_even,number)
result = list(result)
print(result)
numb = [1, 2,6, 5, 8,4]
print(list(map(lambda x: x**2, numb)))
print(list(map(lambda x: str(x), numb)))