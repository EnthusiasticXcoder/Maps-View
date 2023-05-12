import customtkinter as ctk
import mapapp


app = mapapp.App()
def marker_box(coords=None):
    markerInput=ctk.CTkInputDialog(title='Marker Name',text="Marker Input")
    if coords != None :
        app.MapView.add_marker(coords=coords,marker_text=markerInput.get_input())
    else : 
        app.MapView.add_marker(marker_text=markerInput.get_input())
    app.Configure_marker_frame()
    
def Clear_Marker():
    app.MapView.clear_markers()
    app.Configure_marker_frame()
    
def Search_Location(event = None):
    app.MapView.search_event(app.SearchFrame.Search_Entry.get())
    app.SearchFrame.Search_Entry.delete(0,'end')
    app.Search_Frame()

def clear_Command():
    app.MapView.Clear_Search_History()
    app.Search_Frame()
    
def Marker_Location(event = None):
    app.MapView.search_event(app.Search_Entry.get())
    app.Search_Entry.delete(0,'end')

app.MapView.add_right_click_menu_command("Set Marker",command=marker_box,pass_coords=True)
    
app.SearchFrame.Search_Entry.bind("<Return>", Search_Location)
app.SearchFrame.Search_Button.configure(command=Search_Location)

app.SetMarkerButton.configure(command=marker_box)
app.RemoveMarkerButton.configure(command=Clear_Marker)
app.Search_Entry.bind("<Return>", Marker_Location )

app.SearchFrame.ClearButton.configure(command = clear_Command)

app.start()
with open('data.txt','w') as file:
    for marker in app.MapView.marker_list:
        file.write(f'{marker.position[0]},{marker.position[1]},{marker.text},{marker.image},{marker.icon}\n')
with open('History.txt','w') as file :
    for history in app.MapView.search_history :
        file.write(f"{history}\n")