import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
#Functionality of widgets
def showtext():
	#messagebox.showinfo("https://www.maps.com")
	messagebox.showinfo(title="Live Location",message="https://www.maps.com")

window = tkinter.Tk()
window.title("Wolooc v0.1 beta")
#window.geometry("900x600")
#frame= tkinter.Frame(bg="#333333")
bg_image = Image.open("bgwin.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tkinter.Canvas(window,height=bg_image.height,width=bg_image.width)
canvas.pack(fill="both",expand=True)
canvas.create_image(0,0,image=bg_photo,anchor="nw")
frame = tkinter.Frame(canvas, bg="white")
#Label
#bg_label = tkinter.Label(window,image=bg_photo)
#fill it in window
#bg_label.place(relwidth=1,relheight=1)
live = tkinter.Button(frame,text="Live Location",command=showtext,bg="#33d9ff",font={'Arial',24}) 

#Griding in "frame"
live.grid(row=0,column=2,columnspan=2)

#Packing "frame" in "window"
#frame.pack(pady=20)
frame.place(relwidth=1,relheight=1)

#Running the Tkinter
window.mainloop()
