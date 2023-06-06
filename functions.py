def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))

def edit_data(book.txt):
    """Изменяет информацию из файла"""
print(f'\n{num} |{fio} | {phone_num}')
with open(book.txt, "r", encoding="utf-8") as file:
data = file.read()
print(data)
print("")
index_delete_data = int(input("Введите номер строки для редактирования: ")) — 1
data_lines = data.split("\n")
edit_data_lines = data_lines[index_delete_data]
elements = edit_data_lines.split(" | ")
fio = input("Введите ФИО: ")
phone_num = input("Введите номер телефона: ")
    num = elements[0]
       if len(fio) == 0:
          fio = elements[1]
             if len(phone_num) == 0:
               phone_num = elements[2]
edited_line = (f"{num} | {fio} | {phone_num}")
data_lines[index_delete_data] = edited_line
print(f"Запись — {edit_data_lines}, изменена на — {edited_line}\n")
with open(book.txt, «w», encoding=’utf-8′) as data:
     data.write("\n".join(data_lines))
        
def delete_data(book.txt):
     """Удаляет информацию из файла"""
print(f'\n{num} | {fio} | {phone_num}')
with open(book.txt, «r», encoding=»utf-8″) as file:
data = file.read()
print(data)
print("")
index_delete_data = int(input("Введите номер строки для удаления: ")) — 1
data_lines = data.split("\n")
del_data_lines = data_lines[index_delete_data]
data_lines.pop(index_delete_data)
print(f"Удалена запись: {del_data_lines}\n")
with open(book.txt, «w», encoding=’utf-8′) as data:
data.write("\n".join(data_lines))

