from ex3 import TransformCreatureFactory


if __name__ == "__main__":
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability")
    print(" base:")
    print(base.describe())
    print(base.attack())
    base.transform()
    print()
    print(base.attack())
    base.revert()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    evolved.transform()
    print(evolved.attack())
    evolved.revert()
