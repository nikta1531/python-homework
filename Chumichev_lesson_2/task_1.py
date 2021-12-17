# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
print('Выяснить тип результата выражений:')
a = 15 * 3
print('15 * 3')
print(type(a))
print(isinstance(a, int))

b = 15 / 3
print('15 / 3')
print(type(b))
print(isinstance(b, float))

c = 15 // 2
print('15 // 2')
print(type(c))
print(isinstance(c, int))

e = 15 ** 2
print('15 ** 2')
print(type(e))
print(isinstance(e, int))