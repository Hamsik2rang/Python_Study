PLACEHOLDER = "[name]"

with open("./Day8/Resources/invited_names.txt", mode="r") as f:
    people = f.readlines()
print(people)
with open("./Day8/Resources/starting_letter.txt", mode="r") as f:
    form = f.read()
    for person in people:
        person = person.strip()
        letter = form.replace(PLACEHOLDER, person)
        with open(f"./Day8/Resources/Letters/{person}.txt", mode="w") as f:
            f.write(letter)
