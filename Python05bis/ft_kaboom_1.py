if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook

    print(
        alchemy.grimoire.dark_spellbook.dark_spell_record(
            "Doom", "Chemical X, Mana"
        )
    )
