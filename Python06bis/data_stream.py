from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.entries: list[tuple[int, str]] = []
        self.total_entries: int = 0
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
            self.total_entries += 1
        elif isinstance(data, list):
            for element in data:
                if type(element) not in (int, float):
                    raise TypeError("Improper numeric data")
            for element in data:
                self.entries.append((len(self.entries) + 1, str(element)))
                self.total_entries += 1
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
            self.total_entries += 1
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    raise TypeError("Input not a string or a list of strings")
            for element in data:
                self.entries.append((len(self.entries) + 1, element))
                self.total_entries += 1
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
            self.total_entries += 1
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
                self.total_entries += 1
        else:
            raise TypeError("Input not a dict or a list of dicts")


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, stream: DataProcessor) -> None:
        self.processors.append(stream)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        for processor in self.processors:
            if isinstance(processor, NumericProcessor):
                name = "Numeric Processor"
            elif isinstance(processor, TextProcessor):
                name = "Text Processor"
            elif isinstance(processor, LogProcessor):
                name = "Log Processor"
            else:
                continue

            print(
                f"{name}: total {processor.total_entries} items processed, "
                f"remaining {len(processor.entries)} on processor"
            )
            print()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print()

    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Numeric Processor")
    print()

    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)

    stream_data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream:", stream_data)
    data_stream.process_stream(stream_data)
    data_stream.print_processors_stats()

    print("Registering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    print("Send the same batch again")
    data_stream.process_stream(stream_data)
    data_stream.print_processors_stats()

    print(
        "Consume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric_processor.output()
    for _ in range(2):
        text_processor.output()
    log_processor.output()
    data_stream.print_processors_stats()
