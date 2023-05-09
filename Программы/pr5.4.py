from abc import ABC, abstractmethod

class User():
    def __init__(self, med, name, pol):
        self.mediator = med
        self.name = name
        self.pol = pol

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def sendM(self, msg):
        pass

    @abstractmethod
    def sendW(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass

class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)

    def send_messageM(self,msg,user):
        for u in self.users:
            if u != user and u.pol == "M":
                u.receive(msg)

    def send_messageW(self,msg,user):
        for u in self.users:
            if u != user and u.pol == "W":
                u.receive(msg)

class ConcreteUser(User):
    def send(self, msg):
        print(self.name + ": Отправил сообщение: " + msg)
        self.mediator.send_message(msg, self)

    def sendM(self, msg):
        print(self.name + ": Отправил парням: " + msg)
        self.mediator.send_messageM(msg, self)

    def sendW(self, msg):
        print(self.name + ": Отправил девушкам: " + msg)
        self.mediator.send_messageW(msg, self)

    def receive(self, msg):
        print(self.name + ": Получено сообщение: " + msg)

def printl():
    print("-" * 50)


mediator = ChatMediator()

user1 = ConcreteUser(mediator, "Андрей", "M")
user2 = ConcreteUser(mediator, "Костя", "M")
user3 = ConcreteUser(mediator, "Даша", "W")
user4 = ConcreteUser(mediator, "Ира", "W")

mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)
mediator.add_user(user4)

user1.send("Привет всем")
printl()

user1.sendM("Привет Парням")
printl()

user1.sendW("Привет Девушкам")
printl()