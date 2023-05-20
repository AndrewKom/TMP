from abc import ABC, abstractmethod


class PasswordItem:
    def __init__(self, password):
        self.password = password

    def get(self):
        return self.password

class Target(ABC):

    @abstractmethod
    def ex(self) -> None:
        pass


class Real(Target):
    def ex(self) -> None:
        print("Настоящая часть кода запущена...\n5*5 =", 5*5)


class Proxy(Target):

    def __init__(self, real_target: Real) -> None:
        self._real_target = real_target

    def ex(self) -> None:

        if self.access():
            self._real_target.ex()

    def access(self) -> bool:
        realpassword = 12345
        print("Proxy: Проверка доступа")
        if realpassword == password.get():
            return True
        else:
            print("В доступе отказано")
            return False


def client(target: Target) -> None:
    target.ex()


if __name__ == "__main__":
    password = PasswordItem(111111)
    print(password.get())
    print("Запуск напрямую, без Proxy:")
    real_target = Real()
    client(real_target)

    print("\nЗапуск с Proxy и неправильным паролем:")
    proxy = Proxy(real_target)
    client(proxy)

    password = PasswordItem(12345)
    print("\nЗапуск с Proxy и правильным паролем:")
    proxy = Proxy(real_target)
    client(proxy)