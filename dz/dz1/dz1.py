#ДЗ 1

#Задача 1. Ручной счёт.
import math

approx_value = 3.14
exact_value = math.pi
absolute_error = abs(approx_value - exact_value)
relative_error = absolute_error / abs(exact_value) * 100
print("Задача №1 1.1")
print(f"{absolute_error:.5f}")
print(f"{relative_error:.4f}%")


approx_value = 2.718
exact_value = math.e
absolute_error = abs(approx_value - exact_value)
relative_error = absolute_error / abs(exact_value) * 100
print("Задача №1 1.2")
print(f"{absolute_error:.5f}")
print(f"{relative_error:.4f}%")


approx_value = 9.8
exact_value = 9.81
absolute_error = abs(approx_value - exact_value)
relative_error = absolute_error / abs(exact_value) * 100
print("Задача №1 1.3")
print(f"{absolute_error:.5f}")
print(f"{relative_error:.4f}%")


approx_value = 0.333
exact_value = 1/3
absolute_error = abs(approx_value - exact_value)
relative_error = absolute_error / abs(exact_value) * 100
print("Задача №1 1.4")
print(f"{absolute_error:.5f}")
print(f"{relative_error:.4f}%")

# Вывод:
# 0.00028 (2) --> 0.00033 (4) --> 0.00159 (1) --> 0.01000 (3)
# абсолютная погрешность от самого точного к самому неточному: 2, 4, 1, 3
# 0.0104% (2) --> 0.0507% (1) -->  0.1000% (4) --> 0.1019% (3) 
# относительная погрешность от самого точного к самому неточному: 2, 1, 4, 3 
# Порядки не совпадают, потому что абсолютная погрешность показывает, насколько мы ошиблись, 
# а относительная - насколько эта ошибка велика по сравнению с самим числом. 
# Поэтому одна и та же ошибка для маленького числа будет более значительной, чем для большого.


# Задача 2. Сравнение несопоставимых величин.
import math

approx_value = 1247
exact_value = 1250
absolute_error = abs(approx_value - exact_value)
relative_error = absolute_error / abs(exact_value) * 100
print("Задача №2 2.1")
print(f"{absolute_error:.4f}")
print(f"{relative_error:.4f}%")

approx_value = 9.7
exact_value = 10
absolute_error = abs(approx_value - exact_value)
relative_error = absolute_error / abs(exact_value) * 100
print("Задача №2 2.2")
print(f"{absolute_error:.4f}")
print(f"{relative_error:.4f}%")

# Вывод:
# По абсолютной погрешности сильнее ошиблись при измерении моста:
# 3 м = 3000 мм, а у болта погрешность 0.3 мм.
# По относительной погрешности сильнее ошиблись при измерении болта:
# 3% у болта и 0.24% у моста.
# Относительная погрешность учитывает, насколько ошибка велика
# по сравнению с самой измеряемой величиной.


# Задача 3. Функция relative_error.
import math
def relative_error(approx, exact):
    if exact == 0:
        return float('inf')

    return abs(approx - exact) / abs(exact)

# Задача 3.1 Число Пи
result = relative_error(3.14, math.pi)
print(f"3.1. Относительная погрешность: {result * 100:.4f}%")

# Задача 3.2 Число e
result = relative_error(2.718, math.e)
print(f"3.2. Относительная погрешность: {result * 100:.4f}%")

# Задача 3.3 Ускорение свободного падения
result = relative_error(9.8, 9.81)
print(f"3.3. Относительная погрешность: {result * 100:.4f}%")

# Задача 3.4 Дробь 1/3
result = relative_error(0.333, 1/3)
print(f"3.4. Относительная погрешность: {result * 100:.4f}%")


# Вывод:
# Для всех четырёх пар получились те же значения, что и в задаче 1.
# Если точное значение равно нулю, функция возвращает inf.


# Задача 4. Обратная задача - оценка точного значения.
import math
approx_value = 47.3
relative_error_limit = 0.1 / 100

# Вычисляем границы интервала
lower_bound = approx_value / (1 + relative_error_limit)
upper_bound = approx_value / (1 - relative_error_limit)

# Округляем нижнюю границу вниз, а верхнюю вверх
lower_bound = math.floor(lower_bound * 10_000) / 10_000
upper_bound = math.ceil(upper_bound * 10_000) / 10_000

print(f"Нижняя граница: {lower_bound:.4f}")
print(f"Верхняя граница: {upper_bound:.4f}")
print(f"Интервал: [{lower_bound:.4f}, {upper_bound:.4f}]")

# Вывод:
# Границы получились из неравенства |47.3 - x*| <= 0.001 * |x*|.
# После округления точное значение лежит в интервале [47.2527, 47.3474].


# Задача 5. Порог по абсолютной и относительной ошибке.
absolute_error_A = 0.3
relative_error_B = 0.5 / 100

# Находим порог температуры
temperature_limit = absolute_error_A / relative_error_B

print(f"Порог температуры: {temperature_limit:.1f}C")
# Датчик B не уступает A при |T| <= 60.0C

temperatures = [10, 30, 60, 80, 100]

for T in temperatures:
    error_B = abs(T) * relative_error_B
    print(f"T = {T}C, погрешность B = {error_B:.3f}C")

    if error_B < absolute_error_A:
        print("Датчик B точнее")
    elif error_B == absolute_error_A:
        print("Датчики одинаковы по границе погрешности")
    else:
        print("Датчик A точнее")

# Вывод:
# При -60 <= T <= 60C погрешность датчика B не превышает 0.3C.
# При |T| < 60C датчик B имеет меньшую границу погрешности.
# При |T| = 60C границы погрешности одинаковы.
# При |T| > 60C датчик A имеет меньшую границу погрешности.
# Выбор датчика зависит от диапазона температур,
# поскольку абсолютная погрешность B растёт с увеличением |T|.


# Задача 6. Подсчёт значащих цифр

# 1. 0.004520 - 4 значащие цифры: 4.520e-03
# 2. 1200 - 2 значащие цифры: 1.2e+03
# 3. 1.200 - 4 значащие цифры: 1.200e+00
# 4. 10.03 - 4 значащие цифры: 1.003e+01
# 5. 0.03050 - 4 значащие цифры: 3.050e-02
# 6. 250000 - 2 значащие цифры: 2.5e+05

# Вывод:
# Числа 1200 и 250000 имеют неоднозначное количество
# значащих цифр, поскольку неизвестно, являются ли
# конечные нули значащими.
# Для чисел 1200 и 250000 мы приняли 2 значащие цифры.
# Экспоненциальная форма позволяет однозначно
# указать количество значащих цифр.


# Задача 7. Честная запись результата

x = 4.738291
delta = 0.02

# Округляем значение до разряда погрешности
rounded_x = round(x, 2)

print(f"Результат: {rounded_x:.2f} +- {delta:.2f}")
# Количество значащих цифр: 3

# Вывод:
# Результат измерения: 4.74 +- 0.02.
# После округления осталось 3 значащие цифры.
# Запись 4.738291 +- 0.02 некорректна, поскольку
# содержит лишние цифры, не соответствующие точности измерения.


# Задача 8. Округление и banker's rounding

print(round(0.5), round(1.5), round(2.5), round(3.5),
      round(-0.5), round(-1.5), round(-2.5))

import random
import math

# Создаём миллион случайных чисел
numbers = [random.randint(0, 9) + 0.5 for _ in range(10**6)]

# Сумма после banker's rounding
bankers_sum = sum(round(x) for x in numbers)

# Сумма после округления вверх
up_sum = sum(math.floor(x + 0.5) for x in numbers)

# Накопленный сдвиг
difference = up_sum - bankers_sum

print(f"Сумма banker's rounding: {bankers_sum}")
print(f"Сумма округления вверх: {up_sum}")
print(f"Накопленный сдвиг: {difference}")

# Вывод:
# Python при точном значении .5 округляет к ближайшему
# чётному целому числу.
# При округлении половин всегда вверх возникает
# систематическое завышение суммы.
# Для миллиона чисел ожидаемый сдвиг составляет 500000.
# В финансовых расчётах это важно, поскольку ошибки
# округления могут накапливаться при большом числе операций.



# Задача 9. Промежуточное округление

import math

# Создаём список слагаемых
numbers = [1 / k for k in range(1, 101)]

# Эталонная сумма
S_exact = math.fsum(numbers)

# Вариант (а) - без промежуточного округления
S_a = sum(numbers)

# Вариант (б) - округляем каждое слагаемое
S_b = sum(round(x, 3) for x in numbers)

# Абсолютные погрешности
delta_a = abs(S_a - S_exact)
delta_b = abs(S_b - S_exact)

# Относительные погрешности
relative_a = delta_a / abs(S_exact)
relative_b = delta_b / abs(S_exact)

print(f"Эталон: {S_exact:.15f}")
print(f"Вариант (а): {S_a:.15f}")
print(f"Вариант (б): {S_b:.15f}")

print(f"Абсолютная погрешность (а): {delta_a:.12g}")
print(f"Абсолютная погрешность (б): {delta_b:.12g}")

print(f"Относительная погрешность (а): {relative_a:.12g}")
print(f"Относительная погрешность (б): {relative_b:.12g}")

# Во сколько раз ошибка (б) больше
if delta_a != 0:
    ratio = delta_b / delta_a
    print(f"Ошибка (б) больше примерно в {ratio:.2e} раз")
else:
    print("Отношение ошибок не определено, так как ошибка (а) равна нулю")



# Вывод:
# Промежуточное округление увеличивает погрешность,
# так как ошибки накапливаются при суммировании.
# Правило: округлять следует только конечный результат,
# сохраняя максимальную точность промежуточных вычислений.
# На Python 3.14.7 сумма без промежуточного округления
# совпала с math.fsum(), поэтому отношение ошибок не определено.



# Задача 10. Классика 0.1 + 0.2

import math

a = 0.1 + 0.2
b = 0.3

print(f"0.1 + 0.2 = {a}")

# Сравнение чисел
print(f"Сравнение через ==: {a == b}")
print(f"Сравнение через math.isclose: {math.isclose(a, b)}")

# Абсолютная погрешность
delta = abs(a - b)

# Относительная погрешность
relative_error = delta / abs(b)

print(f"Абсолютная погрешность: {delta:.16e}")
print(f"Относительная погрешность: {relative_error:.16e}")

# Вывод:
# Компьютер хранит дробные числа в двоичной системе,
# и число 0.1 невозможно записать в ней точно конечным числом цифр.
# Поэтому компьютер сохраняет ближайшее доступное значение.
# При сложении таких чисел возникают небольшие погрешности,
# из-за которых 0.1 + 0.2 не равно точно 0.3.


# Задача 11. Катастрофическая потеря точности

a = 1 + 10**(-15)
b = 1

expected = 10**(-15)
actual = a - b

# Вычисляем относительную погрешность
relative_error = abs(actual - expected) / abs(expected)

print(f"Ожидаемый результат: {expected:.16e}")
print(f"Фактический результат: {actual:.16e}")
print(f"Относительная погрешность: {relative_error:.6%}")

import math

a = 1
b = 10**8
c = 1

D = b**2 - 4*a*c

# Обычная формула для меньшего по модулю корня
x_small_old = (-b + math.sqrt(D)) / (2*a)

# Вычисляем большой по модулю корень
x_large = (-b - math.sqrt(D)) / (2*a)

# Устойчивая формула для меньшего корня
x_small_new = c / (a*x_large)

# Сравниваем с обычной формулой
difference = abs(x_small_old - x_small_new)
relative_difference = difference / abs(x_small_new)

print(f"Обычная формула: {x_small_old:.16e}")
print(f"Устойчивая формула: {x_small_new:.16e}")
print(f"Разница: {difference:.16e}")
print(f"Относительное расхождение: {relative_difference:.2%}")

from decimal import Decimal, localcontext

# Вычисляем эталон с повышенной точностью
with localcontext() as context:
    context.prec = 60
    x_reference = -2 * Decimal(c) / (Decimal(b) + Decimal(D).sqrt())

    # Сравниваем оба результата с эталоном
    error_old = abs(Decimal.from_float(x_small_old) - x_reference)
    error_new = abs(Decimal.from_float(x_small_new) - x_reference)
    error_ratio = error_old / error_new

print(f"Ошибка обычной формулы: {error_old:.16e}")
print(f"Ошибка устойчивой формулы: {error_new:.16e}")
print(f"Устойчивая формула даёт ошибку меньше в {error_ratio:.2e} раз")

# Вывод:
# При вычитании близких чисел возникает потеря точности
# из-за ошибок округления при работе с float.
# В первом эксперименте относительная погрешность
# составила примерно 11.02%.
# При решении квадратного уравнения обычная формула
# даёт заметную ошибку для меньшего по модулю корня.
# Использование формулы Виета позволяет избежать
# вычитания близких чисел и повысить точность вычислений.
# Для меньшего по модулю корня ошибка уменьшилась
# примерно в 3.22e15 раз.


# Задача 12. Накопление ошибки в цикле

import math

arr = [0.1] * 1_000_000
exact = 1e5

# Способ 1 - обычный цикл
total = 0.0

for x in arr:
    total += x

# Способ 2 - встроенная функция sum()
sum_result = sum(arr)

# Способ 3 - функция math.fsum()
fsum_result = math.fsum(arr)

# Сравниваем результаты
results = [
    ("Цикл for", total),
    ("sum()", sum_result),
    ("math.fsum()", fsum_result)
]

# Выводим таблицу
print(f"{'Способ':<15} {'Сумма':<22} {'Абс. ошибка':<18} {'Отн. ошибка':<18}")
print("-" * 75)

for name, value in results:
    absolute_error = abs(value - exact)
    relative_error = absolute_error / abs(exact)

    print(f"{name:<15} {value:<22.12f} {absolute_error:<18.12g} {relative_error:<18.12g}")


# Вывод:
# При сложении миллиона чисел 0.1 обычным циклом
# накапливается погрешность из-за ограниченной точности float.
# На Python 3.14.7 sum() и math.fsum() получили
# результат без погрешности относительно эталона 100000.
# Поэтому определить, во сколько раз они точнее, 
# через деление погрешностей невозможно.
# Для более точного суммирования рекомендуется math.fsum().


# Задача 13. Суммирование в правильном порядке

import math

small = [1e-10] * 500_000
large = [1e6] * 500_000

# Вариант (а) - сначала маленькие, потом большие
arr_a = small + large

# Вариант (б) - сначала большие, потом маленькие
arr_b = large + small

# Вычисляем суммы обычным циклом
total_a = 0.0
for x in arr_a:
    total_a += x

total_b = 0.0
for x in arr_b:
    total_b += x

# Эталонная сумма
exact = math.fsum(arr_a)

# Абсолютные погрешности
error_a = abs(total_a - exact)
error_b = abs(total_b - exact)

print(f"Эталон: {exact:.12f}")
print(f"Сначала маленькие: {total_a:.12f}")
print(f"Сначала большие: {total_b:.12f}")

print(f"Ошибка (а): {error_a:.12e}")
print(f"Ошибка (б): {error_b:.12e}")

# Вывод:
# Порядок суммирования влияет на точность вычислений.
# При сложении сначала маленьких чисел погрешность
# относительно math.fsum() оказалась равна нулю.
# При сложении сначала больших чисел погрешность
# составила примерно 6.1e-05.
# Маленькие числа могут теряться при прибавлении
# к большой сумме из-за ограниченной точности float.
# Поэтому при обычном суммировании лучше начинать
# с меньших по модулю чисел.


# Задача 14. Детектор накопления погрешности

import math
import matplotlib.pyplot as plt

x = 1.0
factor = 1.0001

steps = []
errors = []

# Пороги относительной погрешности
thresholds = [1e-9, 1e-6, 1e-3]
first_exceed = {t: None for t in thresholds}

# Эксперимент с ростом
for n in range(1, 10_001):
    x *= factor

    # Эталон на текущем шаге
    reference = math.exp(n * math.log(factor))

    # Относительная погрешность
    relative_error = abs(x - reference) / abs(reference)

    steps.append(n)
    errors.append(relative_error)

    # Проверяем превышение порогов
    for t in thresholds:
        if first_exceed[t] is None and relative_error > t:
            first_exceed[t] = n

# Итоговый результат
final_reference = math.exp(10000 * math.log(factor))

print(f"Результат цикла: {x:.15f}")
print(f"Эталон: {final_reference:.15f}")
print(f"Относительная погрешность: {errors[-1]:.12e}")

# Выводим шаги превышения порогов
for t in thresholds:
    if first_exceed[t] is None:
        print(f"Порог {t:.0e} не превышен")
    else:
        print(f"Порог {t:.0e} превышен на шаге {first_exceed[t]}")

# Строим график
plt.plot(steps, errors)
plt.xlabel("Номер шага")
plt.ylabel("Относительная погрешность")
plt.title("Накопление погрешности при умножении")
plt.grid(True)
plt.show()

# Вывод:
# При многократном умножении накапливаются ошибки округления.
# За 10000 шагов относительная погрешность достигла
# примерно 1e-14, но не превысила пороги
# 1e-9, 1e-6 и 1e-3.
# График показывает, что погрешность растёт неравномерно,
# иногда увеличиваясь, а иногда уменьшаясь.
# В данном эксперименте накопление ошибки происходит
# медленно, однако в других мультипликативных
# процессах погрешность может расти быстрее.


# Задача 15. Финансы: float vs Decimal

from decimal import Decimal, getcontext

# Устанавливаем точность Decimal
getcontext().prec = 28

n = 1_000_000

# Способ 1 - float
total_float = 0.0

for _ in range(n):
    total_float += 0.01

# Способ 2 - Decimal
total_decimal = Decimal("0.00")

for _ in range(n):
    total_decimal += Decimal("0.01")

# Способ 3 - целые копейки
total_kopecks = 0

for _ in range(n):
    total_kopecks += 1

total_int = Decimal(total_kopecks) / Decimal(100)

# Сравниваем с точным результатом
exact = Decimal("10000.00")

# Расхождение float и Decimal
difference = abs(Decimal.from_float(total_float) - total_decimal)
relative_difference = difference / exact * 100

print(f"Float: {total_float:.15f}")
print(f"Decimal: {total_decimal}")
print(f"Целые копейки: {total_int}")

print(f"Расхождение в рублях: {difference}")
print(f"Расхождение в процентах: {relative_difference:.12f}%")

# Вывод:
# При миллионе начислений по 0.01 рубля float
# накопил небольшую погрешность.
# Расхождение составило примерно 1.72e-7 рубля,
# или 0.000000001719%.
# Decimal и int получили точный результат 10000 рублей.
# В финансовых расчётах лучше использовать Decimal
# или целые копейки, поскольку float не может точно
# представлять многие десятичные дроби.