import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

TARGET_SIZE = (224, 224)
TARGET_FORMAT = 'JPEG'

def process_images(source_folder, target_folder):
    for category in os.listdir(source_folder):
        category_path = os.path.join(source_folder, category)
        if os.path.isdir(category_path):
            target_category_path = os.path.join(target_folder, category)

            if not os.path.exists(target_category_path):
                os.makedirs(target_category_path)

            counter = 1
            for img_name in os.listdir(category_path):
                source_img_path = os.path.join(category_path, img_name)
                if os.path.isfile(source_img_path):
                    target_img_path = os.path.join(target_category_path, f"{category}_{counter:02}.jpg")

                    with Image.open(source_img_path) as img:
                        img = img.convert('RGB')
                        img = img.resize(TARGET_SIZE, Image.LANCZOS)
                        img.save(target_img_path, TARGET_FORMAT)

                    counter += 1

def select_folders():
    source_folder = filedialog.askdirectory(title="Выберите папку с исходными изображениями")
    if not source_folder:
        messagebox.showwarning("Предупреждение", "Папка не выбрана!")
        return

    target_folder = filedialog.askdirectory(title="Выберите папку для сохранения обработанных изображений")
    if not target_folder:
        messagebox.showwarning("Предупреждение", "Целевая папка не выбрана!")
        return

    process_images(source_folder, target_folder)
    messagebox.showinfo("Готово!", "Изображения обработаны успешно!")

# GUI
root = tk.Tk()
root.title("Обработка изображений")
root.geometry("400x150")

btn_select_folders = tk.Button(
    root,
    text="Выбрать папки и обработать изображения",
    command=select_folders,
    font=("Arial", 12),
    width=35,
    height=2,
)
btn_select_folders.pack(expand=True)

def select_folders():
    source_folder = filedialog.askdirectory(title="Выберите папку с исходными изображениями")
    if not source_folder:
        messagebox.showwarning("Предупреждение", "Исходная папка не выбрана!")
        return

    target_folder = filedialog.askdirectory(title="Выберите папку для сохранения обработанных изображений")
    if not target_folder:
        messagebox.showwarning("Предупреждение", "Целевая папка не выбрана!")
        return

    process_images(source_folder, target_folder)
    messagebox.showinfo("Готово", "Изображения успешно обработаны и сохранены!")

btn_select_folders.pack(expand=True)

root.mainloop()