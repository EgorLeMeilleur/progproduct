from translate import Translator
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, scrolledtext
from tkinter import font as tkFont
import cmath
import math


translations = {
    "English": {
        "language": "Language: ",
        "error": "Error",
        "error_real": "Input correct real part",
        "error_imag": "Input correct imaginary part",
        "name": "Square root",
        "real_part": "Real part: ",
        "imag_part": "Imaginary: ",
        "precision": "Precision (quantity of digits after comma): ",
        "root": "Root equals: ",
        "calc": "Calculate",
        "support": "Technical support: 8-800-235-35-35",
        "doc": "Documentation",
        "text_doc": "Two input fields are given: the upper one for the real part of the number, the lower one for the imaginary part. There is a precision field where the number of decimal places is indicated. To work with complex numbers, you need to enter numbers in both fields. To work with real numbers, you only need to enter a value in the top field. To calculate the root of a number, you need to click on the calculate button and select the required accuracy."
    },
    "Русский": {
        "language": "Язык: ",
        "error": "Ошибка",
        "error_real": "Введите правильно действительную часть",
        "error_imag": "Введите правильно мнимую часть",
        "name": "Квадратный корень",
        "real_part": "Действительная часть: ",
        "imag_part": "Мнимая часть: ",
        "precision": "Точность (количество знаков после запятой): ",
        "root": "Корень равен: ",
        "calc": "Посчитать",
        "support": "Техническая поддержка: 8-800-235-35-35",
        "doc": "Документация",
        "text_doc": "Даны два поля ввода: верхнее для действительной части числа,  нижнее для мнимой части. Есть поле точности, где указывается количество знаков после запятой. Для работы с комплексными числами нужно ввести в оба поля числа. Для работы с действительными числами нужно ввести значение только в верхнее поле. Для расчета корня из числа, нужно нажать на кнопку посчитать и выбрать небходимую точность."
    }
}

def doc():
    lang = combo_lang.get()
    messagebox.showinfo(translations[lang]["doc"], translations[lang]["text_doc"])

def close_window():
    """Close the window."""
    root.destroy()

def set_language(event):
    lang = combo_lang.get()
    label_lang['text'] = translations[lang]["language"]
    label_real['text'] = translations[lang]["real_part"]
    label_complex['text'] = translations[lang]["imag_part"]
    label_precision['text'] = translations[lang]["precision"]
    label_result['text'] = translations[lang]["root"]
    label_tech_sup['text'] = translations[lang]["support"]
    doc_btn.configure(text=translations[lang]["doc"])
    calculation_btn.configure(text=translations[lang]["calc"])

def validate_float_entry(value: str) -> bool:
    """
    Validates if the input value is a valid float.

    Args:
    value (str): The input value to be validated.

    Returns:
    bool: True if the input value is a valid float, False otherwise.
    """
    try: 
        if value:
            if value[0] == '-' and len(value) == 1:
                return True
            float(value)
        return True
    except ValueError:
        return False
            

def root_func(real, imaginary=0):
    """
    Calculate the square root of a complex number.
    
    Args:
    real (float): The real part of the complex number.
    imaginary (float, optional): The imaginary part of the complex number. Defaults to 0.
    
    Returns:
    complex: The square root of the input complex number.
    """
    number = complex(real, imaginary)
    return cmath.sqrt(number)


def check_if_real(number):
    """
    Check if the given number is a real number.

    Args:
    - number: The number to be checked.

    Returns:
    - bool: True if the number is real, False otherwise.
    """
    return math.isclose(number.imag, 0)

def calculation():
    """Perform the calculation based on user input and display the result."""
    # Get the input values from the entry fields
    real_str = entry_real.get()
    complex_str = entry_complex.get()
    precision = int(combo_precision.get())

    # Convert the real part to a float, show error if invalid input
    try:
        real = float(real_str)
    except ValueError:
        messagebox.showerror(translations[combo_lang.get()]["error"], translations[combo_lang.get()]["error_real"])
        return

    # Convert the complex part to a float, show error if invalid input
    try:
        if complex_str == "":
            imag = 0
        else:                      
            imag = float(complex_str)
    except ValueError:
        messagebox.showerror(translations[combo_lang.get()]["error"], translations[combo_lang.get()]["error_imag"])
        return
    
    # Perform the root function calculation
    result = root_func(real, imag)
    if check_if_real(result):
        result = "{:.{}f}".format(result.real, precision)
    else:
        imag_ = abs(result.imag)
        formatted_imaginary = "{:.{}f}".format(imag_, precision)
        result = "±{:.{}f}±{}i".format(result.real, precision, formatted_imaginary)
    
    # Update the result entry field
    entry_result.config(state="normal")
    entry_result.delete(0, "end")
    entry_result.insert(0, result)
    entry_result.config(state="readonly")
                
    

root = Tk()
root.title("Square root")
root.geometry("400x400")
root.resizable(False, False)

combo_lang = ttk.Combobox(root, values=["Русский", "English"], justify="center", state='readonly')
combo_lang.set("Русский")
combo_lang.place(x=235, y=15, width=150, height = 25)
combo_lang.bind('<<ComboboxSelected>>', set_language)

label_lang= Label(root, text = "Язык :")
label_lang.place(x=160, y=15, width=75, height = 25)

label_real= Label(root, text = translations[combo_lang.get()]["real_part"])
label_real.place(x=0, y=145, width=200, height = 25)

entry_real= Entry(text="", validate="key", validatecommand=(root.register(validate_float_entry), "%P"))
entry_real ["justify"] = "center" 
entry_real.place(x=200, y=145, width=170, height = 25)

label_complex= Label(root, text = translations[combo_lang.get()]["imag_part"])
label_complex.place(x=0, y=185, width=200, height = 25)

entry_complex= Entry(text="", validate="key", validatecommand=(root.register(validate_float_entry), "%P"))
entry_complex ["justify"] = "center" 
entry_complex.place(x=200, y=185, width=170, height = 25)

label_precision= Label(root, text = translations[combo_lang.get()]["precision"])
label_precision.place(x=0, y=225, width=275, height = 25)

combo_precision = ttk.Combobox(root, values=[x for x in range(1, 11)], justify="center", state='readonly')
combo_precision.set("1")
combo_precision.place(x=313, y=225, width=50, height = 25)

label_result= Label(root, text = translations[combo_lang.get()]["root"])
label_result.place(x=33, y=305, width=100, height = 25)

entry_result= Entry(state='readonly')
entry_result ["justify"] = "center" 
entry_result.place(x=165, y=305, width=220, height = 25)

calculation_btn = ttk.Button(text = translations[combo_lang.get()]["calc"], style='brown.TButton', command = calculation)
calculation_btn.place(x=125, y=265, width=150)

doc_btn = ttk.Button(text = translations[combo_lang.get()]["doc"], style='brown.TButton', command = doc)
doc_btn.place(x=125, y=345, width=150)

label_tech_sup= Label(root, text = "Техническая поддержка: 8-800-235-35-35")
label_tech_sup.place(x=0, y=375, width=400, height = 25)

if __name__ == "__main__":
    root.protocol("WM_DELETE_WINDOW", close_window)
    root.mainloop()
    