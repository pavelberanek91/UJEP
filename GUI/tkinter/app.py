import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk


class GUI:
    def __init__(self):
        self.vytvor_zakladni_okno()
        self.create_main_frame()
        self.create_button_frame()
        self.create_change_frame()
        self.vytvor_menu()

        self.zakladni_okno.mainloop()

    def vytvor_zakladni_okno(self):
        self.sirka_zakladniho_okna = 1200
        self.vyska_zakladniho_okna = 700
        self.zakladni_okno = tk.Tk()
        self.zakladni_okno.geometry(f"{self.sirka_zakladniho_okna}x{self.vyska_zakladniho_okna}")
        self.zakladni_okno.config(bg='white')
        self.zakladni_okno.title("Window")

    def create_main_frame(self):
        self.main_frame = tk.Frame(
            self.zakladni_okno, 
            width=self.sirka_zakladniho_okna, 
            height=self.vyska_zakladniho_okna, 
            bg="powder blue"
        )
        self.main_frame.grid_propagate(0)
        self.main_frame.pack()

    def create_button_frame(self):
        self.button_frame = tk.Frame(
            master=self.main_frame, background="#f2e583",
            width=self.sirka_zakladniho_okna/4,
            height=self.vyska_zakladniho_okna-100
        )

        self.button_frame.pack_propagate(0)
    
        self.button1 = tk.Button(
            self.button_frame, 
            text="Notebook", 
            font=('Ariel', 24), 
            width=15, 
            height=3, 
            background="#737270", 
            relief="groove", 
            activebackground='#b3b1af', 
            command=self.Notebook
        )

        self.button2 = tk.Button(
            self.button_frame, 
            text="Image", 
            font=('Ariel', 24), 
            width=15, 
            height=3, 
            background="#737270", 
            relief="groove", 
            activebackground='#b3b1af', 
            command=self.Image
        )

        self.button1.pack(padx=50, pady= 35)
        self.button2.pack(padx=50, pady= 35)

        self.button_frame.grid(padx= 25, pady= 50, column = 4, row = 0, rowspan=4)

    def create_change_frame(self):
        self.left_side_frame = tk.Frame(
            self.main_frame, 
            width=3*self.sirka_zakladniho_okna/4-100,
            height=self.vyska_zakladniho_okna-100, 
            bg="powder blue"
        )

        self.left_side_frame.pack_propagate(0)
        
        self.change_frame = tk.Frame(
            self.left_side_frame, 
            width=3*self.sirka_zakladniho_okna/4-100,
            height=self.vyska_zakladniho_okna-300, 
            bg="black"
        )
                
        self.bottom_left_frame = tk.Frame(
            self.left_side_frame, 
            width=3*self.sirka_zakladniho_okna/4-100,
            height= self.vyska_zakladniho_okna-500,
            bg= "yellow"
        )

        self.Notebook()
        self.change_frame.pack(fill="both", expand=1)
        self.bottom_left_frame.pack(fill='both', expand=1)      
        self.left_side_frame.grid(
            padx= 25, 
            pady= 50, 
            row= 0, 
            column= 0, 
            rowspan=3, 
            columnspan=3
        )

    def vytvor_menu(self):
        self.menu = tk.Menu(self.zakladni_okno, tearoff=1)
        
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.option = tk.Menu(self.menu, tearoff=0)

        save_button = tk.Button(self.file_menu)
        self.file_menu.add_cascade(label="Save", menu=save_button)

        self.color_menu = tk.Menu(self.option, tearoff=0)
        change_color_button = tk.Button(self.color_menu)
        
        self.color_menu.add_cascade(
            label="Outer Window", 
            menu=change_color_button, 
            command= self.change_color_main
        )

        self.color_menu.add_cascade(
            label="Button Frame", 
            menu=change_color_button, 
            command= self.change_color_btnframe
        )

        self.color_menu.add_cascade(
            label="Buttons", 
            menu=change_color_button, 
            command= self.change_color_button
        )

        self.option.add_cascade(label="Change color", menu= self.color_menu)
        
        self.menu.add_cascade(label="Soubor", menu=self.file_menu)
        self.menu.add_cascade(label="Filtry", menu=self.option)
        self.zakladni_okno.config(menu=self.menu)

    def Notebook(self):
        self.change_window_destroyer()
        for childen in self.button_frame.winfo_children():
            childen['state'] = "normal" 
        self.button1['state'] = "disable"      
        self.field = tk.Text(master=self.change_frame, bg="white", font=('Ariel', 11))
        self.field.pack(fill='both', expand=True)
        self.Notebook_bottom()

    def Notebook_bottom(self):
        options1 = ['Ariel', 'Times', 'Times New Roman']
        self.font = tk.StringVar()
        self.font.set('Ariel')
        options2 = ['11', '12', '16', '24']
        self.size = tk.StringVar()
        self.size.set('11')

        drop1 = tk.OptionMenu(self.bottom_left_frame, self.font, *options1)
        drop2 = tk.OptionMenu(self.bottom_left_frame, self.size, *options2)
        button = tk.Button(self.bottom_left_frame, text="Change", command=self.change_font)

        drop1.grid(row=0, column=0, padx= 100, pady= 75)
        drop2.grid(row=0, column=1, padx= 100)
        button.grid(row=0, column=2, padx= 100)

    def Image(self):
        self.change_window_destroyer()
        for childen in self.button_frame.winfo_children():
            childen['state'] = "normal"
        self.button2['state'] = "disable"
        
        self.image_window = tk.Toplevel(self.zakladni_okno)
        self.image_counter = 0
        self.load_images()

        self.img_lable = tk.Label(
            master= self.image_window, 
            image=self.images[self.image_counter]
        )

        frame = tk.Frame(self.image_window, bg="#bdbbb5")

        button1 = tk.Button(master=frame, text="<<", state="disable" ,command=self.back)
        label = tk.Label(master=frame, text=f"{self.image_counter+1}/{len(self.images)}")
        button2 = tk.Button(master=frame, text=">>", command=self.forward)
        
        button1.grid(row=0, column= 0, padx=10)
        label.grid(row=0, column= 1)
        button2.grid(row=0, column= 2, padx=10)

        self.img_lable.pack()
        frame.pack()
        self.image_window.mainloop()

    def change_font(self):
        self.field.config(font=(str(self.font.get()), self.size.get()))
        self.zakladni_okno.update()

    def back(self):
        self.image_counter -= 1
        for childen in self.image_window.winfo_children():
            childen.destroy()

        self.img_lable = tk.Label(
            master= self.image_window, 
            image=self.images[self.image_counter]
        )

        frame = tk.Frame(self.image_window, bg="#bdbbb5")

        button1 = tk.Button(master=frame, text="<<",command=self.back)
        label = tk.Label(master=frame, text=f"{self.image_counter+1}/{len(self.images)}")
        button2 = tk.Button(master=frame, text=">>", command=self.forward)

        if self.image_counter == 0:
            button1.config(state='disable')
        
        button1.grid(row=0, column= 0, padx=10)
        label.grid(row=0, column= 1)
        button2.grid(row=0, column= 2, padx=10)

        self.img_lable.pack()
        frame.pack()

    def forward(self):
        self.image_counter += 1
        for childen in self.image_window.winfo_children():
            childen.destroy()

        self.img_lable = tk.Label(
            master=self.image_window, 
            image=self.images[self.image_counter]
        )

        frame = tk.Frame(self.image_window, bg="#bdbbb5")

        button1 = tk.Button(master=frame, text="<<", command=self.back)
        label = tk.Label(master=frame, text=f"{self.image_counter+1}/{len(self.images)}")
        button2 = tk.Button(master=frame, text=">>", command=self.forward)

        if self.image_counter+1 == len(self.images):
            button2.config(state='disable')
        
        button1.grid(row=0, column= 0, padx=10)
        label.grid(row=0, column= 1)
        button2.grid(row=0, column= 2, padx=10)

        self.img_lable.pack()
        frame.pack()

    def change_window_destroyer(self):
        for childen in self.change_frame.winfo_children():
            childen.destroy()

    def load_images(self):
        img1 = ImageTk.PhotoImage(Image.open("Images/Image1.jpg"))
        img2 = ImageTk.PhotoImage(Image.open("Images/Image2.jpg"))
        img3 = ImageTk.PhotoImage(Image.open("Images/Image3.jpg"))
        self.images = [img1, img2, img3]

    def change_color_main(self):
        barva = colorchooser.askcolor()        
        self.main_frame.config(bg=str(barva[1]))

    def change_color_btnframe(self):
        barva = colorchooser.askcolor()
        self.button_frame.config(bg=str(barva[1]))

    def change_color_button(self):
        barva = colorchooser.askcolor()
        for childen in self.button_frame.winfo_children():
            childen.config(bg=str(barva[1]))

GUI()