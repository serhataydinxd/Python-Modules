import importlib.util


def check_pandas() -> int:
    pand = importlib.util.find_spec("pandas")
    if pand is not None:
        import pandas

        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
        return 1
    else:
        print("[KO] pandas could not be imported")
        return 0


def check_numpy() -> int:
    nump = importlib.util.find_spec("numpy")
    if nump is not None:
        import numpy

        print(
            f"[OK] numpy ({numpy.__version__}) - Numerical computation ready"
        )
        return 1
    else:
        print("[KO] numpy could not be imported")
        return 0


if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")

    imported: int = 0
    imported += check_pandas()
    imported += check_numpy()

    print()
    print("pip vs Poetry:")
    print(
        "  requirements.txt declares what to install;"
        " pip resolves it at install time"
    )
    print(
        "  pyproject.toml declares the same constraints,"
        " and Poetry pins the resolved"
    )
    print("  versions in poetry.lock so every install is identical.")

    print()
    if imported != 2:
        print("Could not import some reagents")
        print(
            'Install them using "pip install -r requirements.txt" inside ex0'
        )
        print('or with "poetry install" on this folder')
    else:
        print("All reagents present and accounted for.")
