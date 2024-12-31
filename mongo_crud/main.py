import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Завантаження змінних середовища
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Підключення до MongoDB
client = MongoClient(MONGO_URI)
db = client["cats_database"]
collection = db["cats"]

# Читання (Read)
def read_all_records():
    """Виводить усі записи з колекції."""
    try:
        records = collection.find()
        for record in records:
            print(record)
    except Exception as e:
        print(f"Помилка під час читання записів: {e}")

def read_record_by_name():
    """Виводить інформацію про кота за введеним ім'ям."""
    try:
        name = input("Введіть ім'я кота: ").strip()
        record = collection.find_one({"name": name})
        if record:
            print(record)
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка під час пошуку запису: {e}")

# Оновлення (Update)
def update_age_by_name():
    """Оновлює вік кота за введеним ім'ям."""
    try:
        name = input("Введіть ім'я кота: ").strip()
        new_age = int(input("Введіть новий вік: "))
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Вік кота '{name}' успішно оновлено.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except ValueError:
        print("Вік повинен бути числом.")
    except Exception as e:
        print(f"Помилка під час оновлення віку: {e}")

def add_feature_by_name():
    """Додає нову характеристику до списку features кота за введеним ім'ям."""
    try:
        name = input("Введіть ім'я кота: ").strip()
        new_feature = input("Введіть нову характеристику: ").strip()
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.modified_count > 0:
            print(f"Характеристика додана коту '{name}'.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка під час додавання характеристики: {e}")

# Видалення (Delete)
def delete_record_by_name():
    """Видаляє запис з колекції за введеним ім'ям."""
    try:
        name = input("Введіть ім'я кота для видалення: ").strip()
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям '{name}' видалений.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка під час видалення запису: {e}")

def delete_all_records():
    """Видаляє всі записи з колекції."""
    try:
        confirm = input("Ви впевнені, що хочете видалити всі записи? (так/ні): ").strip().lower()
        if confirm == "так":
            result = collection.delete_many({})
            print(f"Усі записи видалено. Видалено {result.deleted_count} записів.")
        else:
            print("Операцію скасовано.")
    except Exception as e:
        print(f"Помилка під час видалення всіх записів: {e}")

# Меню для виклику функцій
def main():
    while True:
        print("\nМеню:")
        print("1. Вивести всі записи")
        print("2. Знайти запис за ім'ям")
        print("3. Оновити вік за ім'ям")
        print("4. Додати характеристику за ім'ям")
        print("5. Видалити запис за ім'ям")
        print("6. Видалити всі записи")
        print("7. Вийти")

        choice = input("Виберіть опцію: ").strip()

        if choice == "1":
            read_all_records()
        elif choice == "2":
            read_record_by_name()
        elif choice == "3":
            update_age_by_name()
        elif choice == "4":
            add_feature_by_name()
        elif choice == "5":
            delete_record_by_name()
        elif choice == "6":
            delete_all_records()
        elif choice == "7":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

    