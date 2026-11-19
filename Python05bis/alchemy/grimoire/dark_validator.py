from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    ing: list[str] = dark_spell_allowed_ingredients()
    for i in ingredients.split():
        if i.lower().strip(",.:") in ing:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
