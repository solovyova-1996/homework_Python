# __author__* Соловьева Дарья Викторовна
# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses
# меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
#
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких
# ситуациях генератор даст эффект.

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Александр']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def gen_tutor_klasses(tutors, klasses):
    while len(tutors) > 0:
        tutors_el = tutors.pop(0)
        klasses_el = klasses.pop(0) if len(klasses) > 0 else None
        yield tutors_el, klasses_el


gen1 = gen_tutor_klasses(tutors, klasses)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
