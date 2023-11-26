from tkinter import *

# Inisialisasi data buku
list_buku = []

# Function untuk menambahkan buku
def tambah_buku():
    judul = entry_judul.get()
    pengarang = entry_pengarang.get()
    status = entry_status.get()

    if judul and pengarang and status:
        buku = {
            "Judul": judul,
            "Pengarang": pengarang,
            "Status": status
        }

        list_buku.append(buku)
        update_output()
        message.config(text="Buku berhasil ditambahkan.", fg="green")
    else:
        message.config(text="Mohon isi semua kolom.", fg="red")

# Function untuk mengupdate output
def update_output():
    output.delete(1.0, END)
    for buku in list_buku:
        output.insert(END, f"Judul: {buku['Judul']}\n")
        output.insert(END, f"Pengarang: {buku['Pengarang']}\n")
        output.insert(END, f"Status: {buku['Status']}\n")
        output.insert(END, "\n")

# GUI window
window = Tk()
window.title("Simple Book Tracker")

# Labels
label_judul = Label(window, text="Judul Buku:")
label_pengarang = Label(window, text="Pengarang:")
label_status = Label(window, text="Status Baca:")

# Entry widgets
entry_judul = Entry(window)
entry_pengarang = Entry(window)
entry_status = Entry(window)

# Button untuk menambahkan buku
button_tambah = Button(window, text="Tambah Buku", command=tambah_buku)

# Output Text widget
output = Text(window, height=10, width=40)

# Message widget untuk menampilkan pesan
message = Message(window, text="", width=200)

# Menempatkan elemen-elemen dalam grid
label_judul.grid(row=0, column=0)
entry_judul.grid(row=0, column=1)
label_pengarang.grid(row=1, column=0)
entry_pengarang.grid(row=1, column=1)
label_status.grid(row=2, column=0)
entry_status.grid(row=2, column=1)
button_tambah.grid(row=3, column=0, columnspan=2)
output.grid(row=4, column=0, columnspan=2)
message.grid(row=5, column=0, columnspan=2)

# Menjalankan GUI loop
window.mainloop()
