import csv
import os
from os import system

def new_phonebook(file_csv): # Добавление нового справочника
    with open(file_csv, 'w', newline='') as csvfile:
        fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'id': '1', 'First_Name': 'Ivan', 
            'Last_Name': 'Ivanov', 'Number': '89991234567', 'Description': 'Teacher'})
        writer.writerow({'id': '2', 'First_Name': 'Petr', 
            'Last_Name': 'Petrov', 'Number': '89993234567', 'Description': 'Director'})
        writer.writerow({'id': '3', 'First_Name': 'Sergei', 
            'Last_Name': 'Sidorov', 'Number': '89995234567', 'Description': 'HomeWorker'})

def read_phonebook_and_display(file_csv): # Вывод справочника на экран
    with open(file_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['id'], row['First_Name'], row['Last_Name'], row['Number'], row['Description'])

def read_phonebook_and_write_csv_file(file_csv_new, file_csv): # Импортирование нового справочника(csv файл) в основной справочник
    last_id = read_last_id() + 1
    with open(file_csv_new, newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv, 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            for row in reader:
                writer.writerow({'id': last_id, 'First_Name': row['First_Name'], 
                    'Last_Name': row['Last_Name'], 'Number': row['Number'], 
                    'Description': row['Description']})
                last_id = last_id + 1

def add_new_contact_in_phonebook(new_contact): # Добавление нового контакта не из csv
    last_id = read_last_id() + 1
    with open('telephone.csv', 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writerow({'id': last_id, 'First_Name': new_contact[0], 
                'Last_Name': new_contact[1], 'Number': new_contact[2], 
                'Description': new_contact[3]})

def read_last_id(): # Считывание последнего ID
    with open('telephone.csv', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line[0].split(',')
        last_id = int(last_line[0])
        return last_id

def import_phonebook_txt_file(file_txt): # Вызов метода добавление контактов из txt файла
    with open(file_txt, 'r') as file:
        count = 0
        new_contact = []
        lines = file.readlines()
        for line in lines:
            if line.strip() == '':
                count = count
            else:
                new_contact.append(line.strip())
                count = count + 1          
            if count == 4:
                add_new_contact_in_phonebook(new_contact)
                count = 0
                new_contact = []
            else:
                continue

def new_contact_keyboard_input(): # Вызов метода набора контакта с клавиатуры
    print('С клавиатуры Имя/Фамилия/Номер/Описание')
    new_contact = []
    for i in range(4):
        new_contact.append(str(input()))
    add_new_contact_in_phonebook(new_contact)

def export_phonebook_txt_file(file_txt):
    with open('telephone.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            with open(file_txt, 'a') as txtfile:
                stroka = ''
                stroka = str(row)
                txtfile.write(f'{stroka} \n')
