##API Endpoint 

https://tcp-reads-targets-handbags.trycloudflare.com/

# Tinkoff Bot
Решение команды AWildSheepChase на Цифровой Прорыв Сезон ИИ ДФО 2024 Кейс 5 «Бот - Тинькофф»

## Зависимости
[ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/requirements.txt
)
## Работа с API [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/api)

Запуск апишки [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/api/app.py)
Делает запрос к Янекс GPT и получает контекстный ответ [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/api/model_answer.py)
Объявление базы данных и её основных методов[ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/api/vector_db.py)

## Создание эмбедингов и загрузка векторной БД [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/dataloader)

Создание таблиц БД [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/dataloader/create_db.py)
Загрузка БД[ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/dataloader/data_loader_to_db.py)
Объявление базы данных и её основных методов [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/api/vector_db.py)
Используемые датасеты [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/dataloader/datasets)

## Создание эмбедингов и загрузка векторной БД [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/frontend-demo)

Файл разметки интерфейса [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/frontend-demo/index.html)
Скрипт интерфейса [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/frontend-demo/script.js)
Файл со стилями к интерфейсу [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/frontend-demo/style.css)

## Создание метрик [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/metrics)

Создание валидационного датасета и сравнение ответов модели [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/metrics/calculate-metric.ipynb)
Наши метрики [ссылка](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/metrics/metrics-results.json)
