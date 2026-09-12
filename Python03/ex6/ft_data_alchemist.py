import random

if __name__ == "__main__":
    lst: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    print("=== Game Data Alchemist ===")
    print()

    print(f"Initial list of players: {lst}")
    print()

    all_cap: list[str] = [item.capitalize() for item in lst]
    print(f"New list with all names capitalized: {all_cap}")
    print()

    already_cap: list[str] = [item for item in lst if item in all_cap]
    print(f"New list of capitalized names only: {already_cap}")
    print()

    scores: dict[str, int] = {
        item: random.randint(300, 999) for item in all_cap
    }
    print(f"Score dict: {scores}")
    print()

    mid = sum(scores.values()) / len(scores)
    print(f"Score average is {round(mid, 2)}")
    print()

    high: dict[str, int] = {
        item: score for item, score in scores.items() if score > mid
    }
    print(f"High scores: {high}")
