import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.video_source = 0  # Ganti dengan nama video yang ingin Anda gunakan
        self.cap = cv2.VideoCapture(self.video_source)
        self.current_canvas = 'A'

        self.canvas_a = tk.Canvas(self.root, width=640, height=480)
        self.canvas_b = tk.Canvas(self.root, width=640, height=480)
        self.canvas_a.grid(row=0, column=0, padx=10, pady=10)
        self.canvas_b.grid(row=0, column=1, padx=10, pady=10)

        self.play_button = ttk.Button(self.root, text="Play", command=self.play_video)
        self.play_button.grid(row=1, column=0, padx=10, pady=10)
        self.switch_button = ttk.Button(self.root, text="Pindah", command=self.switch_canvas)
        self.switch_button.grid(row=1, column=1, padx=10, pady=10)

        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.create_main_video_frame()

        self.playing = False
        self.update()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_main_video_frame(self):
        self.frame_atas = tk.Frame(self.root, width=self.screen_width // 1.3, height=self.screen_height // 1.57, bg="white",
                              highlightbackground="black", highlightthickness=3)
        self.frame_atas.pack_propagate(False)
        self.frame_atas.pack(pady=10, padx=10, anchor=tk.NW)

        background_color = self.frame_atas.cget("bg")
        self.label_di_frame = tk.Label(self.frame_atas, text="Main Camera Video",
                                    font=("Consolas", 18), bg=background_color)
        self.label_di_frame.pack(pady=10)

    def play_video(self):
        if not self.playing:
            self.playing = True
            self.cap = cv2.VideoCapture(self.video_source)
            self.play()

    def play(self):
        if self.playing:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                if self.current_canvas == 'A':
                    self.canvas_a.create_image(0, 0, image=self.photo, anchor=tk.NW)
                else:
                    self.canvas_b.create_image(0, 0, image=self.photo, anchor=tk.NW)
                self.root.after(10, self.play)
            else:
                self.playing = False
                messagebox.showinfo("Selesai", "Video selesai diputar.")

    def switch_canvas(self):
        if self.current_canvas == 'A':
            self.canvas_a.delete("all")
            self.current_canvas = 'B'
        else:
            self.canvas_b.delete("all")
            self.current_canvas = 'A'

    def on_closing(self):
        self.playing = False
        if self.cap is not None:
            self.cap.release()
        self.root.destroy()

    def update(self):
        self.root.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
