# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }

def thesaurus(*names):
    dictionary = dict()
    for name in names:
        dictionary.setdefault(name[0], [])
        dictionary[name[0]].append(name)
    return dictionary


print(thesaurus('Ник', 'Nik', 'Кот'))
