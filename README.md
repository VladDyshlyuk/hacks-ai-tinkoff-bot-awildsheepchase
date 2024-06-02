##API Endpoint 

https://tcp-reads-targets-handbags.trycloudflare.com/

# Tinkoff Bot
Решение команды AWildSheepChase на Цифровой Прорыв Сезон ИИ ДФО 2024 Кейс 5 «Бот - Тинькофф»

## [Зависимости](/requirements.txt)

## [Работа с API](https//:github.com/VladDyshlyuk/hacks-ai-tinkoff-bot-awildsheepchase/api)

Запуск апишки [app.py](/api/app.py)

Делает запрос к Янекс GPT и получает контекстный ответ [model_answer.py](/api/model_answer.py)

Объявление базы данных и её основных методов[vector_db.py](/api/vector_db.py)

## [Создание эмбедингов и загрузка векторной БД](/dataloader)

Создание таблиц БД [create_db.py](/dataloader/create_db.py)

Загрузка БД[data_loader_to_db.py](/dataloader/data_loader_to_db.py)

Объявление базы данных и её основных методов [vector_db.py](/api/vector_db.py)

Используемые датасеты [datasets](/dataloader/datasets)

## [Создание эмбедингов и загрузка векторной БД](/frontend-demo)

Файл разметки интерфейса [index.html](/frontend-demo/index.html)

Скрипт интерфейса [script.js](/frontend-demo/script.js)

Файл со стилями к интерфейсу [style.css](/frontend-demo/style.css)

## [Создание метрик](/metrics)

Создание валидационного датасета и сравнение ответов модели [calculate-metric.ipyn](/metrics/calculate-metric.ipynb)

Наши метрики [metrics-results.json](/metrics/metrics-results.json)
