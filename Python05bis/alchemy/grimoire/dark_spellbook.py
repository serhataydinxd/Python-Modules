from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eye-ball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    ret = dark_validate_ingredients(ingredients)
    if ret.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({ret})"
    elif ret.endswith(" - INVALID"):
        return f"Spell rejected: {spell_name} ({ingredients})"
    return "Error"
