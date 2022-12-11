PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as people_invited:
    names = people_invited.readlines()

with open("./Input/Letters/starting_letter.txt") as initial_letter:
    letter = initial_letter.read()
    for name in names:
        formatted_name = name.strip()
        letter_for = letter.replace(PLACEHOLDER, formatted_name)
        with open(f"./Output/ReadyToSend/letter_for_{formatted_name}.txt", "w") as final_letter:
            final_letter.write(letter_for)
