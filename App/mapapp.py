import customtkinter as ctk

import ToggelFrame as TFrame
from HelperFrame import Search_Frame, Layer_Frame, Marker , History
import Map 

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode('dark')

class App(ctk.CTk):

    APP_NAME = "Map's View"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)
        self.iconbitmap('App\Images\icon.ico')

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.Toggel = TFrame.ToggelMenu(master=self, corner_radius=0, fg_color=None)
        self.Toggel.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.MapView= Map.Mapwidget(self)
        self.MapView.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        #=========================================== Button Functionas =================
        Search=self.Toggel.add_button(text='Search',image=["App/Images/dark mode/search.png","App/Images/light mode/search.png"])
        Search.configure(command=self.Search_Frame)

        Layers=self.Toggel.add_button(text='Tile Server Layout',image=["App/Images/dark mode/layers.png","App/Images/light mode/layers.png"])
        Layers.configure(command=self.layers_Frame)

        Marker=self.Toggel.add_button(text='Markers',image=["App/Images/dark mode/map-pin.png","App/Images/light mode/map-pin.png"])
        Marker.configure(command=self.Configure_marker_frame)

        Offline=self.Toggel.add_button(text='Offline Database',image=["App/Images/dark mode/database.png","App/Images/light mode/database.png"])
        Offline.configure(command=self.offline_Frame)

        #============================================= Functions Frames =====================
        self.SearchFrame=Search_Frame(master=self.Toggel.ButtonFrame,fg_color='transparent')

        #=============== Layers Functions ======================
        Array =["OpenStreetMap","Google normal","Google satellite","Paint Style","Black & White"]
        self.LayerFrame= ctk.CTkFrame(master=self.Toggel.ButtonFrame,fg_color='transparent')
        self.LayerFrame.grid(row=1,column=0,sticky='nsew')
        self.LayerFrame.columnconfigure(0,weight=1)

        for row,text in enumerate(Array):
            layer = Layer_Frame(self.LayerFrame,text=text,font=self.Toggel.Font,command=self.MapView.change_map)
            layer.grid(row=row,column=0,sticky='ew',pady=10,padx=(10,10))
            if row==0: layer.grid_configure(pady=(50,10))
        
        #================ Marker Functions ===================
        self.MarkerFrame= ctk.CTkFrame(master=self.Toggel.ButtonFrame,fg_color='transparent')
        self.MarkerFrame.grid(row=1,column=0,sticky='nsew')

        self.Search_Entry = ctk.CTkEntry(master=self.MarkerFrame,width=250,height=35,
                                            placeholder_text="Type Address")
        self.Search_Entry.grid(row=0, column=0, sticky="we", padx=(12, 12), pady=12,columnspan=2)
        
        self.SetMarkerButton = ctk.CTkButton(master=self.MarkerFrame,text="Set Marker")
        self.SetMarkerButton.grid(pady=20, padx=(20, 20), row=1, column=0)

        self.RemoveMarkerButton = ctk.CTkButton(master=self.MarkerFrame,text="Clear Markers")
        self.RemoveMarkerButton.grid(pady=20, padx=(20, 20), row=1, column=1)

        #================= Offline Frame ==========================
        self.OfflineFrame= ctk.CTkFrame(master=self.Toggel.ButtonFrame,fg_color='transparent')
        self.OfflineFrame.grid(row=1,column=0,sticky='nsew')

        self.OfflineFrame.columnconfigure(0,weight=1)

        frame=ctk.CTkFrame(master=self.OfflineFrame,corner_radius=15)
        frame.grid(row=0,column=0,sticky='ew',padx=(10,10),pady=(20,0))

        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(1,weight=0)

        ctk.CTkLabel(master=frame, text="Offline Maps", font=self.Toggel.Font,anchor='w').grid(row=0,column=0,sticky='ew',padx=(30,20),pady=(10,10))

        offlineSwitch = ctk.CTkSwitch(master=frame,text="",width=20,command= lambda : self.offline_command(offlineSwitch))
        offlineSwitch.grid(row=0,column=1,sticky='ew',padx=(10,20),pady=(10,10))

    def Search_Frame(self):
        Frame= ctk.CTkFrame(master=self.SearchFrame,fg_color='transparent')
        Frame.grid(row=2,column=0,sticky='nsew',columnspan=2)
        Frame.grid_columnconfigure((0,1),weight=1)
        row=2
        for count,history_object in enumerate(self.MapView.search_history) :
            marker=History(Frame,text=history_object,font=self.Toggel.Font,
                          command=[self.SearchFrame.Search_Entry, self.MapView.Remove_search, self.Search_Frame])
            count=count+1
            col= 1 if count%2==0 else 0
            marker.grid(pady=(10, 0), padx=(10,10), row=row,column=col,sticky='ew')
            row= row+1 if count%2==0 else row

        self.SearchFrame.tkraise()
        self.Toggel.Showframe()

    def layers_Frame(self):
        self.LayerFrame.tkraise()
        self.Toggel.Showframe()

    def Configure_marker_frame(self):
        Frame= ctk.CTkFrame(master=self.MarkerFrame,fg_color='transparent')
        Frame.grid(row=2,column=0,sticky='nsew',pady=10,columnspan=2)
        Frame.grid_columnconfigure(0,weight=1)
        for row,marker_object in enumerate(self.MapView.marker_list) :
            marker=Marker(Frame,marker=marker_object,font=self.Toggel.Font,
                          command=[self.MapView.set_position, self.MapView.Remove_marker, self.Configure_marker_frame])
            marker.grid(pady=(10, 0), padx=(20,0), row=row+1,sticky='ew')
        
        self.MarkerFrame.tkraise()
        self.Toggel.Showframe()

    def offline_command(self, offlineMap):

        if offlineMap.get() == 0 :
            self.MapView= Map.Mapwidget(self,use_database_only=False)
        else:
            self.MapView= Map.Mapwidget(self, use_database_only=True, max_zoom=15, database_path="offline_tiles.db")
        
        self.MapView.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

    def offline_Frame(self):
        self.OfflineFrame.tkraise()
        self.Toggel.Showframe()

    def start(self):
        self.mainloop()
