# Вася использует в своей программе очень много различных математических вычислений, связанных с фигурами.
# Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным количеством функций,
# он решил выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем math.
#
# Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):
#
# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.
# Пример основного кода:
#
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)
# Результат:
#
# 31.41592653589793
#
# 113.09733552923255


from math import pi


class MyMath:
    @classmethod
    def circle_len(cls, radius):
        return f"Длина окружности: {2 * pi * radius}"

    @classmethod
    def circle_sq(cls, radius):
        return f"Площадь окружности: {pi * radius ** 2}"

    @classmethod
    def cube_vol(cls, radius):
        return f"Объем куба, зная только радуис вписанной окружности: {(radius * 2) ** 3}"

    @classmethod
    def sphere_surface_sq(cls, radius):
        return f"Площвдь поверхности сферы: {4 * pi * radius ** 2}"


# obj1 = MyMath()
# var = obj1.circle_sq(radius=15)
# print(var)
res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
