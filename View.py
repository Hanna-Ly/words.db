from tkinter import *
import tkinter.font as tkFont


class View(Tk): 
    
    def __init__(self, controller):
        super().__init__() 
        self.controller = controller
        self.userinput=StringVar()
        self.userinput_2=StringVar()
        self.defaultStyle = tkFont.Font(family='Verdana', size=10, weight='bold')  
        
        # Pohiaken      
        self.geometry('800x500') 
        self.resizable(True,True) 
        self.title('words.db')
        
        # Framede välja kutsumine
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        # Vidinad/Widgets
        self.delete_button()
        self.char_input, self.button= self.create_userinput()
        self.textbox = self.create_database_textbox()
        
    def main(self):
        self.mainloop()
        
    def create_top_frame(self):
        frame = Frame(self, height=50)
        frame.pack(expand = False, fill = X)
        return frame
    
    def create_bottom_frame(self):
        frame = Frame(self) 
        frame.pack(expand = True, fill ='both')
        return frame
    

        
    def create_userinput(self):
        label_info = Label(self.top_frame, text='Sisesta uus sõna:', font=self.defaultStyle)
        label_info.grid(row=1, column=0, padx=5, pady=5)
        
        char_input = Entry(self.top_frame, textvariable=self.userinput, justify='center', font=self.defaultStyle)
        char_input.grid(row=1,column=1, padx=5, pady=5)
        char_input.focus()
        
        button = Button(self.top_frame, text='Lisa tabelisse!', font=self.defaultStyle, borderwidth = 2, command=lambda:self.controller.btn_add_click())
        button.grid(row=1, column=2, padx=5, pady=5)
        
        return char_input, button,
    
    
    def delete_button(self):
        'Kustuta nupp'
        button = Button(self.top_frame, text='Kustuta valitud sõna!', font=self.defaultStyle, borderwidth = 2, command=lambda:self.controller.btn_delete_click())
        button.grid(row=2, column=2,padx=5,pady=5)
        
        
    def create_database_textbox(self):
        textbox = Text(self.bottom_frame, borderwidth = 0)
        textbox.pack(padx=5,pady=5)
        return textbox
    
    
    