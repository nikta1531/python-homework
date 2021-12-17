# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Минуты в секундах, часы в секундах, дни в секундах и т.д.
tm_min = 60
tm_hour = 3600
tm_mday = 86400
tm_wday = 604800
tm_mon = 2678400
tm_year = 31536000

duration = int(input('Реализовать вывод информации\nо промежутке времени в зависимости от\nего продолжительности duration в секундах: '))

# a. до минуты: <s> сек;
if duration < tm_min:
    print(duration, 'сек')

# b. до часа: <m> мин <s> сек;
elif tm_min <= duration and tm_hour > duration:
    minute = duration // tm_min
    second = duration % tm_min
    print(minute, 'мин', second, 'сек')

# c. до суток: <h> час <m> мин <s> сек;
elif duration >= tm_hour and duration < tm_mday:
    hour = duration // tm_hour
    duration = duration % tm_hour
    minute = duration // tm_min
    second = duration % tm_min
    print (hour, 'час', minute, 'мин', second, 'сек')

# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
elif duration >= tm_mday and duration < tm_wday:
    day = duration // tm_mday
    duration = duration % tm_mday
    hour = duration // tm_hour
    duration = duration % tm_hour
    minute = duration // tm_min
    second = duration % tm_min
    print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')

# конец задания