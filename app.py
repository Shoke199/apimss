from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def jpegzam():
    new_window = Toplevel(root)
    new_window.title("Изображение")
    img = Image.open('zam.png')
    photo = ImageTk.PhotoImage(img)
    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def jpeglam():
    new_window = Toplevel(root)
    new_window.title("Изображение")
    img = Image.open('lam.png')
    photo = ImageTk.PhotoImage(img)
    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def jpegot():
    new_window = Toplevel(root)
    new_window.title("Изображение")
    img = Image.open('ot.png')
    photo = ImageTk.PhotoImage(img)
    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def jpegpol():
    new_window = Toplevel(root)
    new_window.title("Изображение")
    img = Image.open('pol.png')
    photo = ImageTk.PhotoImage(img)
    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def incam():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('xarcam.jpg')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def inmk():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('xarmk.jpg')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def indat():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('xardat.jpg')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def inter():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('xarter.jpg')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def ystzam():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('ystzam.png')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def ystlam():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('ystlam.png')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def ystot():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('ystot.png')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def ystpol():
    new_window = Toplevel(root)
    new_window.title("Изображение")

    img = Image.open('ystpol.png')
    photo = ImageTk.PhotoImage(img)

    label = Label(new_window, image=photo)
    label.image = photo
    label.pack()

def funzam():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Открытие замка: открытие двери с использованием ключа, карты, отпечатка пальца или смартфона."
                                   "\nЗакрытие замка: автоматическое закрытие двери после заданного интервала времени или вручную."
                                   "\nУдаленное управление: контроль состояния замка через мобильное приложение или веб-интерфейс."
                                   "\nИстория событий: запись всех операций открытия и закрытия замка с указанием времени и способа аутентификации."
                                   "\nНастройка прав доступа: создание временных или постоянных ключей для гостей или сотрудников."
                                   "\nОповещения и уведомления: отправка уведомлений владельцу при попытке несанкционированного доступа или открытии двери.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Электронный замок")

def funlam():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Регулировка яркости: изменение уровня освещения в зависимости от предпочтений пользователя."
                                   "\nИзменение цвета света: настройка цветовой температуры или оттенка света для создания атмосферы."
                                   "\nАвтоматизация включения/выключения: включение лампы по расписанию или при обнаружении движения."
                                   "\nУправление голосом: интеграция с голосовыми помощниками для управления светом."
                                   "\nЭнергосбережение: автоматическое отключение при отсутствии активности в помещении."
                                   "\nИнтеграция с другими устройствами: синхронизация с датчиками освещенности, присутствия и другими элементами умного дома.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Умная лампочка")

def funot():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Поддержание заданной температуры: автоматическое регулирование нагрева помещения до установленного значения."
                                   "\nРежимы работы: выбор режима обогрева (экономичный, комфортный, ночной)."
                                   "\nГрафик работы: установка расписания включения и выключения отопления."
                                   "\nДистанционное управление: удаленная настройка температурных режимов через смартфон или компьютер."
                                   "\nЭкономия энергии: оптимизация энергопотребления путем учета погодных условий и текущего состояния системы."
                                   "\nМониторинг потребления энергии: отслеживание расходов тепла и электроэнергии для оценки эффективности системы.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Система отопления")

def funpol():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Контроль влажности почвы: измерение уровня влаги в почве и полив при достижении минимального порога."
                                   "\nРасписание полива: настройка графика полива в зависимости от типа растения и сезона."
                                   "\nИндивидуальная настройка для каждого растения: учет особенностей ухода за разными видами растений."
                                   "\nАварийный сигнал при засухе или избытке воды: уведомление владельца о проблемах с увлажнением."
                                   "\nИспользование датчиков дождя: предотвращение избыточного полива при дождливой погоде."
                                   "\nОптимальное использование водных ресурсов: экономия воды благодаря точной настройке объема и частоты полива.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Авто полив растений")

def inzam():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Установка:"
                                   "\n1-Осмотрите комплект поставки и подготовьте инструменты."
                                   "\n2-Открутите старый механический замок, предварительно сняв ручку."
                                   "\n3-Прикрепите новую накладку и заднюю пластину к внутренней стороне двери."
                                   "\n4-Протяните провода внутрь стены (при наличии питания от сети)."
                                   "\n5-Закрепите замок болтами, вставьте личинку или считывающее устройство."
                                   "\n6-Проверьте работу механизма закрывания."
                                   "\nОбслуживание:"
                                   "\n1-Периодически смазывайте движущиеся части замка силиконовым спреем."
                                   "\n2-Меняйте батарейки каждые полгода-год."
                                   "\n3-Очищайте сканеры отпечатков пальцев мягкой тканью.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Электронный замок")

def inlam():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Установка:"
                                   "\n1-Отключите электричество в комнате перед заменой старой лампочки."
                                   "\n2-Аккуратно выкрутите старую лампочку и вкрутите новую."
                                   "\n3-Подключите лампочку к домашней Wi-Fi сети через приложение."
                                   "\nОбслуживание:"
                                   "\n1-Регулярно протирайте плафон влажной тряпочкой."
                                   "\n2-Обновляйте программное обеспечение лампочки по мере выхода новых версий.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Умная лампочка")

def inot():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Установка:"
                                   "\n1-Проконсультируйтесь с инженером-теплотехником для выбора оптимального варианта размещения котлового оборудования."
                                   "\n2-Выполните монтаж котла, расширительного бака, циркуляционного насоса и запорной арматуры."
                                   "\n3-Подготовьте систему трубопроводов и отопительных приборов."
                                   "\n4-Залейте теплоноситель (воду или антифриз) и запустите отопление."
                                   "\nОбслуживание:"
                                   "\n1-Раз в сезон проводите профилактику котельного оборудования."
                                   "\n2-Промывайте теплообменники и радиаторы от отложений известняка и грязи."
                                   "\n3-Поддерживайте рабочее давление в пределах рекомендованных значений.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Система отопления")

def inpol():
    new_window = Toplevel(root)
    new_window.title("Характеристика")

    label = Label(new_window, text="Установка:"
                                   "\n1-Определите схему прокладки капельниц и форсунок в саду или теплице."
                                   "\n2-Организуйте подачу воды от внешнего источника к распределительным линиям."
                                   "\n3-Присоедините трубы и фиттинги, обеспечив герметичное соединение."
                                   "\n4-Монтируйте таймер подачи воды и датчик влажности почвы."
                                   "\nОбслуживание:"
                                   "\n1-Чистка фильтров каждые два месяца."
                                   "\n2-Замена изношенных элементов (форсунки, трубки, соединения)."
                                   "\n3-Ежегодная проверка работоспособности всей системы перед посадочным сезоном.")
    label.pack(padx=20, pady=20)

    add_navigation_buttons(new_window, "Авто полив растений")


def file_open():
    messagebox.showinfo("Открытие файла")

def file_save():
    messagebox.showinfo("Сохранение файла")

def file_close():
    root.destroy()

def add_navigation_buttons(window, device_name):
    frame = Frame(window)
    frame.pack(pady=10)

    if device_name == "Электронный замок":
        image_func = jpegzam
        specs_func = ystzam
        functions_func = funzam
    elif device_name == "Умная лампочка":
        image_func = jpeglam
        specs_func = ystlam
        functions_func = funlam
    elif device_name == "Система отопления":
        image_func = jpegot
        specs_func = ystot
        functions_func = funot
    elif device_name == "Авто полив растений":
        image_func = jpegpol
        specs_func = ystpol
        functions_func = funpol

    btn_image = Button(frame, text="Изображение", command=image_func)
    btn_image.pack(side=LEFT, padx=5)

    btn_specs = Button(frame, text="Характеристика", command=specs_func)
    btn_specs.pack(side=LEFT, padx=5)

    btn_functions = Button(frame, text="Функции", command=functions_func)
    btn_functions.pack(side=LEFT, padx=5)


def create_device_buttons():
    device_frame = Frame(root, bg="lightgray")
    device_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

    Label(device_frame, text="Устройства", bg="lightgray").pack(pady=10)

    def select_device(btn, device_name):

        for child in device_frame.winfo_children():
            if isinstance(child, Button):
                child.config(relief=RAISED, bg="SystemButtonFace")


        if device_name == "Электронный замок":
            jpegzam()
        elif device_name == "Умная лампочка":
            jpeglam()
        elif device_name == "Система отопления":
            jpegot()
        elif device_name == "Авто полив растений":
            jpegpol()

    devices = [
        ("Электронный замок", "Управление доступом и безопасностью"),
        ("Умная лампочка", "Интеллектуальное освещение"),
        ("Система отопления", "Климат-контроль помещений"),
        ("Авто полив растений", "Автоматический полив растений")
    ]

    for device_name, description in devices:
        btn = Button(device_frame, text=device_name, width=20,
                     command=lambda name=device_name, b=None: select_device(btn, name))
        btn.pack(pady=5, padx=10)

        def create_tooltip(widget, text):
            def show_tooltip(event):
                tooltip = Toplevel(root)
                tooltip.wm_overrideredirect(True)
                tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
                label = Label(tooltip, text=text, relief="solid", borderwidth=1)
                label.pack()
                widget.tooltip_window = tooltip

            def hide_tooltip(event):
                if hasattr(widget, 'tooltip_window'):
                    widget.tooltip_window.destroy()
                    delattr(widget, 'tooltip_window')

            widget.bind("<Enter>", show_tooltip)
            widget.bind("<Leave>", hide_tooltip)

        create_tooltip(btn, description)

def create_device_buttons():
    device_frame = Frame(root, bg="lightgray")
    device_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

    Label(device_frame, text="Устройства", bg="lightgray").pack(pady=10)

    def select_device(btn, device_name):
        for child in device_frame.winfo_children():
            if isinstance(child, Button):
                child.config(relief=RAISED, bg="SystemButtonFace")

        btn.config(relief=SUNKEN, bg="lightblue")

        if device_name == "Электронный замок":
            inzam()
        elif device_name == "Умная лампочка":
            inlam()
        elif device_name == "Система отопления":
            inot()
        elif device_name == "Авто полив растений":
            inpol()

    try:
        lock_img = Image.open('zam.png')
        lock_img = lock_img.resize((50, 50), Image.Resampling.LANCZOS)
        lock_icon = ImageTk.PhotoImage(lock_img)

        bulb_img = Image.open('lam.png')
        bulb_img = bulb_img.resize((50, 50), Image.Resampling.LANCZOS)
        bulb_icon = ImageTk.PhotoImage(bulb_img)

        heat_img = Image.open('ot.png')
        heat_img = heat_img.resize((50, 50), Image.Resampling.LANCZOS)
        heat_icon = ImageTk.PhotoImage(heat_img)

        water_img = Image.open('pol.png')
        water_img = water_img.resize((50, 50), Image.Resampling.LANCZOS)
        water_icon = ImageTk.PhotoImage(water_img)
    except:
        lock_icon = bulb_icon = heat_icon = water_icon = None

    devices = [
        ("Электронный замок", "Управление доступом и безопасностью", lock_icon),
        ("Умная лампочка", "Интеллектуальное освещение", bulb_icon),
        ("Система отопления", "Климат-контроль помещений", heat_icon),
        ("Авто полив растений", "Автоматический полив растений", water_icon)
    ]

    for device_name, description, icon in devices:
        if icon:
            btn = Button(device_frame, image=icon,
                         command=lambda name=device_name, b=None: select_device(btn, name),
                         bg="lightgray", relief=RAISED)
            btn.image = icon
        else:
            btn = Button(device_frame, text=device_name, width=20,
                         command=lambda name=device_name, b=None: select_device(btn, name))

        btn.pack(pady=5, padx=10)

        def create_tooltip(widget, text):
            def show_tooltip(event):
                tooltip = Toplevel(root)
                tooltip.wm_overrideredirect(True)
                tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
                label = Label(tooltip, text=text, relief="solid", borderwidth=1)
                label.pack()
                widget.tooltip_window = tooltip

            def hide_tooltip(event):
                if hasattr(widget, 'tooltip_window'):
                    widget.tooltip_window.destroy()
                    delattr(widget, 'tooltip_window')

            widget.bind("<Enter>", show_tooltip)
            widget.bind("<Leave>", hide_tooltip)

        create_tooltip(btn, description)

root = Tk()
root.title("Умный дом")
root.geometry("1000x600")

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(root)
filemenu = Menu(filemenu, tearoff=0)
filemenu.add_command(label="Открыть", command=file_open)
filemenu.add_command(label="Сохранить", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Закрыть", command=file_close)

inmenu = Menu(mainmenu, tearoff=0)
inmenu.add_command(label="Электронный замок", command=inzam)
inmenu.add_command(label="Умная лампочка", command=inlam)
inmenu.add_command(label="Система отопления", command=inot)
inmenu.add_command(label="Авто полив растений", command=inpol)

ystmenu = Menu(mainmenu, tearoff=0)

ystmenu2 = Menu(ystmenu, tearoff=0)
ystmenu2.add_command(label="Изображение", command=jpegzam)
ystmenu2.add_command(label="Характеристика", command=ystzam)
ystmenu2.add_command(label="Функции", command=funzam)

ystmenu.add_cascade(label="Электронный замок",menu=ystmenu2)

ystmenu3 = Menu(ystmenu, tearoff=0)
ystmenu3.add_command(label="Изображение", command=jpeglam)
ystmenu3.add_command(label="Характеристика", command=ystlam)
ystmenu3.add_command(label="Функции", command=funlam)

ystmenu.add_cascade(label="Умная лампочка",menu=ystmenu3)

ystmenu4 = Menu(ystmenu, tearoff=0)
ystmenu4.add_command(label="Изображение", command=jpegot)
ystmenu4.add_command(label="Характеристика", command=ystot)
ystmenu4.add_command(label="Функции", command=funot)

ystmenu.add_cascade(label="Система отопления",menu=ystmenu4)

ystmenu5 = Menu(ystmenu, tearoff=0)
ystmenu5.add_command(label="Изображение", command=jpegpol)
ystmenu5.add_command(label="Характеристика", command=ystpol)
ystmenu5.add_command(label="Функции", command=funpol)

ystmenu.add_cascade(label="Авто полив растений",menu=ystmenu5)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Устройства", menu=ystmenu)
mainmenu.add_cascade(label="Инструкция", menu=inmenu)
mainmenu.add_cascade(label="Помощь")

create_device_buttons()

left_frame = Frame(root)
left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)



root.mainloop()