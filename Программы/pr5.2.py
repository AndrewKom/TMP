from abc import ABC, abstractmethod


class Product:
    bread = ["Кунжутные", "Обычные"]
    meal = ['Две котлеты', 'Котлета']
    nam = ['Помидоры', 'Огурцы']
    souse = ["Кетчуп", "Майонез"]


class burger:
    def __init__(self, name):
        self.name = name

        self.meal = None
        self.topping = []
        self.souse = None
        self.botbread = None

    def printer(self):
        print(f'Название:{self.name}\n' \
              f'Мясо:{self.meal}\n' \
              f'Топинги:{[it for it in self.topping]}\n' \
              f'Соус:{self.souse}\n' \
              f'Булочки:{self.botbread}\n')


class Builder(ABC):



    @abstractmethod
    def add_sauce(self) -> None: pass

    @abstractmethod
    def add_meal(self) -> None: pass

    @abstractmethod
    def add_topping(self) -> None: pass

    @abstractmethod
    def prepare_botbread(self) -> None: pass

    @abstractmethod
    def get_bur(self) -> burger: pass


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_bur(self):
        if not self.builder:
            raise ValueError("Builder didn't set")

        self.builder.add_sauce()
        self.builder.add_meal()
        self.builder.add_topping()
        self.builder.prepare_botbread()


class RichBu(Builder):
    def __init__(self):
        self.bur = burger("Богатый")


    def add_sauce(self) -> None:
        self.bur.souse = Product.souse[0]

    def add_meal(self) -> None:
        self.bur.meal = Product.meal[0]

    def add_topping(self) -> None:
        self.bur.topping.append(Product.nam[0])
        self.bur.topping.append(Product.nam[1])

    def prepare_botbread(self) -> None:
        self.bur.botbread = Product.bread[0]

    def get_bur(self) -> burger:
        return self.bur


class DefaultBur(Builder):
    def __init__(self):
        self.bur = burger("Обычный")


    def add_sauce(self) -> None:
        self.bur.souse = Product.souse[1]

    def add_meal(self) -> None:
        self.bur.meal = Product.meal[1]

    def add_topping(self) -> None:
        self.bur.topping.append(Product.nam[0])

    def prepare_botbread(self) -> None:
        self.bur.botbread = Product.bread[1]

    def get_bur(self) -> burger:
        return self.bur






director = Director()
print("Богатый-1, Обычный-2")
a=int(input())
if a==1:
    builder = RichBu()
else:
    builder = DefaultBur()
director.set_builder(builder)
director.make_bur()
burger = builder.get_bur()
burger.printer()





