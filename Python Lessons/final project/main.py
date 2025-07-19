import os

PHONES_FILE = 'phones.txt'
USERS_FILE = 'users.txt'

def load_phones():
    phones = []
    if os.path.exists(PHONES_FILE):
        with open(PHONES_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('-')
                if len(parts) == 7:
                    phone = {
                        "Издатель": parts[1],
                        "Марка": parts[2],
                        "ОЗУ": parts[3],
                        "Память": parts[4],
                        "Цвет": parts[5],
                        "Цена": parts[6]
                    }
                    phones.append(phone)
    return phones

def save_phones(phones):
    with open(PHONES_FILE, 'w', encoding='utf-8') as f:
        for i, phone in enumerate(phones, start=1):
            line = f"{i}-{phone['Издатель']}-{phone['Марка']}-{phone['ОЗУ']}-{phone['Память']}-{phone['Цвет']}-{phone['Цена']}\n"
            f.write(line)

def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('-')
                if len(parts) == 2:
                    users[parts[0]] = parts[1]
    return users

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        for username, password in users.items():
            f.write(f"{username}-{password}\n")

def setup_default_admin():
    if not os.path.exists(USERS_FILE):
        users = {"admin": "admin"}
        save_users(users)
        print("Создан пользователь admin с паролем admin")

def login():
    users = load_users()
    while True:
        print("=== Вход ===")
        username = input("Логин: ").strip()
        password = input("Пароль: ").strip()
        if username in users and users[username] == password:
            print("Вход успешен!\n")
            return
        else:
            print("Неверный логин или пароль. Попробуйте снова.\n")

def show_phones():
    phones = load_phones()
    if not phones:
        print("Телефонов нет.\n")
        return
    print("=== Телефоны ===")
    for i, phone in enumerate(phones, start=1):
        print(f"{i}. {phone['Издатель']} {phone['Марка']} | Цена: {phone['Цена']}")
    print()

def add_phone():
    phones = load_phones()
    print("=== Добавление телефона ===")
    new_phone = {}
    new_phone['Издатель'] = input("Издатель: ").strip()
    new_phone['Марка'] = input("Марка: ").strip()
    new_phone['ОЗУ'] = input("ОЗУ: ").strip()
    new_phone['Память'] = input("Память: ").strip()
    new_phone['Цвет'] = input("Цвет: ").strip()
    new_phone['Цена'] = input("Цена: ").strip()

    phones.append(new_phone)
    save_phones(phones)
    print("Телефон добавлен!\n")

def delete_phone():
    phones = load_phones()
    if not phones:
        print("Телефонов нет для удаления.\n")
        return

    print("=== Удаление телефона ===")
    for i, phone in enumerate(phones, start=1):
        print(f"{i}. {phone['Издатель']} {phone['Марка']} | Цена: {phone['Цена']}")

    while True:
        choice = input("Введите номер телефона для удаления (или 0 для отмены): ").strip()
        if choice == '0':
            print("Удаление отменено.\n")
            return
        if not choice.isdigit():
            print("Пожалуйста, введите число.")
            continue
        choice = int(choice)
        if 1 <= choice <= len(phones):
            removed = phones.pop(choice - 1)
            save_phones(phones)
            print(f"Телефон '{removed['Издатель']} {removed['Марка']}' удалён.\n")
            return
        else:
            print("Неверный номер. Попробуйте снова.")

def main_menu():
    while True:
        print("=== Главное меню ===")
        print("1. Показать телефоны")
        print("2. Добавить телефон")
        print("3. Удалить телефон")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            show_phones()
        elif choice == '2':
            add_phone()
        elif choice == '3':
            delete_phone()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    setup_default_admin()
    login()
    main_menu()
