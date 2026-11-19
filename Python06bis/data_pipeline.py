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
            self.total_entries += 1
            self.entries.append((self.total_entries, str(data)))
        elif isinstance(data, list):
            for element in data:
                if type(element) not in (int, float):
                    raise TypeError("Improper numeric data")
            for element in data:
                self.total_entries += 1
                self.entries.append((self.total_entries, str(element)))
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
            self.total_entries += 1
            self.entries.append((self.total_entries, data))
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    raise TypeError("Input not a string or a list of strings")
            for element in data:
                self.total_entries += 1
                self.entries.append((self.total_entries, element))
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
            self.total_entries += 1
            self.entries.append(
                (
                    self.total_entries,
                    f"{data['log_level']}: {data['log_message']}",
                )
            )
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    raise TypeError("Input not a dict or a list of dicts")
            for element in data:
                self.total_entries += 1
                self.entries.append(
                    (
                        self.total_entries,
                        f"{element['log_level']}: {element['log_message']}",
                    )
                )
        else:
            raise TypeError("Input not a dict or a list of dicts")


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("{" + ", ".join(items) + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            export: list[tuple[int, str]] = []
            try:
                for i in range(nb):
                    export.append(processor.output())
            except IndexError:
                if len(export) > 0:
                    plugin.process_output(export)
                continue
            plugin.process_output(export)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    print()

    data_stream = DataStream()
    data_stream.print_processors_stats()
    print()

    print("Registering Processors")
    print()

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    first_batch = [
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
    print(f"Send first batch of data on stream: {first_batch}")
    print()

    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    print()
    data_stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {second_batch}")
    print()

    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    data_stream.output_pipeline(5, json_plugin)
    print()
    data_stream.print_processors_stats()
