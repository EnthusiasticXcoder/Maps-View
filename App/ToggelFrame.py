import tkinter as tk
import customtkinter as ctk
from typing import Tuple
from PIL import Image,ImageTk


class ToggelMenu(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, 
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = ('white','#2B2B2B'), 
                 border_color: str | Tuple[str, str] | None = None,
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
       
        super().__init__(master, 
                        width = width, height = height, 
                        corner_radius = corner_radius, 
                        border_width = border_width, 
                        bg_color = bg_color, 
                        fg_color = fg_color, 
                        border_color = border_color, 
                        background_corner_colors = background_corner_colors, 
                        overwrite_preferred_drawing_method = None, **kwargs)
        
        self.Font= ctk.CTkFont(family='Bookman Old Style',size=18,weight='bold')

        self.columnconfigure((0,1),weight=1)
        self.rowconfigure(0,weight=1)

        self.Frame= ctk.CTkFrame(master=self,fg_color='transparent')           # First toggel
        self.Frame.grid(row=0,column=0,sticky='nsew')

        self.ButtonFrame=ctk.CTkFrame(self,corner_radius=0)   # second Toggel
        self.ButtonFrame.columnconfigure(0,weight=1)
        
        #============= First Toggel Menu ===============================
        self.Frame.grid_rowconfigure(1, minsize=30)   # empty row with minsize as spacing
        self.Frame.grid_rowconfigure(12, weight=1)  # empty row as spacing
        self.Frame.grid_rowconfigure(14, minsize=15)    # empty row with minsize as spacing
        self.Frame.grid_rowconfigure(16, minsize=30)

        self.Frame.columnconfigure(2,minsize=15)
        
        self.imgmenu = ImageTk.PhotoImage(Image.open('App/Images/light mode/menu.png').resize((40,40)))
        self.imgx = ImageTk.PhotoImage(Image.open('App/Images/light mode/chevron-left.png').resize((50,50)))

        self.Buttonarray=[]  # Button array with [CTkButton class Object , Text , CTkImage class Object]

        #====================== First Toggel Frame ==================== 
        ModeChange = ctk.CTkOptionMenu(master=self.Frame,fg_color=('white','grey25'),text_color=('grey20','grey80'),
                                       button_color=('grey50','grey35'),button_hover_color=('grey40','grey20'),
                                            values=["Light", "Dark", "System"],
                                            command=ctk.set_appearance_mode)
        ModeChange.set('System')
        ModeSwitch = ctk.CTkSwitch(master=self.Frame,text="",width=0,command= lambda :self.change_mode(ModeSwitch))
        ModeSwitch.grid(row=15, column=0,sticky='ew',columnspan=3,padx=20)
   
        label=tk.Label(self.Frame,image=self.imgmenu,text=None,background='#2B2B2B',cursor='hand2')
        label.grid(row=0,column=0,sticky='w',padx=20,pady=20)
        Logo=ctk.CTkLabel(master=self.Frame,text="",image=ctk.CTkImage(light_image=Image.open('App/Images/Logo1.png'),
                            dark_image=Image.open("App/Images/Logo1.png"),size=(250,60)))

        #====================== Second Toggel Frame ====================
        self.ButtonFrame.columnconfigure(0,weight=1)
        self.ButtonFrame.rowconfigure(1,weight=1)

        Xbutton=ctk.CTkButton(self.ButtonFrame,fg_color='transparent',text="",image=self.loadImage(['App/Images/dark mode/x.png','App/Images/light mode/x.png'],30),width=0,command=lambda :Hide_Frame())
        Xbutton.grid(row=0,column=0,sticky='ne')
        #======================Configure toggel ========================

        def open(e):
            label.configure(image=self.imgx)
            Logo.grid(row=0,column=0,sticky='w',padx=5)
            label.grid_configure(column=3,sticky='e')
            if self.Buttonarray:
                for button in self.Buttonarray :
                    button[0].configure(text=button[1])
                    button[0].grid_configure(columnspan=4,sticky='ew')
            ModeSwitch.grid_forget()
            ModeChange.grid(row=15, column=0,padx=20,sticky='ew',columnspan=3)
            label.bind("<Button-1>",close)
            Hide_Frame()

        def close(e=None):
            label.configure(image=self.imgmenu)
            Logo.grid_forget()
            label.grid_configure(column=0,sticky='w')
            if self.Buttonarray:
                for button in self.Buttonarray :
                    button[0].configure(text="")
                    button[0].grid_configure(columnspan=1,sticky='w')
            ModeChange.grid_forget()
            ModeSwitch.grid(row=15, column=0,sticky='e',columnspan=3,padx=20)
            label.bind("<Button-1>",open)

        def Show_Frame():
            self.ButtonFrame.grid(row=0,column=1,sticky='nsew')
            close()
    
        def Hide_Frame():
            self.ButtonFrame.grid_forget() 
        
        label.bind("<Button-1>",open)
        self.Showframe=Show_Frame
    
    def add_button(self,image : list | None,text : str | None ):
        button =ctk.CTkButton(master=self.Frame,text="",image=self.loadImage(image,30),
                              font=self.Font, text_color=("grey5","grey80"),width=30,
                              compound='left',fg_color='transparent',anchor='sw',hover_color=('grey60','grey25'))
        self.Buttonarray.append([button,text,self.loadImage(image,30)])
        self.Update_Button()
        return button

    def Update_Button(self):
        for row,button in enumerate(self.Buttonarray) :
            button[0].grid(row=row+2,column=0,padx=(10,2),pady=10,sticky='w',columnspan=1)

    def loadImage(self,path,size):
        return ctk.CTkImage(light_image=Image.open(path[0]),
                            dark_image=Image.open(path[1]),
                            size=(size,size))  
    
    def change_mode(self,ModeSwitch):
        if ModeSwitch.get() == 0:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def scale_place(self,coordinate):
        coordinate=(coordinate*1/self._get_widget_scaling())
        return coordinate


if __name__=='__main__':
    def loadImage(path,size):
        return ctk.CTkImage(light_image=Image.open(path),
                            dark_image=Image.open(path),
                            size=(size,size))  
    r=ctk.CTk()
    r.geometry('200x200')
    #ctk.set_appearance_mode('light')
    r.rowconfigure(0, weight=1)
    r.columnconfigure(1, weight=1)
    # ============ create two frames ===
    a=ToggelMenu(master=r)
    a.grid(row=0,column=0,sticky='nsew')
    button=a.add_button(text='Home',image=["App/Images/dark mode/home.png",'App/Images/light mode/x.png'])
    button.configure(command=lambda:a.Showframe())
    
    r.mainloop()