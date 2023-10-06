import tkinter as tk
import tkinter as ttk
from tkinter import * 
from tkinter.ttk import *
from tkinter import*
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Video Viewer")
root.state('zoomed')
root.resizable(False, False)

# ukuran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Temprature Dummy Data
temp_1 = 40
temp_2 = 40
temp_3 = 40
temp_4 = 40

# coordinates
x = 10.13
y = 23.435
z = 43.535


battery_level = 100
drone_speed = 20
rpm_1 = 6000 # pasangkan ini nanti ke sensor
rpm_2 = 6000 # dummy data
rpm_3 = 6000
rpm_4 = 6000

# Input camera
cap = cv2.VideoCapture(0)
# cam_2 = cv2.VideoCapture(0)
# cam_3 = cv2.VideoCapture(0)
# cam_4 = cv2.VideoCapture(0)

# Kotak Main video

def main_video():
    
    
    def update_video():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (1080, 600))
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            canvas_video.create_image(0, 0, image=photo, anchor=tk.NW)
            canvas_video.photo = photo
            root.after(10, update_video)  # Update the video feed every 10 milliseconds
        else:
            cap.release()

    frame_atas = tk.Frame(root, width=screen_width // 1.3, height=screen_height // 1.57, bg="white",
                          highlightbackground="black", highlightthickness=3)
    frame_atas.pack_propagate(False)
    frame_atas.pack(pady=10, padx=10, anchor=tk.NW)

    background_color = frame_atas.cget("bg")
    label_di_frame = tk.Label(frame_atas, text="Main Camera Video",
                              font=("Consolas", 18), bg=background_color)
    label_di_frame.pack(pady=10)

    canvas_video = tk.Canvas(frame_atas, width=1080, height=600)
    canvas_video.pack()
    update_video()


# Kotak Drone Status

def drone_status():
    frame_kotak = tk.Frame(root, width=screen_width // 4.8, height=screen_height // 1.57, bg="white",
                           highlightbackground="black", highlightthickness=3)
    frame_kotak.pack_propagate(False)
    frame_kotak.place(x=1125, y=10)

    background_color = frame_kotak.cget("bg")
    label_judul_frame = tk.Label(frame_kotak,
                                 text="Drone Status",
                                 font=("Consolas", 18), bg=background_color)
    label_judul_frame.pack(pady=10)

    def decrease_battery():
        global battery_level
        if battery_level > 0:
            battery_level -= 1
            battery_progress["value"] = battery_level
            battery_label.config(text=f"{battery_level}%")
            root.after(10000, decrease_battery)

    label_batere_frame = tk.Label(frame_kotak,
                                  text=f'Battery',
                                  font=("Consolas", 12), bg=background_color)
    label_batere_frame.place(x=5, y= 60)
    label_batere_frame.pack_propagate(False)
    
    battery_label = tk.Label(frame_kotak, text=f"{battery_level}%", font=("Consolas", 12),bg=background_color)
    battery_label.place(x=180,y=60)
    label_batere_frame.pack_propagate(False)

    battery_progress = Progressbar(frame_kotak, length=100, maximum=100, value=battery_level)
    battery_progress.place(x=75 ,y = 61)
    label_batere_frame.pack_propagate(False)

    speed_label = tk.Label(frame_kotak, text=f"Speed    = {drone_speed} Km/h ", font=("Consolas", 11),bg="green",fg="white")
    speed_label.place(x=5,y=90)
    label_batere_frame.pack_propagate(False)

    # RPM Field

    rpm_frame = tk.Frame(frame_kotak, width=285, height=100, bg="white",
                           highlightbackground="black", highlightthickness=2)
    rpm_frame.pack_propagate(False)
    rpm_frame.place(x=5, y=120)

    rpm_label = tk.Label(rpm_frame,
                                 text="Revolution Per Minute",
                                 font=("Consolas", 10), bg="yellow",fg="black")
    rpm_label.pack(pady=1)

    rpm_label = tk.Label(rpm_frame,
                                 text=f"Eng_1 = {rpm_1}\n\nEng_2 = {rpm_2}",
                                 font=("Consolas", 11), bg=background_color)
    rpm_label.place(x=5, y= 30)

    rpm_label = tk.Label(rpm_frame,
                                 text=f"Eng_3 = {rpm_3}\n\nEng_4 = {rpm_4}",
                                 font=("Consolas", 11), bg=background_color)
    rpm_label.place(x=160, y= 30)

    # Frame Temprature

    temprature_frame = tk.Frame(frame_kotak, width=285, height=100, bg="white",
                           highlightbackground="black", highlightthickness=2)
    temprature_frame.pack_propagate(False)
    temprature_frame.place(x=5, y=225)

    rpm_label = tk.Label(temprature_frame,
                                 text=" Temprature ",
                                 font=("Consolas", 10), bg="yellow",fg="black")
    rpm_label.pack(pady=1)

    rpm_label = tk.Label(temprature_frame,
                                 text=f"Eng_1 = {temp_1} ºC\n\nEng_2 = {temp_2} ºC",
                                 font=("Consolas", 11), bg=background_color)
    rpm_label.place(x=5, y= 30)

    rpm_label = tk.Label(temprature_frame,
                                 text=f"Eng_3 = {temp_3} ºC\n\nEng_4 = {temp_4} ºC",
                                 font=("Consolas", 11), bg=background_color)
    rpm_label.place(x=160, y= 30)

    
    # Coordinates 

    coordinates = tk.Frame(frame_kotak, width=285, height=100, bg="white",
                           highlightbackground="black", highlightthickness=2)
    coordinates.place(x=5, y=330)
    coordinates.pack_propagate(False)
    

    rpm_label = tk.Label(coordinates,
                         text=" Coordinates ",
                         font=("Consolas", 10), bg="green",fg="white")
    rpm_label.pack(pady=1)

    coordinates_label = tk.Label(coordinates,
                                 text=f"X = {x}\tY = {y}\n\nZ = {z}",
                                 font=("Consolas", 11), bg=background_color)
    coordinates_label.pack(pady=1)



    
    decrease_battery()



# kotak Feed Camera

def feed_camera():
    frame_bawah = tk.Frame(root, width=screen_width // 1.015, height=screen_height // 3.4, bg="white",
                           highlightbackground="black", highlightthickness=3)
    frame_bawah.pack_propagate(False)
    frame_bawah.pack(pady=2)
    background_color = frame_bawah.cget("bg")
    label_di_frame = tk.Label(frame_bawah, text="Feed Camera",
                              font=("Consolas", 18), bg=background_color)
    label_di_frame.pack(pady=10)

    

if __name__ == '__main__':
    main_video()
    drone_status()
    feed_camera()
    root.mainloop()
