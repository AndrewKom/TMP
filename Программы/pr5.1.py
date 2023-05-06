from abc import ABC, abstractmethod

class Legs(ABC):
    def __init__(self, object: str):
        self._object = object

    @abstractmethod
    def create(self): pass


class Cap(ABC):
    def __init__(self, object: str):
        self._object = object

    @abstractmethod
    def create(self): pass


class ModernLegs(Legs):
    def __init__(self):
        super().__init__("Современный")

    def create(self):
        print(f'Созданы ножки для стола: {self._object}')


class ModernCap(Cap):
    def __init__(self):
        super().__init__("Современный")

    def create(self):
        print(f'Создана крышка для стола: {self._object}')



class VenLegs(Legs):
    def __init__(self):
        super().__init__("Венецианский")

    def create(self):
        print(f'Созданы ножки для стола: {self._object}')


class VenCap(Cap):
    def __init__(self):
        super().__init__("Венецианский")

    def create(self):
        print(f'Создана крышка для стола: {self._object}')




class GuiAbstractTable(ABC):
    @abstractmethod
    def getLegs(self) -> Legs: pass

    @abstractmethod
    def getCap(self) -> Cap: pass



class ModernGuiFactory(GuiAbstractTable):
    def getLegs(self) -> Legs:
        return ModernLegs()

    def getCap(self) -> Cap:
        return ModernCap()



class VenGuiFactory(GuiAbstractTable):
    def getLegs(self) -> Legs:
        return VenLegs()

    def getCap(self) -> Cap:
        return VenCap()



class Application:
    def __init__(self, table: GuiAbstractTable):
        self._gui_table = table

    def create_gui(self):
        legs = self._gui_table.getLegs()
        cap = self._gui_table.getCap()
        legs.create()
        cap.create()


def create_factory(objectname: str) -> GuiAbstractTable:
    tabled = {
        "Современный": ModernGuiFactory,
        "Венецианский": VenGuiFactory
    }
    return tabled[objectname]()



objectname = "Современный"
cr = create_factory(objectname)
app = Application(cr)
app.create_gui()


objectname = "Венецианский"
cr = create_factory(objectname)
app = Application(cr)
app.create_gui()