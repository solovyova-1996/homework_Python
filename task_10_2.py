# __author__Соловьева Дарья Викторовна
# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC


class Clothes(ABC):
    summ_tissue = 0


class Coat(Clothes):

    def __init__(self, v):
        self.v = v
        Clothes.summ_tissue += Coat.tissue_consumption(self)

    def tissue_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, h):
        self.h = h
        Clothes.summ_tissue += Costume.tissue_consumption(self)

    def tissue_consumption(self):
        return 2 * self.h + 0.3


coat1 = Coat(7)
print(coat1.tissue_consumption())
coat2 = Coat(9)
print(coat2.tissue_consumption())
costume1 = Costume(16)
print(costume1.tissue_consumption())
costume2 = Costume(9)
print(costume2.tissue_consumption())

print(Clothes.summ_tissue)
