# API-example

## EN
* run the main script via "python3 main.py"
* follow the specified link in the log, for example http://0.0.0.0:8000
* to view the documentation, go to "some_links/docs", for example http://0.0.0.0:8000/docs

### Routing
  * /getWorkerByBoss/bossname - Get an employee by the name of his boss
  * /getWorkerByCustomer/customer_name - Get an employee by his position
    * /Дизайнер - Designer
    * /Разработчик - Developer
    * /Бэкенд-разработчик - Backend developer
    * /Фронтенд разработчик - Frontend developer
    * /Менеджер - Manager
    * /Системный администратор - System Administrator
    * /Тестировщик - Tester
  * /salaryEquals(More Less)/salary - Sort by salary
  * /workerName/name - Get a specific employee by name
  * /workers - shows the hierarchy of employees

* to change the database, edit the "sql.db" file

## RU
* запустите основной скрипт через "python3 main.py "
* перейдите по указанной ссылке в журнале, например http://0.0.0.0:8000
* чтобы просмотреть документацию, перейдите в раздел "some_links/docs", например http://0.0.0.0:8000/docs

### Маршрутизация
 * /getWorkerByBoss/bossname - Получить сотрудника по имени его босса
 * /getWorkerByCustomer/customer_name - Получить сотрудника по его должности
   * /Дизайнер - Дизайнер
   * /Разработчик - Разработчик
   * /Бэкенд-разработчик - Серверный разработчик
   * /Фронтенд разработчик - Разработчик внешнего интерфейса
   * /Менеджер - Менеджер
   * /Системный администратор - Системный администратор
   * /Тестировщик - Тестер
 * /salaryEquals(More Less)/salary - Сортировка по зарплате
 * /workerName/name - Получить конкретного сотрудника по имени
 * /workers - показывает иерархию сотрудников

* чтобы изменить базу данных, отредактируйте файл "sql.db"
