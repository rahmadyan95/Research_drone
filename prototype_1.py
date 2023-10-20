import cv2
import tkinter as tk
from PIL import Image, ImageTk

class Camera:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Streams")

        self.canvas1 = tk.Canvas(self.root, width=640, height=480)
        self.canvas1.pack(side='left')

        self.canvas2 = tk.Canvas(self.root, width=640, height=480)
        self.canvas2.pack(side='right')

        self.canvas3 = tk.Canvas(self.root, width=640, height=480)
        self.canvas3.pack(side='bottom')

        self.cap1 = cv2.VideoCapture(0)
        self.cap2 = cv2.VideoCapture("test1.mp4")
        self.cap3 = cv2.VideoCapture("test2.mp4")

        self.current_canvas = 1  # Inisialisasi untuk menunjukkan video 1 di canvas 1

        # Tombol untuk mengganti tampilan video
        self.switch_button = tk.Button(self.root, text="Switch Videos", command=self.switch_videos)
        self.switch_button.pack()

        self.update()

    def switch_videos(self):
        if self.current_canvas == 1:
            self.current_canvas = 2
        elif self.current_canvas == 2:
            self.current_canvas = 3
        else:
            self.current_canvas = 1

        # Hapus semua gambar di semua canvas
        self.canvas1.delete("all")
        self.canvas2.delete("all")
        self.canvas3.delete("all")

    def resize_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1000, 680))
        return frame

    def update(self):
        ret1, frame1 = self.cap1.read()
        ret2, frame2 = self.cap2.read()
        ret3, frame3 = self.cap3.read()

        if ret1 and ret2 and ret3:
            frame1_resized = self.resize_frame(frame1)
            frame2_resized = self.resize_frame(frame2)
            frame3_resized = self.resize_frame(frame3)

            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(frame1_resized))
            self.photo2 = ImageTk.PhotoImage(image=Image.fromarray(frame2_resized))
            self.photo3 = ImageTk.PhotoImage(image=Image.fromarray(frame3_resized))

            if self.current_canvas == 1:
                self.canvas1.create_image(0, 0, image=self.photo1, anchor='nw')
                self.canvas2.create_image(0, 0, image=self.photo2, anchor='nw')
                self.canvas3.create_image(0, 0, image=self.photo3, anchor='nw')
            elif self.current_canvas == 2:
                self.canvas1.create_image(0, 0, image=self.photo2, anchor='nw')
                self.canvas2.create_image(0, 0, image=self.photo1, anchor='nw')
                self.canvas3.create_image(0, 0, image=self.photo3, anchor='nw')
            elif self.current_canvas == 3:
                self.canvas1.create_image(0, 0, image=self.photo3, anchor='nw')
                self.canvas2.create_image(0, 0, image=self.photo1, anchor='nw')
                self.canvas3.create_image(0, 0, image=self.photo2, anchor='nw')

        self.root.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = Camera(root)
    root.mainloop()
