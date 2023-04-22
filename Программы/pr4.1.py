from abc import ABC, abstractmethod
from typing import List


class cookiesItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"печенька под номером: {self.number}"


class Iterator(ABC):
    @abstractmethod
    def next(self) -> cookiesItem:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...


class cookiesnumIterator(Iterator):
    def __init__(self, cookies: List[cookiesItem]):
        self._cookies = cookies
        self._index = 0

    def next(self) -> cookiesItem:
        cookies_item = self._cookies[self._index]
        self._index += 1
        return cookies_item

    def has_next(self) -> bool:
        return False if self._index >= len(self._cookies) else True


class cookiesAggregate:
    def __init__(self, amount_num: int = 10):
        self.num = [cookiesItem(it+1) for it in range(amount_num)]
        print(f"Взяли банку печенек "
              f"на {amount_num} печенек")

    def amount_num(self) -> int:
        return len(self.num)

    def iterator(self) -> Iterator:
        return cookiesnumIterator(self.num)




if __name__ == "__main__":
    cookies = cookiesAggregate(5)
    iterator = cookies.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))
