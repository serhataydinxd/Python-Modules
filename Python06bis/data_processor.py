from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.entries: list[tuple[int, str]] = []
        super().__init__()

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.entries.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) in (int, float):
            return True
        elif isinstance(data, list):
            for element in data:
                if type(element) not in (int, float):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if type(data) in (int, float):
            self.entries.append((len(self.entries) + 1, str(data)))
        elif isinstance(data, list):
            for element in data:
                if type(element) not in (int, float):
                    raise TypeError("Improper numeric data")
            for element in data:
                self.entries.append((len(self.entries) + 1, str(element)))
        else:
            raise TypeError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, str):
            self.entries.append((len(self.entries) + 1, data))
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    raise TypeError("Input not a string or a list of strings")
            for element in data:
                self.entries.append((len(self.entries) + 1, element))
        else:
            raise TypeError("Input not a string or a list of strings")


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return (
                set(data.keys()) == {"log_level", "log_message"}
                and isinstance(data["log_level"], str)
                and isinstance(data["log_message"], str)
            )
        elif isinstance(data, list):
            for element in data:
                if not self.validate(element):
                    return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if isinstance(data, dict):
            self.entries.append(
                (
                    len(self.entries) + 1,
                    f"{data['log_level']}: {data['log_message']}",
                )
            )
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    raise TypeError("Input not a dict or a list of dicts")
            for element in data:
                self.entries.append(
                    (
                        len(self.entries) + 1,
                        f"{element['log_level']}: {element['log_message']}",
                    )
                )
        else:
            raise TypeError("Input not a dict or a list of dicts")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print()
    print("Testing Numeric Processor...")
    numeric_processor = NumericProcessor()

    print("Trying to validate input '42':", numeric_processor.validate(42))
    print(
        "Trying to validate input 'Hello':",
        numeric_processor.validate("Hello"),
    )
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest("foo")
    except TypeError as error:
        print("Got exception:", error)
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric_processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        index, value = numeric_processor.output()
        print(f"Numeric value {index}: {value}")

    print()
    print("Testing Text Processor...")
    text_processor = TextProcessor()
    print("Trying to validate input '42':", text_processor.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_processor.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    index, value = text_processor.output()
    print(f"Text value {index}: {value}")

    print()
    print("Testing Log Processor...")
    log_processor = LogProcessor()
    print("Trying to validate input 'Hello':", log_processor.validate("Hello"))
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print("Processing data:", logs)
    log_processor.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        index, value = log_processor.output()
        print(f"Log entry {index}: {value}")
