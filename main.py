PLACEHOLDER = "[name]"



with open("Give Path of the file were names of the preson is saved i.e invited_names") as names_file:
    names = names_file.readlines()


with open("Give path of the file were body of the letter is saved i.e starting_letter") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter: #here give path of the folder were you have to save generated message.
            completed_letter.write(new_letter)
