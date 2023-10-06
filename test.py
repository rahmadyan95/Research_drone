import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Fungsi untuk mengambil frame video pertama
def update_frame1():
    ret, frame = cap1.read()  # Membaca frame dari kamera atau video pertama
    if ret:
        # Mengonversi frame OpenCV ke format yang dapat ditampilkan di Tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=frame)

        # Mengganti gambar pada label pertama
        label1.config(image=photo)
        label1.image = photo

        # Memanggil kembali fungsi ini setiap 10 milisekon untuk mendapatkan frame baru
        root.after(10, update_frame1)

# Fungsi untuk mengambil frame video kedua
def update_frame2():
    ret, frame = cap2.read()  # Membaca frame dari kamera atau video kedua
    if ret:
        # Mengonversi frame OpenCV ke format yang dapat ditampilkan di Tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=frame)

        # Mengganti gambar pada label kedua
        label2.config(image=photo)
        label2.image = photo

        # Memanggil kembali fungsi ini setiap 10 milisekon untuk mendapatkan frame baru
        root.after(10, update_frame2)

# Fungsi untuk memindahkan video pertama ke atas dan memperbesar ukuran
def move_and_zoom_video1():
    global is_small1

    if is_small1:
        # Simpan ukuran jendela sebelumnya
        prev_width, prev_height = root.winfo_width(), root.winfo_height()

        # Memperbesar ukuran video pertama dengan padding
        video_label1.pack_forget()  # Hapus label video pertama yang kecil
        label1.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)  # Tambahkan label video pertama besar dengan padding
        is_small1 = False

        # Setel ulang posisi label video pertama besar ke tengah
        root.geometry(f"{prev_width}x{prev_height}")
    else:
        # Memindahkan video pertama ke atas
        label1.pack_forget()  # Hapus label video pertama besar
        video_label1.pack(fill=tk.BOTH, expand=True)  # Tambahkan label video pertama kecil di atas
        is_small1 = True

# Fungsi untuk memindahkan video kedua ke atas dan memperbesar ukuran
def move_and_zoom_video2():
    global is_small2

    if is_small2:
        # Simpan ukuran jendela sebelumnya
        prev_width, prev_height = root.winfo_width(), root.winfo_height()

        # Memperbesar ukuran video kedua dengan padding
        video_label2.pack_forget()  # Hapus label video kedua yang kecil
        label2.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)  # Tambahkan label video kedua besar dengan padding
        is_small2 = False

        # Setel ulang posisi label video kedua besar ke tengah
        root.geometry(f"{prev_width}x{prev_height}")
    else:
        # Memindahkan video kedua ke atas
        label2.pack_forget()  # Hapus label video kedua besar
        video_label2.pack(fill=tk.BOTH, expand=True)  # Tambahkan label video kedua kecil di atas
        is_small2 = True

# Membuat jendela Tkinter
root = tk.Tk()
root.title("2 Video OpenCV ke Tkinter")
root.state('zoomed')

# Membuka kamera atau file video pertama (ganti dengan nama file jika ingin memuat video pertama)
cap1 = cv2.VideoCapture(0)

# Membuka kamera atau file video kedua (ganti dengan nama file jika ingin memuat video kedua)
cap2 = cv2.VideoCapture("test.mp4")

# Membaca ukuran frame video pertama
width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Membaca ukuran frame video kedua
width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Membuat frame untuk tombol "Zoom Video" pertama
frame_buttons1 = ttk.Frame(root)
frame_buttons1.pack(side=tk.LEFT, fill=tk.BOTH)

# Membuat frame untuk tombol "Zoom Video" kedua
frame_buttons2 = ttk.Frame(root)
frame_buttons2.pack(side=tk.RIGHT, fill=tk.BOTH)

# Membuat label untuk menampilkan video pertama besar (di layar penuh)
label1 = ttk.Label(root)
label1.pack(fill=tk.BOTH, expand=True)

# Membuat label untuk menampilkan video kedua besar (di layar penuh)
label2 = ttk.Label(root)
label2.pack(fill=tk.BOTH, expand=True)

# Membuat label untuk menampilkan video pertama kecil di bawah
video_label1 = ttk.Label(root)
video_label1.pack(fill=tk.BOTH, expand=True)

# Membuat label untuk menampilkan video kedua kecil di bawah
video_label2 = ttk.Label(root)
video_label2.pack(fill=tk.BOTH, expand=True)

is_small1 = False
is_small2 = False

# Membuat tombol untuk memindahkan video pertama ke atas dan memperbesar ukuran
move_zoom_button1 = ttk.Button(frame_buttons1, text="Zoom Video 1", command=move_and_zoom_video1)
move_zoom_button1.pack()

# Membuat tombol untuk memindahkan video kedua ke atas dan memperbesar ukuran
move_zoom_button2 = ttk.Button(frame_buttons2, text="Zoom Video 2", command=move_and_zoom_video2)
move_zoom_button2.pack()

# Memanggil fungsi untuk memperbarui frame video pertama dan video kedua
update_frame1()
update_frame2()

# Memulai aplikasi
root.mainloop()

# Menutup kamera atau file video pertama saat jendela ditutup
cap1.release()

# Menutup kamera atau file video kedua saat jendela ditutup
cap2.release()

cv2.destroyAllWindows()
