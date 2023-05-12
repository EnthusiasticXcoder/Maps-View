import customtkinter as ctk
from PIL import Image
from typing import Tuple


class Search_Frame(ctk.CTkFrame):
    def __init__(self, master: any,
                 width: int = 200, height: int = 200,
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = None, 
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
        
        self.grid(row=1,column=0,sticky='nsew')

        self.Search_Entry = ctk.CTkEntry(master=self,width=250,height=35,
                                            placeholder_text="Type Address")
        self.Search_Entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        self.Search_Button = ctk.CTkButton(master=self,text="Search",width=90)
        self.Search_Button.grid(row=0, column=1, sticky="w", padx=(12,10), pady=12)
        
        # Clear history frame
        clearFrame = ctk.CTkFrame(master=self,fg_color='transparent')
        clearFrame.grid(row=1,column=0,sticky='nsew',columnspan=2)

        clearFrame.grid_columnconfigure(0,weight=1)
        clearFrame.grid_columnconfigure(1,weight=0)
        
        ctk.CTkFrame(master=clearFrame,fg_color='black',height=2).grid(row=0,column=0,padx=(5,1),sticky='ew')

        self.ClearButton = ctk.CTkButton(master=clearFrame,cursor='hand2',
                        text="Clear all",hover=False,width=0,
                        fg_color='transparent',text_color=('#01719D',"skyblue"),border_width=0,
                        font=("times new roman",18))
        self.ClearButton.grid(row=0,column=1,padx=(2,8))


class Layer_Frame(ctk.CTkFrame):
    def __init__(self, master: any,text : any,font : ctk.CTkFont | None,command : any,
                 width: int = 200, height: int = 200,
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = 'transparent', 
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
        
        self.columnconfigure(0,weight=1)
        button =ctk.CTkButton(master=self,text=text,font=font, text_color=('grey5','grey80'),
                              width=30,compound='left',fg_color='transparent',anchor='sw',hover_color=('grey60','grey25'),
                              command=lambda : command(text))
        button.grid(row=0,column=0,sticky='ew')
        
class Marker(ctk.CTkFrame):
    def __init__(self, master: any,marker : any,font : ctk.CTkFont | None,command : any,
                 width: int = 200, height: int = 200,
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = 'transparent', 
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
        self.columnconfigure(0,weight=1)
        self.marker_refrence=ctk.CTkButton(self,text=marker.text,font=font, text_color=('grey10','grey80'),
                    width=30,fg_color='transparent',anchor='sw',hover_color=('grey60','grey25'),
                    command=lambda: command[0](marker.position[0],marker.position[1]))
        self.marker_refrence.grid(row=0,column=0,sticky='ew')
        
        self.XButton = ctk.CTkButton(master=self,text="",fg_color='transparent',hover_color='red',width=20,
                                     command= lambda : self.XCommand(command , marker),
                                    image=ctk.CTkImage(dark_image=Image.open("App/Images/light mode/x.png"),
                                                       light_image=Image.open("App/Images/dark mode/x.png")))
        self.XButton.grid(row=0,column=1,sticky='e')
    
    def XCommand(self,command, Element):
        command[1](Element)
        command[2]()

class History(ctk.CTkFrame):
    def __init__(self, master: any,text : any,font : ctk.CTkFont | None,command : any,
                 width: int = 200, height: int = 200,
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = 'transparent', 
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
        self.columnconfigure(0,weight=1)
        self.historyButton=ctk.CTkButton(self,text=text,font=font,text_color=('grey10','grey80'),
                    width=30,fg_color='transparent',anchor='sw',hover_color=('grey60','grey25'),
                    command=lambda: self.Button_command(command[0],text))
        self.historyButton.grid(row=0,column=0,sticky='ew')

        self.XButton = ctk.CTkButton(master=self,text="",fg_color='transparent',hover_color='red',width=20,
                                    image=ctk.CTkImage(dark_image=Image.open("App/Images/light mode/x.png"),
                                                       light_image=Image.open("App/Images/dark mode/x.png")),
                                    command= lambda : self.XCommand(command , text))
        self.XButton.grid(row=0,column=1,sticky='e')

    def Button_command(self,command,text):
        command.delete(0,'end')
        command.insert(0,text)

    def XCommand(self,command, Element):
        command[1](Element)
        command[2]()

