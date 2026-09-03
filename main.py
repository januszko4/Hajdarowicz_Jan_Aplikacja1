import tkinter as tk

root = tk.Tk()
root.title("Super title")
root.geometry("600x400")

lbl = tk.Label(
    root,
    text="Moja pierwsza aplikacja",
    fg="white",
    font=("Arial", 32)
).pack(pady=25)
lbl2 = tk.Label(
    root,
    text="Programowanie aplikacji desktopowych",
    fg="cyan",
    font=("Arial", 16)
).pack(pady=25)



licznik = 0

def click():
    global licznik
    licznik += 1
    lbl_counter.config(text=licznik)

def reset():
    global licznik
    licznik = 0
    lbl_counter.config(text=licznik)

btn1 = tk.Button(
    root,
    text="Kliknij mnie",
    width=25,
    command=click
).pack()
lbl_counter = tk.Label(
    root,
    text=licznik,
    fg="white"
)
lbl_reset_btn = tk.Button(
    root,
    text="Wyzeruj licznik",
    command=reset
).pack()

lbl_counter.pack(pady=25)

root.mainloop()