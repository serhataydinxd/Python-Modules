class Plant:
    name: str
    height: float
    days: int
    grow_rate: float

    def __init__(
        self, name: str, height: float, days: int, grow_rate: float = 1.0
    ) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.grow_rate = grow_rate
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{round(self.days, 1)} days old"
        )

    def grow(self) -> None:
        self.height = self.height + self.grow_rate

    def age(self, day: int) -> None:
        self.days = self.days + day


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30, 1.8)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
