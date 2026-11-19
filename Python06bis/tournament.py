from ex4 import BattleStrategy, NormalStrategy, AggressiveStrategy
from ex3.factory import CreatureFactory
from ex3 import FlameFactory, TransformCreatureFactory
from ex4 import InvalidStrategyError


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    creatures = [factory.create_base() for factory, _ in opponents]

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for first in range(len(opponents)):
            for second in range(first + 1, len(opponents)):
                poke1 = creatures[first]
                poke2 = creatures[second]
                strat1 = opponents[first][1]
                strat2 = opponents[second][1]

                print()
                print("* Battle *")
                print(poke1.describe())
                print(" vs.")
                print(poke2.describe())
                print(" now fight!")

                strat1.act(poke1)
                strat2.act(poke2)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle(
        [
            (flame_factory, normal_strategy),
            (transform_factory, aggressive_strategy),
        ]
    )

    print()
    print("Tournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle(
        [
            (transform_factory, aggressive_strategy),
            (flame_factory, aggressive_strategy),
        ]
    )
