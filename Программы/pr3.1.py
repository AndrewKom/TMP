import random
from abc import ABC, abstractmethod

class Variant(ABC):
    @abstractmethod
    def selection(self) -> None:
        pass

class Paper(Variant):
    def selection(self) -> str:
        return "Бумага"

class Rock(Variant):
    def selection(self) -> str:
        return "Камень"

class Chik(Variant):
    def selection(self) -> str:
        return "Ножницы"

class Spok(Variant):
    def selection(self) -> str:
        return "Спок"

class Zemnovodnoe(Variant):
    def selection(self) -> str:
        return "Ящерица"


class Random(Variant):
    def selection(self) -> str:
        options = ["Бумага", "Камень", "Ножницы", "Спок", "Ящерица"]
        return random.choice(options)

class Game:
    strategy: Variant

    def __init__(self, strategy: Variant = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec2) -> None:
        s1 = self.strategy.selection()
        s2 = sec2.strategy.selection()
        if s1 == s2:
            print("Ничья!")


        elif s1 == "Камень":
            if s2 == "Ножницы":
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Бумага"):
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Спок"):
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает первый игрок!", s1, '>', s2)



        elif s1 == "Бумага":
            if s2 == "Ножницы":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Камень"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Спок"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "Ножницы":
            if s2 == "Камень":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Бумага"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Спок"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "Спок":
            if s2 == "Бумага":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Камень"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ножницы"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Ящерица"):
                print("Побеждает второй игрок!", s1, '<', s2)


        elif s1 == "Ящерица":
            if s2 == "Ножницы":
                print("Побеждает второй игрок!", s1, '<', s2)
            elif s2 == ("Бумага"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Спок"):
                print("Побеждает первый игрок!", s1, '>', s2)
            elif s2 == ("Камень"):
                print("Побеждает второй игрок!", s1, '<', s2)


def playtime(vibor):
    if vibor == "Бумага":
        return Game(Paper())
    elif vibor == "Ножницы":
        return Game(Chik())

    elif vibor == "Камень":
        return Game(Rock())
    elif vibor == "Спок":
        return Game(Spok())
    elif vibor == "Ящерица":
        return Game(Zemnovodnoe())
    elif vibor == "Рандом":
        return Game(Random())

n=1
while n==1:
    print("Первый игрок:\nСделайте выбор: Бумага, Камень, Ножницы, Спок, Ящерица, Рандом")
    vibor=input()
    while vibor not in ("Бумага", "Камень", "Ножницы", "Спок", "Ящерица", "Рандом"):
        print("Повторите ввод")
        vibor=input()
    player1 = playtime(vibor)

    print("Второй игрок:\nСделайте выбор: Бумага, Камень, Ножницы, Спок, Ящерица, Рандом")
    vibor = input()
    while vibor not in ("Бумага", "Камень", "Ножницы", "Спок", "Ящерица", "Рандом"):
        print("Повторите ввод")
        vibor=input()
    player2 = playtime(vibor)
    player1.play(player2)
    print("Хотите повторить? 1-Да")
    n=int(input())
print("Конец! Спасибо за игру!")