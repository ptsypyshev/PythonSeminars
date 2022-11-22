from csv import reader, writer
from os.path import exists
import messages as m

DEFAULT_CSV_FILE = "local.csv"
DEFAULT_TXT_FILE = "local.txt"
CSV_DELIMITER = ";"
TXT_DELIMITER = "\n"


class Person():
    last_name = ""
    first_name = ""
    phone_number = ""
    description = ""

    def __init__(self, args=None):
        if args:
            self.last_name = args[0]
            self.first_name = args[1]
            self.phone_number = args[2]
            self.description = args[3]

    def __str__(self) -> str:
        result = ""
        result += f"Фамилия: {self.last_name}\n"
        result += f"Имя: {self.first_name}\n"
        result += f"Телефон: {self.phone_number}\n"
        result += f"Описание: {self.description}\n"
        return result

    def set(self, attr, val):
        setattr(self, attr, val)

    def get_values(self):
        return (self.last_name, self.first_name,
                self.phone_number, self.description)


class Phonebook():
    items = []
    attrs = []

    def __init__(self, src=DEFAULT_CSV_FILE) -> None:
        if not exists(src):
            with open(src, 'w', encoding='utf-8') as f:
                f.write(m.PHONEBOOK_HEADER)
        with open(src, 'r', encoding='utf-8') as f:
            csvreader = reader(f, delimiter=CSV_DELIMITER, quotechar='|')
            self.attrs = next(csvreader)
            for row in csvreader:
                item = Person(row)
                self.items.append(item)

    def __str__(self) -> str:
        if self.items:
            result = m.PHONEBOOK_PROMPT_MSG
            for item in self.items:
                result += str(item) + "\n"
            return result
        return m.PHONEBOOK_EMPTY_MSG

    def add(self, person):
        self.items.append(person)

    def _save_csv(self):
        with open(DEFAULT_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            csvwriter = writer(f, delimiter=CSV_DELIMITER, quotechar='|')
            csvwriter.writerow(self.attrs)
            for item in self.items:
                csvwriter.writerow(item.get_values())

    def _save_txt(self):
        with open(DEFAULT_TXT_FILE, 'w', encoding='utf-8') as f:
            csvwriter = writer(f, delimiter=TXT_DELIMITER, quotechar='|')
            for item in self.items:
                csvwriter.writerow(item.get_values())

    def save(self):
        self._save_csv()
        self._save_txt()
