from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Блокнот")
root.geometry("600x400")

text = Text(root, wrap="word", undo=True)
text.pack(expand=True, fill=BOTH)

file_path = None  


def new_file():
    global file_path
    file_path = None
    text.delete(1.0, END)
    root.title("Блокнот - Новый файл")


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text.delete(1.0, END)
            text.insert(1.0, f.read())
        root.title(f"Блокнот - {os.path.basename(file_path)}")


def save_file():
    global file_path
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get(1.0, END))
    else:
        save_file_as()


def save_file_as():
    global file_path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get(1.0, END))
        root.title(f"Блокнот - {os.path.basename(file_path)}")


menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)

file_menu.add_command(label="Создать", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Сохранить как", command=save_file_as)

root.mainloop()

