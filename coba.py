import tkinter as tk
import tkinter as tk
import tkinter as ttk
from tkinter import * 
from tkinter.ttk import *
from tkinter import*
import cv2
from PIL import Image, ImageTk

class main_frame:
    def __init__(self,root) :
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        

        self.battery_level = 100
        self.drone_speed = 20
        self.rpm_1 = 6000
        self.rpm_2 = 6000
        self.rpm_3 = 6000
        self.rpm_4 = 6000
        self.temp_1 = 40
        self.temp_2 = 40
        self.temp_3 = 40
        self.temp_4 = 40
        self.x = 10.13
        self.y = 23.435
        self.z = 43.535

        self.drone_status()
        self.main_video_frame()
        self.feed_camera_frame()

    def decrease_battery(self):
        if self.battery_level > 0:
            self.battery_level -= 1
            self.battery_progress["value"] = self.battery_level
            self.battery_label.config(text=f"{self.battery_level}%")
            self.root.after(10000, self.decrease_battery)

    def main_video_frame(self):
        self.frame_atas = tk.Frame(self.root, width=self.screen_width // 1.3, height=self.screen_height // 1.57, bg="white",
                              highlightbackground="black", highlightthickness=3)
        self.frame_atas.pack_propagate(False)
        self.frame_atas.pack(pady=10, padx=10, anchor=tk.NW)

        background_color = self.frame_atas.cget("bg")
        self.label_di_frame = tk.Label(self.frame_atas, text="Main Camera Video",
                                    font=("Consolas", 18), bg=background_color)
        self.label_di_frame.pack(pady=10)

    def drone_status(self):
        frame_kotak = tk.Frame(self.root, width=self.screen_width // 4.8, height=self.screen_height // 1.57, bg="white",
                              highlightbackground="black", highlightthickness=3)
        frame_kotak.pack_propagate(False)
        frame_kotak.place(x=1125, y=10)

        background_color = frame_kotak.cget("bg")
        label_judul_frame = tk.Label(frame_kotak, text="Drone Status", font=("Consolas", 18), bg=background_color)
        label_judul_frame.pack(pady=10)

        label_batere_frame = tk.Label(frame_kotak, text='Battery', font=("Consolas", 12), bg=background_color)
        label_batere_frame.place(x=5, y=60)
        label_batere_frame.pack_propagate(False)

        self.battery_label = tk.Label(frame_kotak, text=f"{self.battery_level}%", font=("Consolas", 12), bg=background_color)
        self.battery_label.place(x=180, y=60)
        label_batere_frame.pack_propagate(False)

        self.battery_progress = Progressbar(frame_kotak, length=100, maximum=100, value=self.battery_level)
        self.battery_progress.place(x=75, y=61)
        label_batere_frame.pack_propagate(False)

        speed_label = tk.Label(frame_kotak, text=f"Speed = {self.drone_speed} Km/h ", font=("Consolas", 11), bg="green", fg="white")
        speed_label.place(x=5, y=90)
        label_batere_frame.pack_propagate(False)

        rpm_frame = tk.Frame(frame_kotak, width=285, height=100, bg="white", highlightbackground="black", highlightthickness=2)
        rpm_frame.pack_propagate(False)
        rpm_frame.place(x=5, y=120)

        rpm_label = tk.Label(rpm_frame, text="Revolution Per Minute", font=("Consolas", 10), bg="yellow", fg="black")
        rpm_label.pack(pady=1)

        rpm_label = tk.Label(rpm_frame, text=f"Eng_1 = {self.rpm_1}\n\nEng_2 = {self.rpm_2}", font=("Consolas", 11), bg=background_color)
        rpm_label.place(x=5, y=30)

        rpm_label = tk.Label(rpm_frame, text=f"Eng_3 = {self.rpm_3}\n\nEng_4 = {self.rpm_4}", font=("Consolas", 11), bg=background_color)
        rpm_label.place(x=160, y=30)

        temprature_frame = tk.Frame(frame_kotak, width=285, height=100, bg="white", highlightbackground="black", highlightthickness=2)
        temprature_frame.pack_propagate(False)
        temprature_frame.place(x=5, y=225)

        rpm_label = tk.Label(temprature_frame, text="Temperature", font=("Consolas", 10), bg="yellow", fg="black")
        rpm_label.pack(pady=1)

        rpm_label = tk.Label(temprature_frame, text=f"Eng_1 = {self.temp_1} ºC\n\nEng_2 = {self.temp_2} ºC", font=("Consolas", 11), bg=background_color)
        rpm_label.place(x=5, y=30)

        rpm_label = tk.Label(temprature_frame, text=f"Eng_3 = {self.temp_3} ºC\n\nEng_4 = {self.temp_4} ºC", font=("Consolas", 11), bg=background_color)
        rpm_label.place(x=160, y=30)

        coordinates = tk.Frame(frame_kotak, width=285, height=100, bg="white", highlightbackground="black", highlightthickness=2)
        coordinates.place(x=5, y=330)
        coordinates.pack_propagate(False)

        rpm_label = tk.Label(coordinates, text="Coordinates", font=("Consolas", 10), bg="green", fg="white")
        rpm_label.pack(pady=1)

        coordinates_label = tk.Label(coordinates, text=f"X = {self.x}\tY = {self.y}\n\nZ = {self.z}", font=("Consolas", 11), bg=background_color)
        coordinates_label.pack(pady=1)

        self.decrease_battery()

    def feed_camera_frame(self):
        frame_bawah = tk.Frame(self.root, width=self.screen_width // 1.015, height=self.screen_height // 3.4, bg="white",
                            highlightbackground="black", highlightthickness=3)
        frame_bawah.pack_propagate(False)
        frame_bawah.pack(pady=2)
        background_color = frame_bawah.cget("bg")
        label_di_frame = tk.Label(frame_bawah, text="Feed Camera",
                                font=("Consolas", 18), bg=background_color)
        label_di_frame.pack(pady=10)





if __name__ == '__main__':
    root = tk.Tk()
    root.title("Video Viewer")
    root.state('zoomed')
    root.resizable(False, False)
    app = main_frame(root)

    root.mainloop()