import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from python_file import *



win = tk.Tk()
win.title = 'Emoji counter'
win.geometry('800x500')


def open_file():
    browse_text.set('Loading...')
    file = askopenfile(parent=win, mode='rb', title='Choose the file', )
    global file_name
    file_name = file.name
    browse_text.set('Browse another')
    browse_text.set('Browse another')


def insert_output():
    # dt = parse(str(start_date.get()))
    # print(dt)
    # print(dt.strftime('%d/%m/%Y'))
    if text_format_variable.get() == "Android":
        count_of_emojis = count_emoji_android(file_name, username.get(), start_date.get(), end_date.get())
    else:
        count_of_emojis = count_emoji_ios(file_name, username.get(), start_date.get(), end_date.get())
    if type(count_of_emojis[0]) == int:
        output.delete("1.0", "end")
        output.insert(END, 'In total there are ' + str(count_of_emojis[0]) + ' emojis for the users: ' + username.get() + '\n' +
                      'In total users: ' + username.get() + ' sent ' + str(count_of_emojis[1]) + ' messages' + '\n')
    elif type(count_of_emojis) == str:
        output.delete("1.0", "end")
        output.insert(END, count_of_emojis + '\n')


select = tk.Label(text='Select the chat text file')
browse_text = tk.StringVar()
browse_button = tk.Button(win, textvariable = browse_text, command=open_file, height=4, width=15, bg='blue', fg='white')
browse_text.set("Browse Text File")
browse_button.pack()

label = tk.Label(text='username')
username = tk.Entry()
label.pack()
username.pack()

label = tk.Label(text='start date (DD/MM/YYYY)')
start_date = tk.Entry()
label.pack()
start_date.pack()


label = tk.Label(text='end date (DD/MM/YYYY)')
end_date = tk.Entry()
label.pack()
end_date.pack()

output = Text(win, height=5, width=75, bg='light yellow')

count_button = Button(win, height=2, width=20, text='Count', command=insert_output)
count_button.pack()
output.pack()


text_format = tk.Frame()
text_format.pack()

text_format_variable = tk.StringVar(value="iPhone")
iphone_button = tk.Radiobutton(text_format, text="iPhone", variable=text_format_variable,
                            value="iPhone", width=8)
android_button = tk.Radiobutton(text_format, text="Android", variable=text_format_variable,
                            value="Android", width=8)

iphone_button.pack(side="left")
android_button.pack(side="left")



win.mainloop()
