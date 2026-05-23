#This is a very simple design, i am an begginer who try to learn
import customtkinter

def open_popup():
    popup = customtkinter.CTkToplevel(root)
    popup.title("Pop-up")
    popup.geometry("100x50")
    
    label = customtkinter.CTkLabel(master=popup, text="You have a virus!")
    label.place(relx=0.5, rely=0.5, anchor="center")



root = customtkinter.CTk()
root.title("Loggin page")
root.geometry("400x700")
customtkinter.set_appearance_mode("system")

button = customtkinter.CTkButton(master=root, text="This is an experiment", fg_color="transparent", corner_radius=32, border_width = 3, border_color = "white", command=open_popup)
button.place(x=125, y=125)

textbox = customtkinter.CTkTextbox(master=root, corner_radius=12, border_color="white")
textbox.place(relx=0.5, rely=0.5, anchor="center")
root.mainloop()
