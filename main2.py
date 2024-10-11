from customtkinter import *
import webbrowser
from PIL import Image,ImageTk
#import time
#defining variable
USER = ""
PASS = ""
url=""
img=Image.open("bgwin.jpg")

#functions for widgets
def login():
	username = user_entry.get()
	password = pass_entry.get()
	if username == USER and password == PASS:
		label_feedback.configure(text="Logged In",text_color="green")
		#to the main application window
		open_main_window()
	else:
		label_feedback.configure(text="Invalid",text_color="red")
def livelocation():
	webbrowser.open(url)

#main application
def open_main_window():
	#destroy the login page frame
	frame.destroy()
	#create new main frame
	main_frame = CTkFrame(window)
	main_frame.pack(pady=20)
	#adding widgets to the main frame
	label_main = CTkLabel(main_frame,
						text="Welcome to the command and center of the survelliance gadget.",
						padx=20)
	label_main.pack(pady=(10,10))
	window.after(2000,main_frame.destroy)
	
	#frames recreated
	main_frame = CTkFrame(window)
	left_frame= CTkFrame(window)
	#loading blurred image
	
	#adding widgets to recreated main frame
	live = CTkButton(main_frame,text="Live Location",
					corner_radius=32,fg_color="green",
					hover_color="black",command=livelocation)
	charge = CTkLabel(main_frame,corner_radius=25,
					fg_color="transparent",text="Charging Status:")
	charging_status= CTkProgressBar(main_frame,fg_color="white",
					orientation="horizontal",mode="determinate",
					progress_color="lightblue",width=200,height=2)
	charging_status.set(100)
	charging_status.start()
	emer_entry = CTkEntry(main_frame,placeholder_text="Message")
	emer_btn = CTkButton(main_frame,text="Send",corner_radius=2,
						width=20,height=20)
	profile= CTkLabel(left_frame)
	#geometry manager for widgets
	live.grid(row=1,column=1,padx=20,pady=40,columnspan=2)
	charge.grid(row=2,column=1)
	charging_status.grid(row=2,column=2,padx=10)
	emer_entry.grid(row=3,column=1,padx=20)
	emer_btn.grid(row=3,column=2)
	profile.grid(row=1,column=1)
	main_frame.pack(pady=60)
	left_frame.pack()
	#main_frame.pack(fill="both",expand=True)
	#background image to frame
	#bg_lblf= CTkLabel(main_frame,text="",image=bg_img)
	#bg_lblf.place(x=0,y=0)
	#def bg_resf(e):
	#	i = CTkImage(img,size=(900,600))
	#	bg_lblf.configure(text="",image=i)
	#main_frame.bind("<Configure>",bg_resf)
	
	
#creating a window
window = CTk()
window.geometry("900x600")
set_appearance_mode("dark")
window.title("Wolooc")

#loading image
bg_img=CTkImage(img)
bg_lbl= CTkLabel(window,text="",image=bg_img)
bg_lbl.place(x=0,y=0)

frame = CTkFrame(window)

#widgets login page
login_btn = CTkButton(master=frame,text="Login",
					bg_color="transparent",fg_color="green",
					hover_color="black",corner_radius=32,
					command=login)
user_entry = CTkEntry(master=frame,corner_radius=32,
					placeholder_text="Username")
pass_entry = CTkEntry(master=frame,corner_radius=32,show="*",
					placeholder_text="Password")
label_feedback = CTkLabel(frame, text="Login Page",
					font=('Arial',28),wraplength=200)

#geometry managaer for login page
label_feedback.grid(row=1,column=1,pady=20,padx=40)
user_entry.grid(row=2,column=1,pady=10,padx=40)
pass_entry.grid(row=3,column=1,pady=10,padx=40)
login_btn.grid(row=4,column=1,pady=20,padx=40)
frame.pack(pady=100)

#background image
def bg_res(e):
	i = CTkImage(img,size=(900,600))
	bg_lbl.configure(text="",image=i)

window.bind("<Configure>",bg_res)
window.mainloop()
