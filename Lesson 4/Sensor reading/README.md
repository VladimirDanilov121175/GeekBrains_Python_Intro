# Задача
Написать программу, регистрирующую обращения к датчикам температуры, давления и скорости ветра в журнал с возможностью
вывода журнала в виде HTML или XML файла.  
___

## Модули

### Модуль, имитирующий показания датчиков
Методы: temperature(), pressure(), wind_speed(). 

### Модуль, снимающий показания с датчиков
Методы: get_temperature(), get_pressure(), get_wind_speed(). 

### Модуль записи показаний в журнал
Методы: log_temperature(), log_pressure(), log_wind_speed(). 

### Модуль генерации HTML и XML
Методы: create_html(), create_xml(). 

### Модуль, имитирующий пользовательский интерфейс
Место, где по концепции предполагается логика пользовательского интерфейса, например,
кнопок, по нажатию на 

### Основной модуль, запускающий программу
start_logging()
