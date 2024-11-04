import xml.etree.ElementTree as ET
import json


DATASET_PATH = 'currency.xml'
OUT_PATH2 = "outCrrml.txt"


with open(DATASET_PATH, 'r', encoding='windows-1251') as file:
    xml_data = file.read()

read = ET.fromstring(xml_data)

print(f"Date: {read.attrib['Date']}")
print(f"Name of the Marking: {read.attrib['name']}")


def get_data(): 
    with open(DATASET_PATH, 'r', encoding='windows-1251') as file: 
        xml_data = file.read()

    root = ET.fromstring(xml_data) 
    valutes = root.findall('Valute') 
    print(f'Amount of Valute: {len(valutes)}') 

    fields = [] 

    for valute in read.findall('Valute'):
        id_valute = valute.attrib['ID']
        num_code = valute.find('NumCode').text
        char_code = valute.find('CharCode').text
        nominal = valute.find('Nominal').text
        name = valute.find('Name').text
        value = valute.find('Value').text
        unit_rate = valute.find('VunitRate').text
        field = [] 

        field.append( f'ID: {id_valute}')
        field.append( f'Number code: {num_code}')
        field.append( f'Currency: {char_code}')
        field.append( f'Nominal: {nominal}')
        field.append( f'Name: {name}')
        field.append( f'Value: {value}')
        field.append( f'Unit Rate: {unit_rate}')

        if nominal == '1':
            fields.append(field) 

 
    return fields 


if __name__ == "__main__": 
    with open(DATASET_PATH, encoding='windows-1251') as file:        
        res3 = get_data() 
        res3 = json.dumps(res3, indent=4, ensure_ascii=False) 
        with open(OUT_PATH2, "w", encoding="utf-8") as out: 
            out.write(res3)