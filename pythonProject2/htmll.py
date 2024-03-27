import redis
import json

red = redis.Redis(
    host="127.0.0.1",
    port=6379,
)



dict1 = {}  # создаём словарь для записи

c="0" #Создаем переменную для выхода из цикла
while c=="0":
    de=input("deystfie")
    if de=="1":
        a=input("Name")
        b=input("Nomer")
        dict1[a]=b
        c=input("введите 0 если хотите проолжить иначе 1")

    elif de=="2":
        a=input("Name")
        b=dict1[a]
        print(b)
        c = input("введите 0 если хотите проолжить иначе 1")
    elif de=="3":
        a = input("Name")
        del dict1[a]
        c = input("введите 0 если хотите проолжить иначе 1")




red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1'))
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание


red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))