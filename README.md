# Нулевая работа
```
@startuml "Практическая работа 0"
left to right direction
skinparam backgroundcolor AntiqueWhite/Gold
rectangle Касса {
Покупатель -- (Покупает товары)
Покупатель -- (Забирает товары)
(Оплачивает товары) <.. (Покупает товары)
Продавец -- (Включает терминал)
(Оплачивает товары) <. (Включает терминал)
банк -- (проверить наличие средств)
банк -- (Подтверждает покупку)
(проверить наличие средств) <. (Оплачивает товары)
(Подтверждает покупку) <. (проверить наличие средств)
(Забирает товары) <. (Подтверждает покупку)
}
@enduml
```
![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/0.png)

# Первая практическая работа "Система учета рабочего времени"
```
@startuml "Практическая работа 1"
left to right direction
title Система учета рабочего времени
skinparam backgroundcolor AntiqueWhite/Gold
actor Руководитель
actor Исполнитель

rectangle Система {
Руководитель -- (Выдавать задание)
(Выдавать задание) ..>(Выполнять задание):<<include>>
(Выдавать задание) ..> (Отслеживать выполнение):<<include>>
Исполнитель -- (Выполнять задание)
(Выполнять задание) ..> (Вести учет времени):<<include>>
}
@enduml
```
![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/1.png)

```
@startuml
class Руководитель{
+Паспортные данные
+ФИО
+Должность
Выдача задания()
Проверка Статуса()
}

class Задание{
+Номер задания
+Кто выдал задание
+Исполнитель задания
+Время исполнения задания

}

class Исполнитель{
+Паспортные данные
+ФИО
+Должность
Выполнение задания()
Изменение статуса()
Проверка времени()
}
class СтатусЗадания{
+Номер задания
+Статус задания
}
class ВремяЗадания{
+Номер задания
+Время
}

Руководитель --> Задание:Выдает
Исполнитель --> Задание:Выполняет
Исполнитель --> СтатусЗадания:Изменяет статус
Исполнитель -- ВремяЗадания:Проверять
Руководитель -- СтатусЗадания:Проверяет статус
Задание..>СтатусЗадания
Задание..>ВремяЗадания
@enduml
```
![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/2.png)


# Вторая практическая работа: Диаграмма последовательности и развертывания
```
@startuml "Практическая работа 2"
title Система учета рабочего времени: диаграмма последовательности
skinparam backgroundcolor AntiqueWhite/Gold
participant Руководитель
participant Задание
participant Исполнитель
participant Таймер
activate Руководитель

Руководитель -> Задание: Описывает задание
activate Задание
Руководитель -> Исполнитель: Выдает задание
deactivate Руководитель
activate Исполнитель
Исполнитель -> Таймер:Включает таймер для отслеживания времени
activate Таймер
Исполнитель -> Задание:Приступает к выполнению
Исполнитель -> Задание:Выполняет задание
deactivate Задание
Исполнитель -> Таймер:Закрепляет время выполнения
deactivate Таймер
Исполнитель -> Руководитель:Сообщает о выполнении задания
deactivate Исполнитель
activate Руководитель
Руководитель -> Задание:Проверка качества выполнения
activate Задание
Задание -> Руководитель:Корректное выполнение задания
Руководитель -> Задание:Принимает задание
deactivate Руководитель
deactivate Задание

@enduml
```

![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/work2.png)

```
@startuml "Практическая работа 2.2"
left to right direction
title Система учета рабочего времени: диаграмма развертывания
skinparam backgroundcolor AntiqueWhite/Gold
database Задания
node ПК_Исполнитель
node ПК_Руководитель
node Таймер
node Система_контроля

ПК_Исполнитель - Задания: Выполняют
ПК_Руководитель - Задания: Выдают
ПК_Исполнитель - Таймер: Используют
ПК_Руководитель - Система_контроля: Проверка выполнения задания
Система_контроля - Задания
@enduml
```
![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/work2.2.png)

# Практическая работа 3: Strategy and Template Method
Strategy: https://github.com/AndrewKom/TMPStrategy

![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/work3.2.png)

Template Method: https://github.com/AndrewKom/TMPTemplate_Method/tree/main

![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/work3.1.png)



# Практическая работа 4: Iterator pattern and Visitor
Iterator pattern: https://github.com/AndrewKom/TMP/blob/main/Программы/pr4.1.py

![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/work4.1.png)

Visitor:https://github.com/AndrewKom/TMP/blob/main/Программы/pr4.2.py

![alt text](https://github.com/AndrewKom/TMP/blob/main/Фото/work4.2.png)

# Практическая работа 5: Abstract Factory and Builder and Adapter and Intermediary

Abstract Factory: https://github.com/AndrewKom/TMP/blob/main/Программы/pr5.1.py

Builder:https://github.com/AndrewKom/TMP/blob/main/Программы/pr5.2.py

Adapter: https://github.com/AndrewKom/TMP/blob/main/Программы/5.3.py

Mediator: https://github.com/AndrewKom/TMP/blob/main/Программы/pr5.4.py

# Практическая работа 6: Inversion of control, Proxy, Composite

Inversion of control: 

Proxy: https://github.com/AndrewKom/TMP/blob/main/Программы/pr6.2.py

Composite: https://github.com/AndrewKom/TMP/blob/main/Программы/pr6.3.py



