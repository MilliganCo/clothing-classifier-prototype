import os
import tkinter as tk
from tkinter import filedialog, messagebox


def rename_files_in_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for index, file_name in enumerate(sorted(files), start=1):
        extension = os.path.splitext(file_name)[1]
        new_name = f"{folder_name}_{str(index).zfill(2)}{extension}"

        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        rename_files_in_folder(folder_selected)
        messagebox.showinfo("Готово", f"Файлы в папке '{os.path.basename(folder_selected)}' переименованы.")


# GUI
root = tk.Tk()
root.title("Переименование файлов в папке")
root.geometry("400x150")

btn_select_folder = tk.Button(
    root,
    text="Выбрать папку и переименовать файлы",
    command=select_folder,
    font=("Arial", 12),
    width=35,
    height=2,
)
btn_select_folder.pack(expand=True)

root.mainloop()
