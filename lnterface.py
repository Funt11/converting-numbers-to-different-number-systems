
# Created by Funt11

import program
import tkinter as tk


def interface():

    main_ = tk.Tk()

    main_.resizable(False, False)
    main_.title("Перевод вещественных чисел из 10-ой в 5-ую и обратно.")
    main_.iconbitmap("1234.ico")
    main_.geometry("750x630")  # размер приложения

    # Ввод числа
    text_box1 = tk.Entry(font=("Arial", 18), width=20, relief="solid")
    label = tk.Label(main_, text="Исходное число",
                     font=("Arial", 15))

    text_box1.place(x=200, y=50)
    label.place(x=30, y=55)

    # Выпадающий список
    choices_input = ["10 (десятичной)", "5 (пятеричной)"]  # список ввода
    choices_output = ["10 (десятичную)", "5 (пятеричную)"]  # список вывода

    selected_option_input = tk.StringVar()  # выбранное значение ввода
    selected_option_input.set(choices_input[0])  # начальное значение ввода

    selected_option_output = tk.StringVar()
    selected_option_output.set(choices_output[1])

    menu_input = tk.OptionMenu(main_, selected_option_input, *choices_input)
    menu_input.config(font=("Arial", 12))  # корректируем шрифт
    label_menu_input = tk.Label(
        main_, text="Перевод из", font=("Arial", 15))

    menu_output = tk.OptionMenu(main_, selected_option_output, *choices_output)
    menu_output.config(font=("Arial", 12))
    label_menu_output = tk.Label(
        main_, text="Перевод в", font=("Arial", 15))

    menu_input.place(x=150, y=125)
    label_menu_input.place(x=30, y=125)

    menu_output.place(x=430, y=125)
    label_menu_output.place(x=320, y=125)

    # Изменяемый ответ после конвертера
    answer_main = tk.Label(text="", font=("Arial", 15))
    answer_main.place(x=110, y=235)

    answer_ = tk.Label(text="Ответ:", font=("Arial", 18))
    answer_.place(x=30, y=235)

    # Кнопка Конвертировать
    button = tk.Button(text="Конвертировать", font=("Arial", 15),
                       command=lambda: program.validate(text_box1, answer_main, selected_option_input, selected_option_output))
    button.place(x=230, y=180)

    # Кнопки для ввода в калькулятор
    button0 = tk.Button(text="0", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "0"))
    button1 = tk.Button(main_, text="1", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "1"))
    button2 = tk.Button(text="2", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "2"))
    button3 = tk.Button(text="3", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "3"))
    button4 = tk.Button(text="4", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "4"))
    button5 = tk.Button(text="5", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "5"))
    button6 = tk.Button(text="6", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "6"))
    button7 = tk.Button(text="7", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "7"))
    button8 = tk.Button(text="8", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "8"))
    button9 = tk.Button(text="9", font=("Arial", 18),
                        command=lambda: program.click_button(text_box1, "9"))
    button_plus = tk.Button(text="+", font=("Arial", 18),
                            command=lambda: program.click_button(text_box1, "+"))
    button_minus = tk.Button(text="-", font=("Arial", 18),
                             command=lambda: program.click_button(text_box1, "-"))
    button_delete_one = tk.Button(text="<--", font=("Arial", 18),
                                  command=lambda: program.delete_one(text_box1))
    button_delete_all = tk.Button(text="C", font=(
        "Arial", 18), command=lambda: program.delete_all(text_box1))
    button_comma = tk.Button(text=",", font=("Arial", 18),
                             command=lambda: program.click_button(text_box1, ","))

    button7.place(x=30, y=290, width=80)
    button8.place(x=115, y=290, width=80)
    button9.place(x=200, y=290, width=80)
    button4.place(x=30, y=342, width=80)
    button5.place(x=115, y=342, width=80)
    button6.place(x=200, y=342, width=80)
    button1.place(x=30, y=394, width=80)
    button2.place(x=115, y=394, width=80)
    button3.place(x=200, y=394, width=80)
    button0.place(x=30, y=446, width=80)
    button_plus.place(x=115, y=446, width=80)
    button_minus.place(x=200, y=446, width=80)
    button_delete_one.place(x=285, y=290, width=80)
    button_delete_all.place(x=285, y=342, width=80)
    button_comma.place(x=285, y=394, width=80)

    label_name = tk.Label(
        main_, text="Created by Funt11", font=("Arial", 12))

    label_name.place(x=470, y=570)

    # Бинд клавиши Enter, event хранит информацию о нажатии клавиши Enter, функция invoke нажимает кнопку.
    main_.bind("<Return>", lambda event: button.invoke())

    # Меню сверху
    menu_bar = tk.Menu(main_)

    # Действия
    file_menu1 = tk.Menu(menu_bar, tearoff=0)

    file_menu1.add_command(
        label="Удалить 1 символ.", command=lambda: program.delete_one(text_box1), font=("Arial", 15))
    file_menu1.add_command(label="Очистить весь ввод.", font=(
        "Arial", 15), command=lambda: program.delete_all(text_box1))
    file_menu1.add_command(label="Конвертировать", font=("Arial", 15), command=lambda: program.validate(
        text_box1, answer_main, selected_option_input, selected_option_output))
    file_menu1.add_separator()  # Разделяем штрихами кнопку Выход
    file_menu1.add_command(label="Выход", font=(
        "Arial", 15), command=main_.quit)
    # Добавляем в меню кнопку Действия
    menu_bar.add_cascade(label="Действия", menu=file_menu1)

    # Информация
    file_menu2 = tk.Menu(menu_bar, tearoff=0)

    menu_bar.add_cascade(label="Информация о программе", menu=file_menu2)
    file_menu2.add_command(label="Программа переводит из 5-ой системы счисления в 10 и обратно.",
                           font=("Mono", 11))

    # Появление меню
    main_.config(menu=menu_bar)

    main_.mainloop()  # запуск окна программы


interface()
