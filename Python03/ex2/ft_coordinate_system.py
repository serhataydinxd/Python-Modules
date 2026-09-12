import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            str_x, str_y, str_z = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(str_x)
        except ValueError as e:
            print(f"Error on parameter '{str_x}': {e}")
            continue

        try:
            y = float(str_y)
        except ValueError as e:
            print(f"Error on parameter '{str_y}': {e}")
            continue

        try:
            z = float(str_z)
        except ValueError as e:
            print(f"Error on parameter '{str_z}': {e}")
            continue

        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    center_dist = math.sqrt(
        (first[0] ** 2) + (first[1] ** 2) + (first[2] ** 2)
    )
    print(f"Distance to center: {round(center_dist, 4)}")
    print()

    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    dist = math.sqrt(
        ((first[0] - second[0]) ** 2)
        + ((first[1] - second[1]) ** 2)
        + ((first[2] - second[2]) ** 2)
    )
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")
