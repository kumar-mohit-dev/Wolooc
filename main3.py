from customtkinter import *
import webbrowser
from PIL import Image
user=""
password=""
#bg1
#bg2=
bg3=Image.open("bgwin.jpg")
#function for 
def loginn():
	USERR=user_entry.get()
	PASSWORDD=pass_entry.get()
	if USERR==user and PASSWORDD==password:
		frame.destroy()
		frameleft.destroy()
		open_main_window()
	else:
		welcome.configure(text="Invalid",text_color="red")
			
def open_main_window():
	outframe=CTkFrame(window,corner_radius=0,width=600,height=900,
					fg_color="#D9D9D9")
	outframe.grid(row=1,column=1)
	frame=CTkFrame(outframe,corner_radius=15,width=350,height=300,
					fg_color="white")
    frame.grid(row=1,column=1)#widgets in main function
    
	taser=CTkLabel(frame,text="Taser",fg_color="white")#ss
	taser.grid(row=1,column=1)
	
	bg_label=CTkLabel(outframe,image=CTkImage(dark_image=bg3,
					size=(900,600)),text="")
	bg_label.grid(row=1,column=1)
	
#creating window
window = CTk()
window.title("Wolooc")
window.geometry("900x600")

frameleft=CTkFrame(window,width=450,height=600,fg_color="black"
				,corner_radius=0)
frameleft.grid(row=1,column=1)

frame=CTkFrame(frameleft,corner_radius=15,width=400,height=350,
				fg_color="#D9D9D9")
frame.grid(row=1,column=1,padx=60,pady=125)

#widgets in frame
welcome=CTkLabel(frame,text="Welcome Back \nLogin Account",
				text_color="black",font=("",35,"bold"))
welcome.grid(row=1,column=1,pady=20,padx=20,sticky="nw")

user_entry=CTkEntry(frame,placeholder_text="Username",width=200,
				height=50,corner_radius=20,fg_color="black",
				text_color="white",font=("",14,"bold"))
user_entry.grid(row=2,column=1,sticky="nw",padx=20)

pass_entry=CTkEntry(frame,placeholder_text="Password",show="*",
				fg_color="black",text_color="white",width=200,
				height=50,font=("",14,"bold"),corner_radius=20)
pass_entry.grid(row=3,column=1,pady=20,sticky="nw",padx=20)

crt_acc=CTkButton(frame,text="Create Account",text_color="blue",
				fg_color="transparent",hover_color="#D9D9D9",
				cursor="hand2")
crt_acc.grid(row=4,column=1,sticky="nw",pady=20)

login=CTkButton(frame,width=50,height=30,text="Login",
				font=("",10,"bold"),fg_color="blue",cursor="hand2"
				,command=loginn)
login.grid(row=4,column=1,sticky="e",pady=5)

window.mainloop()
