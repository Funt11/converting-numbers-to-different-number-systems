import tkinter as tk

# Добавление символа в конец ввода


def click_button(box, text1):
    #box.icursor(tk.END)
    box.insert(tk.END, text1)
    # Следуем за вводом символов
    box.xview_moveto(1)

# Удаление последнего символа


def delete_one(box):
    # Получаем текущие символы
    current = box.get()
    # Если есть символы, то
    if current:
        box.delete(len(current) - 1)

# Удаление всего ввода


def delete_all(box):
    current = box.get()
    # Если есть символы, то
    if current:
        box.delete(0, len(current))


# Разделяем число на целую и дробную часть для проверки на число
def validate(box, answer, input_, output_):
    checker = "string"
    input_checker = False
    current = box.get().strip()
    current = current.replace(",", ".")
    input_get = input_.get()


    if current == "":
        answer.config(text="Ввод пустой.")
        return 
    
    if "10" in input_get:
        input_checker = True
    

    if current.count(".") == 1:
        int_ = current[:current.index(".")]
        float_ = current[current.index(".")+1:]
        
        if not(input_checker) and any(number_ in current for number_ in "56789"):
            checker = "False"
                
        elif len(int_) > 1 and not (int_.startswith("0")) and not (int_.startswith("+0")) and not (int_.startswith("-0")) and float_:

            try:
                float(current)
                checker = "float"
            except:
                checker = "string"

        elif len(int_.lstrip("+-")) == 1 and float_:

            try:
                float(current)
                checker = "float"
            except:
                checker = "string"

        

    elif current.count(".") == 0:

        if not(input_checker) and any(number_ in current for number_ in "56789"):
            checker = "False"

        elif len(current) >= 1 and not (current.startswith("0")) and not (current.startswith("+0")) and not (current.startswith("-0")):
            try:
                int(current)
                checker = "int"
            except:
                checker = "string"

        elif current == "0":
            checker = "int"

    if checker == "int" or checker == "float":
        #answer.config(text="good.")
        #print("1")
        distribution(current, answer, input_, output_, checker)

    elif checker == "False":
        answer.config(text="В вводе есть символы, отсутствующие в данной системе счисления.")
    else:
        answer.config(text="Неправильный ввод!")


# Распределение в перевод
def distribution(number_, answer_, input_, output_, checker):
    input_get = input_.get()
    output_get = output_.get()

    if checker == "int" and "10" in input_get and "5" in output_get:
        answer_.config(text=int10_to_5(number_))

    elif checker == "float" and "10" in input_get and "5" in output_get:
        answer_.config(text=float10_to_5(number_))

    elif checker == "int" and "5" in input_get and "10" in output_get:
        answer_.config(text=int5_to_10(number_))
    
    elif checker == "float" and "5" in input_get and "10" in output_get:
        answer_.config(text=float5_to_10(number_))

    elif "5" in input_get and "5" in output_get:
        answer_.config(text="Вы переводите из системы счисления 5-ой в 5-ую.")

    elif "10" in input_get and "10" in output_get:
        answer_.config(text="Вы переводите из системы счисления 10-ой в 10-ую.")

# Перевод целого из 10 в 5
def int10_to_5(number: str):

    if number == "0":
        return "0"
    
    saved = ""
    new_number = ""
    if number.startswith("+") or number.startswith("-"):
        if number.startswith("-"):
            saved = "-"

        number = number.lstrip("+-")


    number = int(number)

    while number > 0:
        number_ = number % 5
        new_number = str(number_) + new_number
        number = number // 5


    return saved + str(new_number)



# Перевод float из 10 в 5
def float10_to_5(number: str):
    number = number.replace(",", ".")
    int_ = number[:number.index(".")]
    float_ = number[number.index(".")+1:]
    saved = ""

    if number == "0.0":
        return "0.0"
    
    if int_.startswith("+") or int_.startswith("-"):
        if int_.startswith("-"):
            saved = "-"
        
        int_ = int_.lstrip("+-")

    # Перевод целого
    new_int_ = ""
    int_ = int(int_)

    while int_ > 0:
        number_1 = int_ % 5
        new_int_ = str(number_1) + new_int_
        int_ = int_ // 5

    new_float_ = ""
    float_ = "0." + float_
    float_ = float(float_)
    float_ = float_ * 5
    c = 0

    while float_ > 0:
        c += 1
        new_float_ += str(int(float_))
        float_ -= int(float_)
        float_ = float_ * 5

        if c > 25:
            break

    final_number = None
    final_number = new_int_ + "." + new_float_

    return saved + final_number


# Перевод из целого 5 в 10
def int5_to_10(number: str):

    new_number = 0
    index = 0
    saved = ""

    if number == "0":
        return "0"

    if number.startswith("+") or number.startswith("-"):
        if number.startswith("-"):
            saved = "-"
        
        number = number[1:]

    for i in range(len(number)-1, -1, -1):
        new_number += int(number[index])*5**i
        index += 1

    return saved + str(new_number)


# Перевод из float 5 в 10
def float5_to_10(number: str):
    number = number.replace(",", ".")
    int_ = 0
    float_ = 0
    final_number = 0
    saved = ""

    if number == "0.0":
        return "0.0"

    if number.startswith("+") or number.startswith("-"):
        if number.startswith("-"):
            saved = "-"
        
        number = number[1:]

    c = len(number[:number.index(".")])-1
    # Перевод в 10 целой части
    for i in range(0, number.index(".")):
        int_ += (int(number[i])*5**c)
        c -= 1

    # Перевод в 10 дробной части

    c1 = -1
    for i in range(number.index(".")+1, len(number)):
        float_ += (int(number[i])*5**c1)
        c1 -= 1

    final_number = int_ + float_

    return saved + str(final_number)

def open_instruction():
    f = open("1.txt")
   
