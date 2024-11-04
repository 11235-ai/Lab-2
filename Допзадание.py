import csv
import json

DATASET_PATH = "books-en.csv"
OUT_PATH = "outPlus.json"
OUT2_PATH = "outPlus2.json"

def get_publisher(dataset):
    dataset.seek(0)
    publisher = next(dataset)
    publisher = publisher.split(";")
    publisher = [col.strip() for col in publisher]
    return publisher

def get_objectpubli(line, publisher):
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

    result = {col: f for col, f in zip(publisher, fields)}
    return result

def filter_publisher(dataset, publisher): 
    publishers_set = []
    for line in dataset:
        obj1 = get_objectpubli(line, publisher)
        publisher_value = obj1["Publisher"]
        if publisher_value and publisher_value not in publishers_set:
            publishers_set.append(publisher_value)
    dataset.seek(0)    
    return publishers_set  

def get_topbooks(dataset_path, top):
    books = []
    with open(dataset_path, encoding="windows-1251") as dataset:  
        reader = csv.DictReader(dataset, delimiter=';')
        for row in reader:
            book_name = row["Book-Title"].strip()
            downloads_value = int(row["Downloads"].replace(",", "").strip()) 
            books.append({"Book-Title": book_name, "Downloads": downloads_value})
    books.sort(key=lambda x: x["Downloads"], reverse=True)
    return books[:top]

if __name__ == "__main__":
    with open(DATASET_PATH, encoding="windows-1251") as dataset: 
        title = get_publisher(dataset)
        res = filter_publisher(dataset, title)

        res = json.dumps(res, indent=4, ensure_ascii=False)
        with open(OUT_PATH, "w", encoding="utf-8") as out:
            out.write(res)

    with open(DATASET_PATH, encoding="windows-1251") as dataset: 
        top_books = get_topbooks(DATASET_PATH, top=20)
        top_books = json.dumps(top_books, indent=4, ensure_ascii=False)
        with open(OUT2_PATH, "w", encoding="utf-8") as out:
            out.write(top_books)

            