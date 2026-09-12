import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    print()

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            item, quan = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item.isspace() or item == "":
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            quantity = int(quan)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        inventory[item] = quantity

    print()
    print(f"Got inventory: {inventory}")
    print()

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")
    print()

    total = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total}")

    for item in inventory.keys():
        per: float = 0.0
        try:
            per = round(inventory[item] / total * 100, 1)
        except ZeroDivisionError:
            pass
        print(f"Item {item} represents {per}%")

    if len(item_list) > 0:
        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item in item_list[1:]:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item
            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )

    print()
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
