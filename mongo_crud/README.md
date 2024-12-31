# MongoDB CRUD Operations

## Опис

Цей проєкт реалізує базові CRUD-операції з використанням MongoDB для управління даними про котів.
Дані зберігаються у колекції cats бази даних cats_database.

## Передумови

1. MogoDB Atlas.
   Потрібен обліковий запис MongoDB Atlas.
   Кластер із базою даних cats_database.
2. Файл exported_cats.json:
   Містить дані для колекції cats.
3. Необхідні бібліотеки:
   pymongo
   python-dotenv

## Структура документа

Кожен документ у колекції `cats` має таку структуру:

```json
{
  "_id": "ObjectId",
  "name": "barsik",
  "age": 3,
  "features": ["ходить в капці", "дає себе гладити", "рудий"]
}
```

## Інструкції

1. Імпорт даних із exported_cats.json у MongoDB
   Встановіть MongoDB Database Tools і виконайте команду:
   mongoimport --uri="<MONGO_URI>" --collection=cats --file=exported_cats.json --jsonArray  
   де <MONGO_URI> - ваш MongoDB URI.
2. Створіть файл .env зі змінною:
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/
   де <username>, <password> та <cluster-url> - облікові дані MongoDB Atlas.
3. Використання main.py
   Запустіть скрипт main.py, щоб виконувати CRUD-операції.
   python main.py

### Приклад використання

Після запуску скрипта вам буде запропоновано меню:

1. Вивести всі записи
2. Знайти запис за ім'ям
3. Оновити вік за ім'ям
4. Додати характеристику за ім'ям
5. Видалити запис за ім'ям
6. Видалити всі записи
7. Вийти
