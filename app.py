from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

icons = {}
tooltip_windows = {}

def create_image_window(image_name, title):
    try:
        new_window = Toplevel(root)
        new_window.title(title)
        img = Image.open(image_name)
        photo = ImageTk.PhotoImage(img)
        label = Label(new_window, image=photo)
        label.image = photo
        label.pack()
    except:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {image_name}")

def create_text_window(text, title, device_name=None):
    new_window = Toplevel(root)
    new_window.title(title)

    scrollbar = Scrollbar(new_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_widget = Text(new_window, wrap=WORD, yscrollcommand=scrollbar.set, padx=20, pady=20)
    text_widget.insert(END, text)
    text_widget.config(state=DISABLED)
    text_widget.pack(fill=BOTH, expand=True)

    scrollbar.config(command=text_widget.yview)

    if device_name:
        add_navigation_buttons(new_window, device_name)

def add_navigation_buttons(window, device_name):
    frame = Frame(window)
    frame.pack(pady=10)

    device_map = {
        "Электронный замок": {
            "image": ("zam.png", "Изображение замка"),
            "specs": ("""Установка:
1. Осмотрите комплект поставки и подготовьте инструменты.
2. Открутите старый механический замок.
3. Прикрепите новую накладку.
4. Протяните провода.
5. Закрепите замок болтами.
6. Проверьте работу механизма.

Обслуживание:
1. Периодически смазывайте движущиеся части.
2. Меняйте батарейки каждые полгода.
3. Очищайте сканеры отпечатков пальцев.""", "Характеристика замка"),
            "functions": ("""Открытие замка: открытие двери с использованием ключа, карты, отпечатка пальца или смартфона.
Закрытие замка: автоматическое закрытие двери.
Удаленное управление: контроль через мобильное приложение.
История событий: запись всех операций.
Настройка прав доступа: создание временных ключей.
Оповещения: уведомления при попытке доступа.""", "Функции замка")
        },
        "Умная лампочка": {
            "image": ("lam.png", "Изображение лампочки"),
            "specs": ("""Установка:
1. Отключите электричество.
2. Выкрутите старую лампочку и вкрутите новую.
3. Подключите к Wi-Fi через приложение.

Обслуживание:
1. Протирайте плафон.
2. Обновляйте программное обеспечение.""", "Характеристика лампочки"),
            "functions": ("""Регулировка яркости: изменение уровня освещения.
Изменение цвета света: настройка цветовой температуры.
Автоматизация: включение по расписанию.
Управление голосом: интеграция с помощниками.
Энергосбережение: автоматическое отключение.
Интеграция: синхронизация с датчиками.""", "Функции лампочки")
        },
        "Система отопления": {
            "image": ("ot.png", "Изображение системы отопления"),
            "specs": ("""Установка:
1. Проконсультируйтесь с инженером.
2. Выполните монтаж оборудования.
3. Подготовьте систему трубопроводов.
4. Залейте теплоноситель.

Обслуживание:
1. Проводите профилактику раз в сезон.
2. Промывайте теплообменники.
3. Поддерживайте рабочее давление.""", "Характеристика отопления"),
            "functions": ("""Поддержание температуры: регулирование нагрева.
Режимы работы: экономичный, комфортный, ночной.
График работы: расписание включения.
Дистанционное управление: через смартфон.
Экономия энергии: оптимизация потребления.
Мониторинг: отслеживание расходов.""", "Функции отопления")
        },
        "Авто полив растений": {
            "image": ("pol.png", "Изображение системы полива"),
            "specs": ("""Установка:
1. Определите схему прокладки капельниц.
2. Организуйте подачу воды.
3. Присоедините трубы и фиттинги.
4. Монтируйте таймер и датчики.

Обслуживание:
1. Чистка фильтров каждые два месяца.
2. Замена изношенных элементов.
3. Ежегодная проверка системы.""", "Характеристика полива"),
            "functions": ("""Контроль влажности: измерение уровня влаги.
Расписание полива: настройка графика.
Индивидуальная настройка: для разных растений.
Аварийный сигнал: уведомление о проблемах.
Использование датчиков: предотвращение избыточного полива.
Оптимальное использование: экономия воды.""", "Функции полива")
        }
    }

    if device_name in device_map:
        device = device_map[device_name]

        Button(frame, text="Изображение",
               command=lambda: create_image_window(device["image"][0], device["image"][1])).pack(side=LEFT, padx=5)

        Button(frame, text="Характеристика",
               command=lambda: create_text_window(device["specs"][0], device["specs"][1], device_name)).pack(side=LEFT, padx=5)

        Button(frame, text="Функции",
               command=lambda: create_text_window(device["functions"][0], device["functions"][1], device_name)).pack(side=LEFT, padx=5)

def select_device(device_name):
    device_data = {
        "Электронный замок": """Установка:
1. Осмотрите комплект поставки и подготовьте инструменты.
2. Открутите старый механический замок.
3. Прикрепите новую накладку.
4. Протяните провода.
5. Закрепите замок болтами.
6. Проверьте работу механизма.

Обслуживание:
1. Периодически смазывайте движущиеся части.
2. Меняйте батарейки каждые полгода.
3. Очищайте сканеры отпечатков пальцев.""",
        "Умная лампочка": """Установка:
1. Отключите электричество.
2. Выкрутите старую лампочку и вкрутите новую.
3. Подключите к Wi-Fi через приложение.

Обслуживание:
1. Протирайте плафон.
2. Обновляйте программное обеспечение.""",
        "Система отопления": """Установка:
1. Проконсультируйтесь с инженером.
2. Выполните монтаж оборудования.
3. Подготовьте систему трубопроводов.
4. Залейте теплоноситель.

Обслуживание:
1. Проводите профилактику раз в сезон.
2. Промывайте теплообменники.
3. Поддерживайте рабочее давление.""",
        "Авто полив растений": """Установка:
1. Определите схему прокладки капельниц.
2. Организуйте подачу воды.
3. Присоедините трубы и фиттинги.
4. Монтируйте таймер и датчики.

Обслуживание:
1. Чистка фильтров каждые два месяца.
2. Замена изношенных элементов.
3. Ежегодная проверка системы."""
    }

    if device_name in device_data:
        create_text_window(device_data[device_name], f"Инструкция - {device_name}", device_name)

def create_tooltip(widget, text):
    def show_tooltip(event):
        if widget.winfo_containing(event.x_root, event.y_root) == widget:
            tooltip = Toplevel(root)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = Label(tooltip, text=text, relief="solid", borderwidth=1,
                          bg="lightyellow", padx=5, pady=2)
            label.pack()
            tooltip_windows[widget] = tooltip

    def hide_tooltip(event):
        if widget in tooltip_windows:
            tooltip_windows[widget].destroy()
            del tooltip_windows[widget]

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

def create_device_buttons():
    device_frame = Frame(root, bg="lightgray")
    device_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

    Label(device_frame, text="Устройства", bg="lightgray",
          font=("Arial", 12, "bold")).pack(pady=10)

    devices = [
        ("Электронный замок", "Управление доступом и безопасностью", "zam.png"),
        ("Умная лампочка", "Интеллектуальное освещение", "lam.png"),
        ("Система отопления", "Климат-контроль помещений", "ot.png"),
        ("Авто полив растений", "Автоматический полив растений", "pol.png")
    ]

    for device_name, description, icon_file in devices:
        try:
            img = Image.open(icon_file)
            img = img.resize((50, 50), Image.Resampling.LANCZOS)
            icon = ImageTk.PhotoImage(img)
            icons[device_name] = icon

            btn = Button(device_frame, image=icon, bg="lightgray", relief=RAISED,
                         command=lambda name=device_name: select_device(name))
            btn.pack(pady=5, padx=10)
        except:
            btn = Button(device_frame, text=device_name, width=20,
                         command=lambda name=device_name: select_device(name))
            btn.pack(pady=5, padx=10)

        create_tooltip(btn, description)

def file_open():
    messagebox.showinfo("Открытие", "Функция открытия файла")

def file_save():
    messagebox.showinfo("Сохранение", "Функция сохранения файла")

def file_close():
    root.destroy()

def create_menus():
    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Открыть", command=file_open)
    file_menu.add_command(label="Сохранить", command=file_save)
    file_menu.add_separator()
    file_menu.add_command(label="Закрыть", command=file_close)
    menubar.add_cascade(label="Файл", menu=file_menu)

    device_menu = Menu(menubar, tearoff=0)

    devices = ["Электронный замок", "Умная лампочка",
               "Система отопления", "Авто полив растений"]

    for device in devices:
        dev_submenu = Menu(device_menu, tearoff=0)
        dev_submenu.add_command(label="Изображение",
                                command=lambda d=device: create_image_window(
                                    f"{d.split()[-1].lower()}.png" if d != "Электронный замок" else "zam.png",
                                    f"Изображение {d}"))
        dev_submenu.add_command(label="Характеристика",
                                command=lambda d=device: select_device(d))
        dev_submenu.add_command(label="Функции",
                                command=lambda d=device: select_device(d))
        device_menu.add_cascade(label=device, menu=dev_submenu)

    menubar.add_cascade(label="Устройства", menu=device_menu)

    instr_menu = Menu(menubar, tearoff=0)
    for device in devices:
        instr_menu.add_command(label=device,
                               command=lambda d=device: select_device(d))
    menubar.add_cascade(label="Инструкция", menu=instr_menu)

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="О программе",
                          command=lambda: messagebox.showinfo("О программе", "Умный дом v1.0"))
    menubar.add_cascade(label="Помощь", menu=help_menu)

root = Tk()
root.title("Умный дом")
root.geometry("1000x600")

create_menus()

create_device_buttons()

root.mainloop()