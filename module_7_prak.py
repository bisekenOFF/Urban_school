import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберете файл", filetypes=(('Текстовый файл', '.txt'),
                                                                                            ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


def info():
    Window_inf = tkinter.Tk()
    Window_inf.title('Инфо')
    Window_inf.geometry('350x150')
    Window_inf.configure(bg='black')
    #Window_inf.resizable(width=False, height=False)
    text_inf = tkinter.Label(Window_inf, text='Тут должна быть информация как работать с блокнотом', height=5, width=65,
                             background='silver', foreground='blue')
    text_inf.grid(column=1, row=1)
    Window_inf.mainloop()


Window = tkinter.Tk()
Window.title('Проводник')
Window.geometry('350x350')
Window.configure(bg='black')
Window.resizable(width=False, height=False)
text = tkinter.Label(Window, text='Файл:', height=5, width=65, background='silver', foreground='blue')
text.grid(column=1, row=1)

button_select = tkinter.Button(Window, width=20, height=3, text='Выбрать файл', background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)

button_select1 = tkinter.Button(Window, width=20, height=3, text='Инфо', background='silver', foreground='blue',
                                command=info)
button_select1.grid(column=1, row=3, pady=5)
Window.mainloop()
