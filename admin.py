class Admin:
    def __init__(self):
        print("""Добро пожаловать в электронную библиотеку!
Для выбора напишите цифру функции из меню и нажмите "Enter".""")

    def print_menu(self):
         print("""
Меню:
1) Создать папку с книгой. 
2) Добавить главу к уже существующей книге. 
3) Дописать главу выбранной книги. 
4) Удаление какой либо главы, выбранной книги. 
5) Удаление книги. 
6)Просмотр всех книг из библиотеки 
Просто нажмите "Enter" если хотите выйти из электронной библиотеки.
""")

