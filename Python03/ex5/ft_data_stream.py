import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    lads: list[str] = ["Bob", "Dylan", "Charlie", "Alice"]

    events: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "cry",
        "swim",
        "jump",
        "roll",
    ]

    while True:
        lad = random.choice(lads)
        event = random.choice(events)
        yield (lad, event)


def consume_event(
    lst: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(lst) > 0:
        index = random.randint(0, len(lst) - 1)
        event = lst[index]
        del lst[index]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()

    generator: typing.Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        p_tuple: tuple[str, str] = next(generator)
        print(f"Event {i}: Player {p_tuple[0]} did action {p_tuple[1]}")

    print()
    lst: list[tuple[str, str]] = [("", "")] * 10
    for i in range(10):
        lst[i] = next(generator)

    print(f"Built list of 10 events: {lst}")
    for event in consume_event(lst):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lst}")
