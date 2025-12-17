def create_username(forename, surname, year="2025"):
    username = f"{forename[0]}{surname}{year[2:]}"
    return username


user = create_username("Frances", "Ford", year="2021")  # FFord21
