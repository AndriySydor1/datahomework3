from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Завантаження змінних середовища з .env
load_dotenv()

# Отримання URI з .env
uri = os.getenv("MONGO_URI")

# Підключення до MongoDB
client = MongoClient(uri)
db = client['cats_database']
collection = db['cats']
# Приклад роботи з базою даних
print("Підключення встановлено!")

# Створення (Create)
def create_cat(name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Створено запис з ID: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при створенні запису: {e}")

# Читання (Read)
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні записів: {e}")

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")

# Оновлення (Update)
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count:
            print(f"Вік кота {name} оновлено.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при оновленні віку: {e}")

def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count:
            print(f"Характеристика '{feature}' додана до кота {name}.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")

# Видалення (Delete)
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кіт з ім'ям {name} видалений.")
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except Exception as e:
        print(f"Помилка при видаленні всіх записів: {e}")

# Тестові виклики
if __name__ == "__main__":
    # Додати котів
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("murzik", 2, ["сірий", "веселий"])

    # Читання
    read_all_cats()
    read_cat_by_name("barsik")

    # Оновлення
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любить рибу")

    # Видалення
    delete_cat_by_name("murzik")
    