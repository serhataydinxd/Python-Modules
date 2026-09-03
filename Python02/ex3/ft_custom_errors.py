class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.args = (message,)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.args = (message,)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.args = (message,)


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise WaterError("Not enough water in the tank!")
    elif operation_number == 1:
        raise PlantError("The tomato plant is wilting!")


def test_plant() -> None:
    try:
        print()
        print("Testing PlantError...")
        garden_operations(1)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water() -> None:
    try:
        print()
        print("Testing WaterError...")
        garden_operations(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_em_all() -> None:
    try:
        garden_operations(1)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        garden_operations(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant()
    test_water()
    print()
    print("Testing catching all garden errors...")
    test_em_all()
    print()
    print("All custom error types work correctly!")
