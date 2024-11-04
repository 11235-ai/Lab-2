# import csv
# import json

# DATASET_PATH = "memes_dataset.csv"
# OUT_PATH = "out.json"


# def get_title(dataset):
#     dataset.seek(0)
#     title = next(dataset)
#     title = title.split(",")
#     title = [col.strip() for col in title]

#     return title


# def get_object_alt(line, title):
#     reader = csv.DictReader([line], title, delimiter=',', quotechar='"')
#     result = next(reader)
#     return result


# def get_object(line, title):
#     fields = []
#     value = ""
#     in_complex = False

#     for char in line:
#         if in_complex: 
#             value += char

#             if char == '"':
#                 value = value[:-1]
#                 fields.append(value)
#                 value = ''
#                 in_complex = False
#         else:
#             if char not in (',', '"'):
#                 value += char
#                 continue
            
#             if char == ',':
#                 fields.append(value)
#                 value = ''
#                 continue
            
#             if char == '"':
#                 in_complex = True
#                 continue

#     result = {col: f for col, f in zip(title, fields)}
#     return result


# def filter_year(dataset, title, year):
#     filtered = []

#     for line in dataset:
#         obj = get_object(line, title)
#         year_value = obj["origin_year"]

#         if year_value == str(year):
#             filtered += [obj]

#     dataset.seek(0)
#     return filtered


# if __name__ == "__main__":
#     with open(DATASET_PATH, encoding="utf-8") as dataset:
#         title = get_title(dataset)

#         res = filter_year(dataset, title, 1990)
#         print(len(res))
#         # for r in res:
#         #     print(r)

#         # line = next(dataset)
#         # res = get_object_alt(line, title)

#         # print(res)

#         res = json.dumps(res, indent=4)
#         with open(OUT_PATH, "w") as out:
#             out.write(res)
