import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Video Player")
root.state('zoomed')

# Inisialisasi OpenCV untuk memutar video
cap = cv2.VideoCapture(0)

# Variabel status untuk memantau apakah video sudah diatur ulang ke posisi semula
video_centered = False
original_position = (0, 0)

# Fungsi untuk memainkan video
def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (300, 300))
        
        # Ubah ukuran frame video menjadi 1080x600 saat tombol "Center Video" ditekan
        if video_centered:
            frame = cv2.resize(frame, (1080, 600),interpolation=cv2.INTER_CUBIC)
        
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        label.config(image=frame)
        label.image = frame
        label.after(10, play_video)  # Rekursif untuk terus memainkan video

# Fungsi untuk memindahkan video ke tengah atau posisi semula
def toggle_center_video():
    global video_centered, original_position
    if video_centered:
        # Jika video sudah diatur ulang ke posisi semula, kembalikan ke posisi semula
        label.place(x=original_position[0], y=original_position[1])
        video_centered = False
    else:
        # Jika video belum diatur ulang, atur ulang ke posisi semula dan ubah ukuran
        original_position = (label.winfo_x(), label.winfo_y())
        label.place(x=0, y=0)
        video_centered = True

# Tombol untuk memindahkan video ke tengah atau posisi semula
center_button = ttk.Button(root, text="Center Video", command=toggle_center_video)
center_button.place(x=1200, y=100)

# Label untuk menampilkan frame video
label = ttk.Label(root)
label.place(x=100, y=300)

play_video()

root.mainloop()
