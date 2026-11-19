from ex3 import FlameFactory, TransformCreatureFactory
from ex3.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    print(" fight!")
    print(first_creature.attack())
    print(second_creature.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing factory")
    test_factory(flame_factory)
    print()

    print("Testing factory")
    test_factory(transform_factory)
    print()

    print("Testing battle")
    test_battle(flame_factory, transform_factory)
