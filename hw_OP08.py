import tkinter as tk
from PIL import ImageTk, Image


def add_task():
    task = task_entry.get()
    if task:
        task_list_box_general.insert(tk.END, task)
        task_entry.delete(0, tk.END)


# Перенос задачи из списка задач в список текущих задач
def current_task():
    selected_index = task_list_box_general.curselection()
    if selected_index:
        selected_task = task_list_box_general.get(selected_index)
        task_list_box_current.insert(tk.END, selected_task)
        task_list_box_general.delete(selected_index)


# Перенос задачи из списка задач в список отмененных задач
def canceled_task():
    selected_index = task_list_box_general.curselection()
    if selected_index:
        selected_task = task_list_box_general.get(selected_index)
        task_list_box_canceled.insert(tk.END, selected_task)
        task_list_box_general.delete(selected_index)


# Перенос задачи из списка текущих задач в список выполненных задач
def completed_task():
    selected_index = task_list_box_current.curselection()
    if selected_index:
        selected_task = task_list_box_current.get(selected_index)
        task_list_box_completed.insert(tk.END, selected_task)
        task_list_box_current.delete(selected_index)


# Перенос задачи из списка текущих задач в список задач
def postpone_task():
    selected_index = task_list_box_current.curselection()
    if selected_index:
        selected_task = task_list_box_current.get(selected_index)
        task_list_box_general.insert(tk.END, selected_task)
        task_list_box_current.delete(selected_index)


# Перенос задачи из списка отмененных задач в список задач
def returned_task():
    selected_index = task_list_box_canceled.curselection()
    if selected_index:
        selected_task = task_list_box_canceled.get(selected_index)
        task_list_box_general.insert(tk.END, selected_task)
        task_list_box_canceled.delete(selected_index)


# Удаление задачи из списка отмененных задач
def deleted_task():
    selected_index = task_list_box_canceled.curselection()
    if selected_index:
        task_list_box_canceled.delete(selected_index)


# Подарок за выполнение задачи
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Полка")

    # Загружаем изображение
    image = Image.open("pie.jpg")

    # Создаем объект ImageTk для отображения изображения в Tkinter
    img = ImageTk.PhotoImage(image)

    # Создаем виджет Label для отображения изображения
    label = tk.Label(new_window, image=img)
    label.image = img  # сохраняем ссылку на изображение, чтобы избежать сбора мусора
    label.pack()


root = tk.Tk()
root.title("Планировщик задач")
root.config(background="PaleGreen2")

# Заполняем список задач

label_task_entry = tk.Label(root, text="Введите задачу:", bg="PaleGreen2")
label_task_entry.pack()

task_entry = tk.Entry(root, width=50, bg="cornflower blue", fg="black")
task_entry.pack(padx=5)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5, padx=5)

frame = tk.Frame(root, width=100, bg="chartreuse1")
frame.pack()

# Фрейм для списка задач и их обработка

label_task_general = tk.Label(frame, text="Список задач", bg="chartreuse1")
label_task_general.grid(column=0, row=0)

task_list_box_general = tk.Listbox(frame, width=30, bg="cornflower blue", fg="black")
task_list_box_general.grid(column=0, row=1, sticky="nsew", padx=5, pady=(0, 5))

current_task_button = tk.Button(frame, text="Взять в работу", command=current_task)
current_task_button.grid(column=0, row=3, pady=5, padx=5)

canceled_task_button = tk.Button(frame, text="Отменить задачу", command=canceled_task)
canceled_task_button.grid(column=0, row=4, pady=5, padx=5)

# Фрейм для списка текущих задач и их обработка

label_task_current = tk.Label(frame, text="Текущие задачи", bg="chartreuse1")
label_task_current.grid(column=1, row=0)

task_list_box_current = tk.Listbox(frame, width=30, bg="yellow2", fg="black")
task_list_box_current.grid(column=1, row=1, padx=(0, 5), pady=(0, 5), sticky="nsew")

completed_task_button = tk.Button(frame, text="Задача выполнена", command=completed_task)
completed_task_button.grid(column=1, row=3, pady=5, padx=5)

postpone_task_button = tk.Button(frame, text="Отложить задачу", command=postpone_task)
postpone_task_button.grid(column=1, row=4, pady=5, padx=5)

# Фрейм для списка завершенных задач

label_task_completed = tk.Label(frame, text="Завершенные задачи", bg="chartreuse1")
label_task_completed.grid(column=2, row=0)

task_list_box_completed = tk.Listbox(frame, width=30, bg="SpringGreen3", fg="black")
task_list_box_completed.grid(column=2, row=1, padx=(0, 5), pady=(0, 5), sticky="nsew")

pie_task_button = tk.Button(frame, text="Молодец!\nВозьми с полки\nпирожок", width=20, height=4,
                            command=open_new_window)
pie_task_button.grid(column=2, row=3, rowspan=2, pady=5, padx=5)

# Фрейм для списка отмененных задач

label_task_canceled = tk.Label(frame, text="Отмененные задачи", bg="chartreuse1")
label_task_canceled.grid(column=3, row=0)

task_list_box_canceled = tk.Listbox(frame, width=30, bg="tomato3", fg="black")
task_list_box_canceled.grid(column=3, row=1, padx=(0, 5), pady=(0, 5), sticky="nsew")

returned_task_button = tk.Button(frame, text="Вернуть в список", command=returned_task)
returned_task_button.grid(column=3, row=3, pady=5, padx=5)

deleted_task_button = tk.Button(frame, text="Удалить задачу", command=deleted_task)
deleted_task_button.grid(column=3, row=4, pady=5, padx=5)

root.mainloop()
