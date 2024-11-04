# from csv import reader


# output = open('result.txt', 'w')

# while True:
#     flag = 0
#     search = input('Введите запрос: ')
#     if search == '0':
#         break
#     with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
#         table = reader(csvfile, delimiter=';')
#         for row in table:
#             lower_case = row[2].lower()
#             index = lower_case.find(search.lower())
#             if index != -1:
#                 print(row[2])
#                 output.write(f'{row[2]}. Цена {row[8]} руб. S/n {row[18]}\n')
#                 flag += 1



#         if flag == 0:
#             print('Ничего не найдено.')
#         else:
#             print(f'Найдено {flag} результатов.')

# output.close()


import csv
import json
import random

DATASET_PATH = "books-en.csv"
OUT_PATH = "outlab2.json"
OUT_BIO = "outBIO.txt"

Name_Autor = input("Aвтор: ")

def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(";")
    title = [col.strip() for col in title]
    return title

def get_year(dataset):
    dataset.seek(0)
    year = next(dataset)
    year = year.split(";")
    year = [col.strip() for col in year]
    return year

def get_autor(dataset):
    dataset.seek(0)
    autor = next(dataset)
    autor = autor.split(";")
    autor = [col.strip() for col in autor]
    return autor

def r_csv(dataset):
    lector_csv = csv.reader(dataset, delimiter=';')
    next(lector_csv)
    return list(lector_csv)

def get_object_alt(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    result = next(reader)
    return result

def get_objecttl(line, title):
    fields = []
    value = ""
    in_complex = False

    for char in line:
        if in_complex: 
            value += char
            if char == '"':
                value = value[:-1]
                fields.append(value)
                value = ''
                in_complex = False
        else:
            if char not in (';', '"'):
                value += char
                continue
            if char == ';':
                fields.append(value)
                value = ''
                continue
            if char == '"':
                in_complex = True
                continue

    result = {col: f for col, f in zip(title, fields)}
    return result

def get_objectyr(line, year):
    fields = []
    value = ""
    in_complex = False

    for char in line:
        if in_complex: 
            value += char
            if char == '"':
                value = value[:-1]
                fields.append(value)
                value = ''
                in_complex = False
        else:
            if char not in (';', '"'):
                value += char
                continue
            if char == ';':
                fields.append(value)
                value = ''
                continue
            if char == '"':
                in_complex = True
                continue

    result = {col: f for col, f in zip(year, fields)}
    return result

def get_objectaut(line, autor):
    fields = []
    value = ""
    in_complex = False

    for char in line:
        if in_complex: 
            value += char
            if char == '"':
                value = value[:-1]
                fields.append(value)
                value = ''
                in_complex = False
        else:
            if char not in (';', '"'):
                value += char
                continue
            if char == ';':
                fields.append(value)
                value = ''
                continue
            if char == '"':
                in_complex = True
                continue

    result = {col: f for col, f in zip(autor, fields)}
    return result

def count_title(dataset, title):
    filtered1 = []
    k = 1
    for line in dataset:
        obj = get_objecttl(line, title)
        title_value = obj.get("Book-Title", "")
        if len(title_value) > 30:
            k += 1
        if title == str(title):
            filtered1.append(obj)
    dataset.seek(0)
    return k

def filter_year_autor(dataset, year, autor):
    filtered = []
    for line in dataset:
        obj1 = get_objectaut(line, autor)
        obj2 = get_objectyr(line, year)
        autor_value = obj1.get("Book-Author", "")
        year_value = obj2.get("Year-Of-Publication", "")

        if year_value < "1990" and autor_value == Name_Autor:
            filtered.append(obj1)

    dataset.seek(0)
    return filtered

def references(book, num_citas=20):
    random_lines = random.sample(book, min(num_citas, len(book)))
    citas = []
    for lines in random_lines:
        ISBN, Title, Author, Year, Publisher, *_ = lines
        referencia = f"Line {book.index(lines)+2}: {Author}, ({Year}), {Title}, {Publisher}, ISBN: {ISBN}"
        citas.append(referencia)
    return citas

if __name__ == "__main__":

    with open(DATASET_PATH, encoding="windows-1251") as dataset:
        title = get_title(dataset)
        year = get_year(dataset)
        res = count_title(dataset, title)
        res2 = filter_year_autor(dataset, year, title)

        print(f'B поле "Название" строка длиной более 30 символов равна: {res}')

        res2 = json.dumps(res2, indent=4, ensure_ascii=False)
        with open(OUT_PATH, "w", encoding="utf-8") as out:
            out.write(res2)

    with open(DATASET_PATH, encoding="windows-1251") as dataset:
        res4 = r_csv(dataset) 
        res4 = references(res4)

        with open(OUT_BIO, 'w', encoding='utf-8') as archivo_txt:
            for cita in res4:
                archivo_txt.write(cita + '\n')