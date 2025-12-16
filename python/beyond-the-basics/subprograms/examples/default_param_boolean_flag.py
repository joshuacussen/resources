def format_name(first, last, uppercase=False):
    name = f"{first} {last}"

    if uppercase:
        name = name.upper()

    return name


name = format_name("Ada", "Lovelace")  # Ada Lovelace
upper_name = format_name("Ada", "Lovelace", uppercase=True)  # ADA LOVELACE
