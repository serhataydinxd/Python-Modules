class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30
    rose.show()
    sun = Plant()
    sun.name = "Sunflower"
    sun.height = 80
    sun.age = 45
    sun.show()
    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120
    cactus.show()
