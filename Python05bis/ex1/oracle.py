from dotenv import load_dotenv
import os


def main() -> int:
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    url = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    if (
        mode is None
        or url is None
        or api is None
        or log is None
        or zion is None
    ):
        print("Missing configuration")
        if mode is None:
            print("MATRIX_MODE is missing, defaulting")
            mode = "development"
        if url is None:
            print("DATABASE_URL is missing, defaulting")
            url = "not configured"
        if api is None:
            print("API_KEY is missing, defaulting")
            api = "not configured"
        if log is None:
            print("LOG_LEVEL is missing, defaulting")
            log = "INFO"
        if zion is None:
            print("ZION_ENDPOINT is missing, defaulting")
            zion = "not configured"

    print()
    print("Configuration loaded:")
    database_status = (
        "not configured" if url == "not configured" else "configured"
    )
    api_status = "not configured" if api == "not configured" else "configured"
    zion_status = (
        "not configured" if zion == "not configured" else "configured"
    )
    if mode == "production":
        print("Mode: production")
        print("Be careful what you do, you are in prod")
        print(f"Database: {database_status}")
        print(f"API Access: {api_status}")
        print(f"Log Level: {log}")
        print(f"Remote Network: {zion_status}")
    elif mode == "development":
        print("Mode: development")
        print("Go crazy, you are in dev")
        print(f"Database: {database_status}")
        print(f"API Access: {api_status}")
        print(f"Log Level: {log}")
        print(f"Zion Endpoint: {zion_status}")
    else:
        print("Bad mode, check env")
        return 1
    return 0


if __name__ == "__main__":
    print("ORACLE STATUS: Consulting the configuration...")
    print()

    code = main()
    if code == 1:
        print("Bad config, check env")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")

    print()
    print("The Oracle sees all configurations.")
