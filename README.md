# Task_1

Данный проект решает задачу по хранению данных и получению аналитики о студентах.

## Использованные технологии

* **Python**
  <br>Основной язык, на котором написана большая часть всего проекта.
* **PostgreSQL**
  <br>Для хранения информации используется база данных PostgreSQL.
* **Docker**
  <br>Для проекта были написаны Docker и Docker-compose файлы, что позволяет быстро разворачивать его на любой машине.
* **Unit tests**
  <br>Выполнено покрытие проекта unit тестами, что позволяет эффективно и быстро отслеживать корректность работы основного функционала в случае внесения каких-либо изменений либо дополнений в код.

## Требования к проекту

* Для передачи параметров для подключения к БД, а также передачи директорий с SQL запросами используются переменные окружения.
* Входные данные о студентах и комнатах должны быть JSON файлами предопределенной структуры.

## Возможности проекта

* Может возвращать результаты запросов в JSON или XML формате на выбор.
* Предварительное создание таблиц необходимой структуры перед загрузкой данных не обязательно, они создаются автоматически.
* Благодаря Docker-compose может быть быстро запущен на любом устройстве.

## Запуск проекта

1. Создать файл окружения с соответствующими переменными окружения и присвоить им необходимые значения (имя базы данных, пароль, хост и т.д., пути до файлов с данными и запросами).
2. Запустить Docker.
3. Перейти в корневую директорию проекта.
4. Запустить docker-compose файл при помощи команды:

   ```sh
   docker-compose up



  
