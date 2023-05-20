class Leaf:
    def __init__(self, number, *args):
        self.number = number
        self.position = args[0]


    def show(self):
        print("\t", end="")
        print(self.position)

    def showNum(self):
        print("\t", end="")
        print(self.number)


class Element:
    def __init__(self, number, *args):
        self.number = number
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def show(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.show()

    def showNum(self):
        print(self.number)
        for child in self.children:
            print("\t", end="")
            child.showNum()



if __name__ == "__main__":
    Hi = Element("A1", "Генерал")
    Item1 = Element("B1", "Майор 1")
    Item2 = Element("B2", "Майор 2")
    Item3 = Element("B3", "Майор 3")
    Item11 = Leaf("C1", "Рядовой 11")
    Item12 = Leaf("C2", "Рядовой 12")
    Item21 = Leaf("C3", "Рядовой 21")
    Item22 = Leaf("C4", "Рядовой 22")
    Item31 = Leaf("C5", "Рядовой 31")
    Item32 = Leaf("C6", "Рядовой 32")
    Item1.add(Item11)
    Item1.add(Item12)
    Item2.add(Item21)
    Item2.add(Item22)
    Item3.add(Item31)
    Item3.add(Item32)

    Hi.add(Item1)
    Hi.add(Item2)
    Hi.add(Item3)
    Hi.show()
    print("Номера:")
    Hi.showNum()