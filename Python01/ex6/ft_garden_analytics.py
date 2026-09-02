class Plant:
    class Stats:
        _grow_calls: int
        _age_calls: int
        _show_calls: int

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls = self._grow_calls + 1

        def record_age(self) -> None:
            self._age_calls = self._age_calls + 1

        def record_show(self) -> None:
            self._show_calls = self._show_calls + 1

        def record_shade(self) -> None:
            return

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    _name: str
    _height: float
    _age: int
    _grow_rate: float
    _stats: Stats

    def __init__(
        self, name: str, height: float, age: int, grow_rate: float = 1.0
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._grow_rate = grow_rate
        self._stats = self.Stats()

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def show(self) -> None:
        self._stats.record_show()
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

    def grow(self, days: int = 1) -> None:
        self._height = self._height + self._grow_rate * days
        self._stats.record_grow()

    def age(self, days: int = 1) -> None:
        self._age = self._age + days
        self._stats.record_age()

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def check_age(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    _color: str
    _bloomed: bool

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        grow_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        _shade_calls: int

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls = self._shade_calls + 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    _trunk_diameter: float

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        grow_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )


class Seed(Flower):
    _seeds: int
    _seed_capacity: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_capacity: int,
        grow_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, color, grow_rate)
        self._seeds = 0
        self._seed_capacity = seed_capacity

    def bloom(self) -> None:
        super().bloom()
        self._seeds = self._seed_capacity

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, 30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print()
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)
