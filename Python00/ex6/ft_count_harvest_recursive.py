def recur_it(day: int) -> None:
    if day > 0:
        recur_it(day - 1)
        print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    recur_it(day)
    print("Harvest time!")
