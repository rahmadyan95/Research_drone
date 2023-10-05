import tkinter as tk
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Video Viewer")
root.state('zoomed') 
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Video Source 
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)
cap3 = cv2.VideoCapture(0)  
cap4 = cv2.VideoCapture(0)  

half_width = screen_width // 2
half_height = screen_height // 2 

frame1 = tk.Frame(root, width=half_width, height=half_height)
frame1.grid(row=0, column=0, padx=5, pady=5)  

frame2 = tk.Frame(root, width=half_width, height=half_height)
frame2.grid(row=0, column=1, padx=5, pady=5)  

frame3 = tk.Frame(root, width=half_width, height=half_height)
frame3.grid(row=1, column=0, padx=5, pady=5)  

frame4 = tk.Frame(root, width=half_width, height=half_height)
frame4.grid(row=1, column=1, padx=5, pady=5)  

def resize_frame(frame, width, height):
    return cv2.resize(frame, (width, height))

def show_frame1():
    ret, frame = cap1.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = resize_frame(frame, half_width, half_height)
        cv2.putText(frame, "Camera 1", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 , 128, 0), 2)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label1.imgtk = imgtk
        label1.configure(image=imgtk)
        label1.after(10, show_frame1)  

def show_frame2():
    ret, frame = cap2.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = resize_frame(frame, half_width, half_height)
        cv2.putText(frame, "Camera 2", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 , 128, 0), 2)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label2.imgtk = imgtk
        label2.configure(image=imgtk)
        label2.after(10, show_frame2) 

def show_frame3():
    ret, frame = cap3.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = resize_frame(frame, half_width, half_height)
        cv2.putText(frame, "Camera 3", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 , 128, 0), 2)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label3.imgtk = imgtk
        label3.configure(image=imgtk)
        label3.after(10, show_frame3)  

def show_frame4():
    ret, frame = cap4.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = resize_frame(frame, half_width, half_height)
        cv2.putText(frame, "Camera 4", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 , 128, 0), 2)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label4.imgtk = imgtk
        label4.configure(image=imgtk)
        label4.after(10, show_frame4) 

label1 = tk.Label(frame1)
label1.pack()

label2 = tk.Label(frame2)
label2.pack()

label3 = tk.Label(frame3)
label3.pack()

label4 = tk.Label(frame4)
label4.pack()

show_frame1()
show_frame2()
show_frame3()
show_frame4()

root.mainloop()
