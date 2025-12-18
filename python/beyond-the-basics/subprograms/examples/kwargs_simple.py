def create_username(forename, surname, year):
    username = f"{forename[0]}{surname}{year[2:]}"
    return username


user = create_username(forename="Jon", surname="Hamm", year="2025")  # JHamm25
user2 = create_username(year="2023", forename="Quintin", surname="Bacon")  # QBacon23
