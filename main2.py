import xml.etree.ElementTree as ET

DATASET_PATH = 'currency.xml'

with open(DATASET_PATH, 'r', encoding='windows-1251') as file:
    xml_data = file.read()

read = ET.fromstring(xml_data)

print(f"Fecha: {read.attrib['Date']}")
print(f"Nombre del mercado: {read.attrib['name']}\n")


for valute in read.findall('Valute'):
    id_valute = valute.attrib['ID']
    num_code = valute.find('NumCode').text
    char_code = valute.find('CharCode').text
    nominal = valute.find('Nominal').text
    name = valute.find('Name').text
    value = valute.find('Value').text
    unit_rate = valute.find('VunitRate').text

    print(f"ID: {id_valute}")
    print(f"Number code: {num_code}")
    print(f"Currency: {char_code}")
    print(f"Nominal: {nominal}")
    print(f"Name: {name}")
    print(f"Value: {value}")
    print(f"Unit Rate: {unit_rate}\n")
