"""print(abs(-7))
numbers = [5, 15, 7, 8, -9, 0]
print(max(numbers))
print(min(numbers))
print(round(10.9872, 2))
print(sum(numbers))
winners = ["Leo", "Max", "Kate"]
for number, winner in enumerate(winners,1):
    print(number, winner)

number = []
for i in range(3):
    numb = int(input("Введите число: "))
    number.append(numb)

print(sum(number))
print(max(number))
print(min(number))"""

def get_sep(sep,sep_len):
    return sep * sep_len


sep = get_sep("-", 100)
text = 'Hello {} Func {}'.format(sep,sep)
print(text)