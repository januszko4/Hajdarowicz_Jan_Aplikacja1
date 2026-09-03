import tkinter as tk


root = tk.Tk()
root.title("Kalkulator")
root.geometry("400x350")


def pobierz_liczby():
    try:
        liczba1 = float(entry_liczba1.get())
        liczba2 = float(entry_liczba2.get())
        return liczba1, liczba2
    except ValueError:
        lbl_wynik.config(text="Wpisz poprawne liczby.")
        return None


def dodaj():
    liczby = pobierz_liczby()

    if liczby is not None:
        liczba1, liczba2 = liczby
        lbl_wynik.config(text=f"Wynik: {liczba1 + liczba2}")


def odejmij():
    liczby = pobierz_liczby()

    if liczby is not None:
        liczba1, liczba2 = liczby
        lbl_wynik.config(text=f"Wynik: {liczba1 - liczba2}")


def pomnoz():
    liczby = pobierz_liczby()

    if liczby is not None:
        liczba1, liczba2 = liczby
        lbl_wynik.config(text=f"Wynik: {liczba1 * liczba2}")


def podziel():
    liczby = pobierz_liczby()

    if liczby is not None:
        liczba1, liczba2 = liczby

        if liczba2 == 0:
            lbl_wynik.config(text="Nie można dzielić przez zero.")
        else:
            lbl_wynik.config(text=f"Wynik: {liczba1 / liczba2}")


def reset():
    entry_liczba1.delete(0, tk.END)
    entry_liczba2.delete(0, tk.END)
    lbl_wynik.config(text="Wynik")


tk.Label(
    root,
    text="Kalkulator",
    font=("Arial", 24)
).pack(pady=15)


tk.Label(
    root,
    text="Liczba 1"
).pack()

entry_liczba1 = tk.Entry(root)
entry_liczba1.pack(pady=5)


tk.Label(
    root,
    text="Liczba 2"
).pack()

entry_liczba2 = tk.Entry(root)
entry_liczba2.pack(pady=5)


frame = tk.Frame(root)
frame.pack(pady=15)

tk.Button(
    frame,
    text="+",
    width=5,
    command=dodaj
).pack(side="left", padx=5)

tk.Button(
    frame,
    text="-",
    width=5,
    command=odejmij
).pack(side="left", padx=5)

tk.Button(
    frame,
    text="*",
    width=5,
    command=pomnoz
).pack(side="left", padx=5)

tk.Button(
    frame,
    text="/",
    width=5,
    command=podziel
).pack(side="left", padx=5)


lbl_wynik = tk.Label(
    root,
    text="Wynik",
    font=("Arial", 16)
)
lbl_wynik.pack(pady=10)


tk.Button(
    root,
    text="Reset",
    command=reset
).pack()


tk.Button(
    root,
    text="Zamknij program",
    command=root.destroy
).pack(pady=5)


root.mainloop()