import tkinter as tk

root = tk.Tk()
root.title("Super title")
root.geometry("600x500")


def pokaz_profil():
    imie = entry_imie.get()
    klasa = entry_klasa.get()
    jezyk = entry_jezyk.get()
    gotowy = gotowy_var.get()

    if imie == "" or jezyk == "" or klasa == "" or not gotowy:
        profil.config(text="Wypełnij wszystkie pola") # wczesniej tylko sprawdzanie imienia i komunikat o tym
    else:
        profil.config(
            text=f"Imię: {imie}\n"
                 f"Klasa: {klasa}\n"
                 f"Ulubiony język programowania: {jezyk}\n"
                 f"Znaki w twoim imieniu: {len(imie)}\n"
                 f"Jestem gotowy do testu: {'Tak' if gotowy else 'Nie'}"
        )


def wyczysc():
    entry_imie.delete(0, tk.END)
    entry_klasa.delete(0, tk.END)
    entry_jezyk.delete(0, tk.END)
    gotowy_var.set(False)
    profil.config(text="")


tk.Label(
    root,
    text="Imię:",
    font=("Arial", 16),
    fg="white"
).pack(pady=5)

entry_imie = tk.Entry(
    root,
    bg="white",
    fg="black",
    width=30
)
entry_imie.pack(pady=5)


tk.Label(
    root,
    text="Klasa:",
    font=("Arial", 16),
    fg="white"
).pack(pady=5)

entry_klasa = tk.Entry(
    root,
    bg="white",
    fg="black",
    width=30
)
entry_klasa.pack(pady=5)


tk.Label(
    root,
    text="Ulubiony język programowania:",
    font=("Arial", 16),
    fg="white"
).pack(pady=5)

entry_jezyk = tk.Entry(
    root,
    bg="white",
    fg="black",
    width=30
)
entry_jezyk.pack(pady=5)


gotowy_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Jestem gotowy do testu",
    variable=gotowy_var
).pack(pady=5)


tk.Button(
    root,
    text="Pokaż profil",
    command=pokaz_profil,
    width=20
).pack(pady=5)


tk.Button(
    root,
    text="Wyczyść pola",
    command=wyczysc,
    width=20
).pack(pady=5)


profil = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    fg="white"
)
profil.pack(pady=5)


root.mainloop()