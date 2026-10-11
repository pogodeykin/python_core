from abc import ABC, abstractmethod

class Flower(ABC):

    def __init__(self, name: str, price: float, lifetime: int):
        if price < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        if lifetime <= 0:
            raise ValueError("Время жизни должно быть больше нуля")

        self.name = name
        self.price = price
        self.lifetime = lifetime

    @abstractmethod
    def describe(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.name} — {self.price:.2f} руб., {self.lifetime} дн."


class Rose(Flower):
    def describe(self) -> str:
        return "Роза"


class Peony(Flower):
    def describe(self) -> str:
        return "Пион"


class Lily(Flower):
    def describe(self) -> str:
        return "Лилия"


class Accessory:

    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Стоимость не может быть отрицательной")

        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} — {self.price:.2f} руб."


class Bouquet:
    def __init__(self):
        self.flowers: list[Flower] = []
        self.accessories: list[Accessory] = []

    def add_flower(self, flower: Flower) -> None:
        self.flowers.append(flower)

    def add_accessory(self, accessory: Accessory) -> None:
        self.accessories.append(accessory)

    def total_price(self) -> float:
        flowers_price = sum(flower.price for flower in self.flowers)
        accessories_price = sum(item.price for item in self.accessories)
        return flowers_price + accessories_price

    def wilting_time(self) -> float:
        if not self.flowers:
            return 0

        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_by_price(self) -> None:
       self.flowers.sort(key=lambda flower: flower.price)

    def contains_flower(self, name: str) -> bool:
        return any(flower.name.lower() == name.lower() for flower in self.flowers)

    def __str__(self) -> str:
        flowers = "\n".join(f"  {flower}" for flower in self.flowers)
        accessories = "\n".join(f"  {item}" for item in self.accessories)

        return (
            f"Цветы:\n{flowers or '  нет'}\n"
            f"Аксессуары:\n{accessories or '  нет'}\n"
            f"Стоимость букета: {self.total_price():.2f} руб.\n"
            f"Среднее время жизни: {self.wilting_time():.1f} дн."
        )


bouquet = Bouquet()

bouquet.add_flower(Rose("Роза", 250, 7))
bouquet.add_flower(Peony("Пион", 150, 5))
bouquet.add_flower(Lily("Лилия", 300, 10))

bouquet.add_accessory(Accessory("Крафтовая бумага", 100))
bouquet.add_accessory(Accessory("Упаковочная лента", 50))

print(bouquet)

bouquet.sort_by_price()
print("\nЦветы после сортировки:")
for flower in bouquet.flowers:
    print(flower)

print("\nЕсть ли роза в букете?", bouquet.contains_flower("Роза"))