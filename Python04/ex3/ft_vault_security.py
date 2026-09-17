def secure_archive(
    file: str,
    action: str = "read",
    text: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file, "r") as f:
                archive: str = f.read()
            return (True, archive)

        if action == "write":
            with open(file, "w") as f:
                f.write(text)
            return (True, "Content successfully written to file")

        return (False, f"Invalid action: '{action}'")

    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive(__file__)
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_archive.txt", "write", result[1]))
    else:
        print((False, "No content available to write"))
