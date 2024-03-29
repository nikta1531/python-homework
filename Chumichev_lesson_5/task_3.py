# Task 3
# Есть два списка:
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо
# вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))

from itertools import zip_longest

gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)
print(next(gen))
