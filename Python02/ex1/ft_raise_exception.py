def input_temperature(temp_str: str) -> int:
    val = int(temp_str)
    if val > 40:
        raise ValueError(f"{val}°C is too hot for plants (max 40°C)")
    elif val < 0:
        raise ValueError(f"{val}°C is too cold for plants (min 0°C)")
    return val


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    try:
        print()
        print("Input data is '25'")
        val = input_temperature("25")
        print(f"Temperature is now {val}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print()
        print("Input data is 'abc'")
        val = input_temperature("abc")
        print(f"Temperature is now {val}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print()
        print("Input data is '100'")
        val = input_temperature("100")
        print(f"Temperature is now {val}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print()
        print("Input data is '-50'")
        val = input_temperature("-50")
        print(f"Temperature is now {val}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
