# Первая работа
```@startuml "Практическая работа 1"
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
![alt text](https://github.com/AndrewKom/TMP/blob/main/1.png)

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
![alt text](https://github.com/AndrewKom/TMP/blob/main/2.png)
