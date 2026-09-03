import tkinter as tk

root = tk.Tk()
root.title("Super title")
root.geometry("600x400")


def pokaz_profil():
    imie = entry_imie.get()
    klasa = entry_klasa.get()
    jezyk = entry_jezyk.get()
    gotowy = gotowy_var.get()

    if imie == "":
        profil.config(text="Wpisz swoje imię...")
    else:
        profil.config(
            text=f"Imię: {imie}\n"
                 f"Klasa: {klasa}\n"
                 f"Ulubiony język programowania: {jezyk}\n"
                 f"Znaki w twoim imieniu: {len(imie)}\n"
                 f"Jestem gotowy do testu: {'Tak' if gotowy else 'Nie'}"
        )


tk.Label(
    root,
    text="Imię:",
    font=("Arial", 16),
    fg="white"
).pack()

entry_imie = tk.Entry(root, bg="white", fg="black")
entry_imie.pack()

tk.Label(
    root,
    text="Klasa:",
    font=("Arial", 16),
    fg="white"
).pack()

entry_klasa = tk.Entry(root, bg="white", fg="black")
entry_klasa.pack()

tk.Label(
    root,
    text="Ulubiony język programowania:",
    font=("Arial", 16),
    fg="white"
).pack()

entry_jezyk = tk.Entry(root, bg="white", fg="black")
entry_jezyk.pack()

gotowy_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Jestem gotowy do testu",
    variable=gotowy_var
).pack()

tk.Button(
    root,
    text="Pokaż profil",
    command=pokaz_profil,
    width= 20
).pack(pady=20)

profil = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    fg="white"
)
profil.pack()

root.mainloop()