import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import ConnectionPatch
from matplotlib.patches import FancyArrowPatch

points = []
# Запись данных

for i in range(4):
    print("Добро пожаловать на полигон")
    x = float(input(f"Введите Широту данные для полигона {i+1}: "))
    y = float(input(f"Ведите Долгату данные для полигона {i+1}: "))
    points.append((x, y))

# Расстояние между линиями (переменная pos):
pos = float(input("Введите размеры: "))

# Декомпозиция
rectangle = plt.Polygon(points, closed=True, fill=None)

# Отрисовка
fig, ax = plt.subplots()
ax.add_patch(rectangle)

# Координаты для отрисовки
x_coords, y_coords = zip(*points)
x_min, x_max = min(x_coords), max(x_coords)
y_min, y_max = min(y_coords), max(y_coords)

# отрисовка линий по вертикали
for x in np.arange(x_min, x_max, pos):
    if (pos >= x_min and pos <= x_min):
        print("error")
        break
    if x_min <= x <= x_max:
        ax.add_line(Line2D([x+1, x+1], [y_min, y_max], color='blue'))
    else:
        print("error")

    
    # отрисовка линий по горизонтали, смена направления при каждой итераци
    ad = pos
    if (x - x_min) % (2 * pos) == 0:
        arrow = FancyArrowPatch((x+1, y_max), (x+pos+1, y_max), connectionstyle=f"arc3,rad=-{ad}", color="red")
    else:
        arrow = FancyArrowPatch((x+1, y_min), (x+pos+1, y_min), connectionstyle=f"arc3,rad={ad}", color="red")
    ax.add_patch(arrow)

ax.autoscale()
plt.show()

# Установка утилит

# pip install matplotlib

# python3 -m venv venv
# source venv/bin/activate

# Радиус:


# # Задаем переменную pos
# pos = 5  # Пример радиуса

# # Задаем углы для генерации линий
# angles = np.linspace(0, 2*np.pi, 100)

# # Вычисляем координаты точек линий на основе радиуса и угла
# x = pos * np.cos(angles)
# y = pos * np.sin(angles)

# # Визуализируем полученные линии
# plt.plot(x, y)
# plt.axis('equal')
# plt.show()