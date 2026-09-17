import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")

    for file in sys.argv[1:]:
        try:
            print(f"Accessing file '{file}'")
            f: typing.IO[str] = open(file, "r")
            try:
                content = f.read()
            finally:
                f.close()

        except OSError as e:
            print(f"Error opening file '{file}': {e}")

        else:
            print("---")
            print()

            print(content, end="")
            print()

            print("---")
            print(f"File '{file}' closed.")
            print()
