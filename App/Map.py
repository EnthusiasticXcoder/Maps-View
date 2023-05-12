import tkinter
import tkintermapview as CTkMap 


class Mapwidget(CTkMap.TkinterMapView):
    def __init__(self, *args, width: int = 300, height: int = 200, 
                 corner_radius: int = 0, bg_color: str = None, 
                 database_path: str = None, use_database_only: bool = False, 
                 max_zoom: int = 19, **kwargs):
        
        super().__init__(*args, width=width, height=height, 
                         corner_radius=corner_radius, 
                         bg_color=bg_color, database_path=database_path, 
                         use_database_only=use_database_only, 
                         max_zoom=max_zoom, **kwargs)

        self.marker_list = []
        self.search_history = []
        # load markers from file
        self.load_data()

        # Set default values
        self.set_address("Indore")
        self.add_left_click_map_command(self.click_zoom)
    
    def load_data(self):
        with open('History.txt','r') as file:
            data = file.readlines()
            for history in data :
                self.search_history.append(history.replace("\n",""))

        with open('data.txt','r') as file:
            marker_data=file.readlines()
            for data in marker_data :
                data=data.replace('\n',"")
                data=data.split(',')
                if data[3]=='None' and data[4]=='None':
                    self.marker_list.append(self.set_marker(deg_x=float(data[0]),deg_y=float(data[1]),text=data[2], command=self.click_marker_event))
                elif data[3]!='None':
                    self.marker_list.append(self.set_marker(deg_x=float(data[0]),deg_y=float(data[1]), text=data[2], 
                                image=data[3],image_zoom_visibility=(0, float("inf")), command=self.click_marker_event))
                elif data[4]!='None':
                    self.marker_list.append(self.set_marker(deg_x=float(data[0]),deg_y=float(data[1]), text=data[2], 
                                image=data[3],icon=data[4],image_zoom_visibility=(0, float("inf")), command=self.click_marker_event))
        
    def search_event(self, address : str | None, event=None):
        if not self.search_history.count(address) :
            self.search_history.append(address)
        self.set_address(address)
    
    def Clear_Search_History(self):
        with open('History.txt','w') as file :
            file.write("")
        self.search_history = []
    
    def Remove_search(self,Element: str = None):
        self.search_history.remove(Element)

    def click_marker_event(self,marker):
        def Hide_Show_Image():
            if marker.image_hidden is True:
                marker.hide_image(False)
            else:
                marker.hide_image(True)

        def MarkerText():
            pass

        def MarkerImage():
            pass

        m = tkinter.Menu(self, tearoff=0)
        m.add_command(label='Edit Text', command=lambda:MarkerText)
        m.add_command(label="Edit Image", command=lambda:MarkerImage)
        m.add_command(label="Hide/Show Image", command=lambda:Hide_Show_Image)

        position=marker.get_canvas_pos(marker.position)

        m.tk_popup(int(position[0]+self.winfo_rootx()),int(position[1]+self.winfo_rooty()))

        
    def add_marker(self,coords=None,marker_text=None):
        current_position = self.get_position() if coords == None else coords
        adr = CTkMap.convert_coordinates_to_address(current_position[0], current_position[1]) 
        marker_name= marker_text if marker_text!="" or " " else f'{adr.city}, {adr.state}, {adr.country}'
        self.marker_list.append(self.set_marker(current_position[0], current_position[1], text=marker_name, command=self.click_marker_event))
    
    def Remove_marker(self, Object_Marker):
        self.marker_list.remove(Object_Marker)

    def clear_markers(self):
        for marker in self.marker_list:
            marker.delete()
        self.marker_list=[]
        with open('data.txt','w') as file:
            file.write("")

    def click_zoom(self,coordinate):
        self.set_position(coordinate[0],coordinate[1])
        self.set_zoom(zoom=self.last_zoom+1)
    
    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Paint Style":   
            self.set_tile_server("http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png")
        elif new_map == "Black & White":
            self.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")

if __name__=='__main__':
    import customtkinter as ctk
    r=ctk.CTk()
    Mapwidget(r).pack(fill='both',expand=1)
    r.mainloop()