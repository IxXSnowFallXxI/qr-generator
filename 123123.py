from tkinter import *
from tkinter import ttk
import qrcode
root = Tk()
root.geometry("400x500")
data = "https://github.com/IxXSnowFallXxI"
levels_ask = Label(root,
                   text="Уровень коррекции: ",
                   font=('Arial', 10,),
                   fg = 'black',
                   )
correcting_errors = {0: 'До 7% повреждений', 1: 'До 15% повреждений',
                     2: 'До 25% повреждений', 3: 'До 30% повреждений'}
correct_level = ttk.Combobox(values=[level for level in correcting_errors.values()])
levels_ask.place(x=10, y=10)
correct_level.place(x=180, y=10)
qr_size = ttk.Spinbox(from_=1.0, to=1000.0)
qr_size_ask = Label(root,
                    text="Размер QR-кода:",
                    font=('Arial', 10,),
                    fg = 'black',
                    )
qr_size_ask.place(x=10, y=60)
qr_size.place(x=180, y=60)

border_size_ask = Label(root,
                        text="Размер толщины рамки: ",
                        font=('Arial', 10,),
                        fg = 'black',
                        )
border_size = ttk.Spinbox(from_=1.0, to=10)
border_size_ask.place(x=10, y=110)
border_size.place(x=180, y=110)
#######################################
def qr_generator():
    global correcting_errors  
    select_level = correct_level.get()
    size_of_box = int(qr_size.get())
    print(size_of_box)
    border_coef = int(border_size.get())
    print(border_coef)
    reverse_dict = {v: k for k, v in correcting_errors.items()}
    print(reverse_dict[select_level])    
    qr = qrcode.QRCode(
        version = 2,
        error_correction = reverse_dict[select_level],
        box_size = size_of_box,
        border = border_coef,
        )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(
    fill_color="black",
    back_color="white"
    )
    img.show()
#--------------------------------------------->
start_btn = ttk.Button(text="START", command = qr_generator)
start_btn.place(x=100, y=200)                       
root.mainloop()
