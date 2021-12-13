from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Road Accident Avoiding System')
root.iconbitmap(default='resources/favicon.ico')

window_width = 800
window_height = 600
root.geometry(f'{window_width}x{window_height}')
root.minsize(width=window_width, height=window_height)

welcome_image = ImageTk.PhotoImage((Image.open('resources/welcome_screen.png')))
welcome_image_label = Label(root, image=welcome_image, borderwidth=10, relief=GROOVE)
options_frame = LabelFrame(root, text='Options', borderwidth=10, relief=GROOVE)
button_start = Button(options_frame, text='Start', width=25, pady=10, bg='lightgreen', activebackground='green')
button_exit = Button(options_frame, text='Exit', width=25, pady=10, command=root.quit, bg='red2', activebackground='red4')

welcome_image_label.pack(padx=100, pady=50)
options_frame.pack(padx=100, pady=50)
button_start.pack(padx=25, pady=10)
button_exit.pack(padx=25, pady=10)

root.mainloop()
