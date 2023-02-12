# Практическое задание 5.

import numpy as np
# 1) Когда используется критерий Стьюдента, а когда Z –критерий?

print(f'Ответ 1. \n Критерий Стьюдента используется для сравнения средних значений двух групп. Z-критерий используется для проверки гипотез о нормальности распределения данных.')

# 2) Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр
# оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.

import scipy.stats as stats

z=(17.5-17)/0.2
# print(f'Наблюдаемое значение Z-критерия: {z: .4f}')
zt=stats.norm.ppf(0.95)
# print(f'Табличное значение Z-критерия: {zt: .4f}')
# print(f'Сравним полученные значения: z<zt - {z<zt}')
print(f'Ответ 2. \n Отвергаем нулевую гипотезу H0:u0 = 17 на уровне значимости a=0.05')

# 3) Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?

cookies=np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
tn=(np.mean(cookies)-200)/(np.std(cookies,ddof=1)/len(cookies)**0.5)
# print(f'Наблюдаемое значение t-критерия: {tn: .4f}')

tt=stats.t.ppf(0.995,len(cookies)-1)
# print(f'Табличное значение t-критерия: {tt: .4f}')
# print(f'Сравним полученные значения: np.abs(tn)<tt - {np.abs(tn)<tt}')
print(f'Ответ 3. \n Принимаем нулевую гипотезу H0:u0 = 200 на уровне значимости a=0.01')


# 4) Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160
