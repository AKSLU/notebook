from tkinter import *
import os

root = Tk()
root.title("Блокнот")
root.geometry("400x400")

path_lalbel = Label(root,text="Написать название с раширением")
path_lalbel.pack(fill=X, padx=5, pady=5)
path_entry = Entry(root)
path_entry.pack(fill=X, padx=10, pady=10)

text = Text(root, wrap="word", undo=True)
text.pack(expand=True, fill=BOTH)

file_path = None 


def new_file():
    global file_path
    file_path = None
    path_entry.delete(0, END)
    text.delete(1.0, END)
    root.title("Блокнот - Новый файл")


def open_file():
    global file_path
    file_path = path_entry.get().strip()
    if file_path and os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text.delete(1.0, END)
            text.insert(1.0, f.read())
        root.title(f"Блокнот - {os.path.basename(file_path)}")
    else:
        root.title("Блокнот - файл не найден")


def save_file():
    global file_path
    file_path = path_entry.get().strip()
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get(1.0, END))
        root.title(f"Блокнот - {os.path.basename(file_path)}")
    else:
        root.title("Блокнот - укажите путь к файлу")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)

file_menu.add_command(label="Создать", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)

root.mainloop()
