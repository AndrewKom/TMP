from abc import ABC, abstractmethod
from typing import List


class OrderItemVisitor(ABC):
    @abstractmethod
    def visit(self, item) -> float:
        ...


class ItemElement(ABC):
    @abstractmethod
    def accept(self, visitor: OrderItemVisitor) -> float:
        ...


class Tort(ItemElement):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)


class Coffee(ItemElement):
    def __init__(self, name: str,
                 price: float,
                 capacity: float):
        self.name = name
        self.price = price
        self.capacity = capacity

    def get_price(self) -> float:
        return self.price

    def get_capacity(self) -> float:
        return self.capacity

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)


class WithOutDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Tort):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyTortDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Tort):
            cost = item.get_price()
            cost -= cost * 0.20 #Скидка 20% на торт
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyCoffeeDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Tort):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
            cost -= cost * 0.40 #Скидка 40% на кофе
        return cost


class AllDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Tort):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        cost -= cost * 0.50 #Скидка 50% на все товары
        return cost


class Waiter:
    def __init__(self, discount: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discount

    def set_order(self, order: List[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount: OrderItemVisitor) -> None:
        self.discount_calculator = discount

    def calculate_finish_price(self) -> float:
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        return price



order: List[ItemElement] = [Tort("Красный бархат", 10.1),
                            Coffee("Латте мал", 5, 0.3),
                            Tort("Черный лес", 9.5),
                            Coffee("Капучино бол", 4, 0.5),
                            Tort("Чизкейк", 11.9),
                            Tort("Москва", 15.2)]
discount = WithOutDiscountVisitor()
waiter = Waiter(discount)
waiter.set_order(order)

n=1
while n==1:
    print("Введите скидку: Без, Тортик, Кофе, Всё")
    vibor=input()
    while vibor not in ("Без", "Тортик", "Кофе", "Всё"):
        print("Повторите ввод")
        vibor=input()

    if vibor=="Без":
        discount = WithOutDiscountVisitor()
        waiter = Waiter(discount)
        waiter.set_order(order)
        print(f"Сумма заказа без учета скидок: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif vibor=="Тортик":
        discount = OnlyTortDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на тортик: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif vibor=="Кофе":
        discount = OnlyCoffeeDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на кофе: "
              f"{round(waiter.calculate_finish_price(),2)}")
    elif vibor=="Всё":
        discount = AllDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на всё: "
              f"{round(waiter.calculate_finish_price(),2)}")
    print("Хотите повторить? 1-Да")
    n = int(input())
print("Конец! Спасибо за заказ!")