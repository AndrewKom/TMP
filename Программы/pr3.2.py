from abc import ABC, abstractmethod


class Algorithm(ABC):

    def template_method(self):

        self.flagstock()
        self.draw_1()
        self.draw_2()
        self.draw_3()
        self.final()
        self.printer()

    def flagstock(self):
        print("Флагшток нарисован")

    @abstractmethod
    def draw_1(self):
        pass

    @abstractmethod
    def draw_2(self):
        pass

    @abstractmethod
    def draw_3(self):
        pass

    def final(self):
        print('Флаг готов!')

    def printer(self):
        n = 50
        print("-" * n)

class colors:
    def painwhite(self):
        print("Полоса белого цвета нарисована")

    def painred(self):
        print("Полоса красного цвета нарисована")

    def painblue(self):
        print("Полоса синего цвета нарисована")

    def painblack(self):
        print("Полоса черного цвета нарисована")

    def painyel(self):
        print("Полоса желтого цвета нарисована")

class RussianFlag(Algorithm):
    def draw_1(self):
        z = colors()
        z.painwhite()

    def draw_2(self):
        z = colors()
        z.painblue()

    def draw_3(self):
        z = colors()
        z.painred()

    def final(self):
        print('Флаг России готов!')

class Ger(Algorithm):
    def draw_1(self):
        z = colors()
        z.painblack()

    def draw_2(self):
        z = colors()
        z.painred()

    def draw_3(self):
        z = colors()
        z.painyel()


print("Рисуем флаг России")
a=RussianFlag()
a.template_method()



print("Рисуем флаг Германии")
b=Ger()
b.template_method()

