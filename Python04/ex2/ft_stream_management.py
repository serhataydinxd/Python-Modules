import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")

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
            err = str(e)
            sys.stderr.write("[STDERR] Error opening file '")
            sys.stderr.write(file)
            sys.stderr.write("': ")
            sys.stderr.write(err)
            sys.stderr.write("\n")
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
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new = sys.stdin.readline().strip("\n")

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
                    err = str(e)
                    sys.stderr.write("[STDERR] Error opening file '")
                    sys.stderr.write(new)
                    sys.stderr.write("': ")
                    sys.stderr.write(err)
                    sys.stderr.write("\n")
                    print("Data not saved.")

                else:
                    print(f"Data saved in file '{new}'.")
