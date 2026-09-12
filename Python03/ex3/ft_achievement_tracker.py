import random


def gen_player_achievements() -> set[str]:
    achievements: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder",
    ]
    how_many = random.randint(7, 9)
    new_set: set[str] = set(random.sample(achievements, how_many))
    return new_set


if __name__ == "__main__":
    achievements: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder",
    ]

    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")
    print()

    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()

    print(f"Alice is missing: {set(achievements).difference(alice)}")
    print(f"Bob is missing: {set(achievements).difference(bob)}")
    print(f"Charlie is missing: {set(achievements).difference(charlie)}")
    print(f"Dylan is missing: {set(achievements).difference(dylan)}")
