# MongoDB CRUD Operations

## Опис

Цей проект реалізує базові CRUD-операції з використанням MongoDB для управління даними про котів.

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

## Інструкція з запуску

### Підготовка

1. Перейдіть до папки mongo_crud:
   cd mongo_crud
2. Створіть файл .env у цій папці з вмістом:
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority

### Запуск

Запустіть скрипт:
python main.py

## Залежності

Python 3.10+
pymongo
python-dotenv
