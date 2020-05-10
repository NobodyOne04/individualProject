**Описание**
====================
* Проект реализует веб интерфейс с доступом к библиотеке pymorphy2
1. Что умеет?
* 1) Преобразовывать слова в нормальную форму
* 2) Переводить слова в нужную форму. Например: ед.ч, и.п
* 3) Определять морфологические свойства слова   

**Запуск**
=====================
1. Установка зависимостей:
* pip3 install -r requiraments.txt или python3 -m pip install -r requiraments.txt
2. Запуск:
* Запустить сервер с моделью: перейти в директорию проекта,
  приложение python3 manager.py runserver с указанием хоста и порта,
  например:  python3 manager.py runserver 127.0.0.1:8000