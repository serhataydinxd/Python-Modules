import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")

    else:
        print("=== Cyber Archives Recovery & Preservation ===")

        file = sys.argv[1]
        try:
            print(f"Accessing file '{file}'")
            f: typing.IO[str] = open(file, "r")
            try:
                content: str = f.read()
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

            print("Transform data:")
            print("---")
            print()

            transformed = content.replace("\n", "#\n")
            if content and not content.endswith("\n"):
                transformed = transformed + "#"

            print(transformed, end="")
            print()

            print("---")
            new = input("Enter new file name (or empty): ")

            if new == "":
                print("Not saving data.")

            else:
                print(f"Saving data to '{new}'")
                try:
                    new_f: typing.IO[str] = open(new, "w")
                    try:
                        new_f.write(transformed)
                    finally:
                        new_f.close()

                except OSError as e:
                    print(f"Error opening file '{new}': {e}")
                    print("Data not saved.")

                else:
                    print(f"Data saved in file '{new}'.")
