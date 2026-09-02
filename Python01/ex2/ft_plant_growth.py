class Plant:
    name: str
    height: float
    days: int

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{round(self.days, 1)} days old"
        )

    def grow(self, gro: float) -> None:
        self.height = self.height + gro

    def age(self, day: int) -> None:
        self.days = self.days + day


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    init_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()
    print(f"Growth this week: {round(rose.height - init_height, 1)}cm")
