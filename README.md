**Описание**
====================
* Проект реализует веб приложение
  для морфологического разбора с использованием библиотеки pymorphy2
* Что умеет?
  * Преобразовывать слова в нормальную форму (ед.ч, И.П)
  * Переводить слова в нужную форму. Например: (мн.ч, В.П)
  * Определять морфологические свойства слова 

**Запуск**
=====================
* Установка зависимостей:
    * pip3 install -r requiraments.txt или python3 -m pip install -r requiraments.txt, 
     иначе смотреть руководство python3 pip
* Запуск:
    * Перейти в директорию проекта,
    * Запуск сервера: python3 manager.py runserver с указанием хоста и порта.
      Например:  python3 manager.py runserver 127.0.0.1:8000

**Примечание**
===================== 
* Обоснование использования паттерна Singleton находится в docs/description.txt,
  диаграмма классов в той же папке(docs)