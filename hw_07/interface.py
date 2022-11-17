from models import Person, Phonebook
import messages as m


def run():
    phonebook = Phonebook()
    print(m.HELLO_MSG)
    while True:
        user_input = input(m.COMMAND_MSG)
        if user_input == "1":
            print(phonebook)
        elif user_input == "2":
            add_row(phonebook)
        else:
            break
    print(m.END_MSG)


def add_row(phonebook):
    person = Person()
    for attr in phonebook.attrs:
        person.set(attr, input(f"Введите {m.TRANSLATION.get(attr)}: "))
    phonebook.add(person)
    phonebook.save()
    print(m.ADD_MSG)
