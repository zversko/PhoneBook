import csv
import os
import my_modules
from os import system

def choice_method(num): # Выбор метода
    if num == 1:
        system("cls")
        my_modules.new_phonebook('telephone.csv')
        main()
        exit()
    elif num == 2:
        os.system('dir')
        main()
        exit()
    elif num == 3:
        system("cls")
        my_modules.read_phonebook_and_display('telephone.csv')
        print('')
        main()
        exit()
    elif num == 4:
        system("cls")
        file_csv_new = input('Введите файл *.csv > ')
        my_modules.read_phonebook_and_write_csv_file(file_csv_new, 'telephone.csv')
        main()
        exit()
    elif num == 5:
        system("cls")
        file_txt = input('Введите файл *.txt > ')
        my_modules.import_phonebook_txt_file(file_txt)
        main()
        exit()
    elif num == 6:
        my_modules.new_contact_keyboard_input()
        main()
        exit()
    elif num == 7:
        system("cls")
        file_txt = input('Введите файл *.txt > ')
        my_modules.export_phonebook_txt_file(file_txt)
        main()
        exit()
    elif num == 8:
        exit()
    
def main(): # Меню
    print('Добро пожаловать в телефонный справочник! \n Выберите один из пунктов:')
    print('1. Создать новый телефонный справочник (telephone.csv)')
    print('2. Вывести список файлов в папке на экран ')
    print('3. Вывести основной телефонный справочник на экран')
    print('4. Импортировать справочник из csv файла')
    print('5. Импортировать справочник из txt файла')
    print('6. Ввести новый контакт с клавиатуры ')
    print('7. Экспортировать основной справочник в txt файл')
    print('8. Выход \n')
    num = input('Введите число от 1 до 8 > ')
    try:
        num = int(num)
    except:
        system("cls")
        print('Это не число')
        main()
        exit()
    if 1 <= int(num) <= 8:
        choice_method(num)
    else:
        system("cls")
        print('Неправильное число')
        main()
        exit()
    
main()

