class Plant:
    _name: str
    _height: float
    _age: int
    _grow_rate: float

    def __init__(
        self, name: str, height: float, age: int, grow_rate: float = 1.0
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._grow_rate = grow_rate

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days old"
        )

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height:g}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self.set_height(self._height + self._grow_rate)

    def age(self, days: int = 1) -> None:
        self.set_age(self._age + days)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-5.0)
    rose.set_age(-2)
    print()
    print("Current state: ", end="")
    rose.show()
