# menu.py

import tkinter as tk
from tkinter import filedialog, messagebox

class MenuBar(tk.Menu):
    def __init__(self, parent, gui):
        super().__init__(parent)
        self.gui = gui
        self.create_menus()

    def create_menus(self):
        # Datoteka
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="Izvoz kontakata", command=self.gui.izvoz_kontakata)
        file_menu.add_command(label="Uvoz kontakata", command=self.gui.uvoz_kontakata)
        file_menu.add_command(label="Spremi kao...", command=self.spremi_kao)
        file_menu.add_separator()
        file_menu.add_command(label="Izlaz", command=self.gui.root.quit)
        self.add_cascade(label="Datoteka", menu=file_menu)

        # Uredi
        edit_menu = tk.Menu(self, tearoff=0)
        edit_menu.add_command(label="Spremi novi kontakt", command=self.gui.spremi_podatke)
        edit_menu.add_command(label="Ažuriraj kontakt", command=self.gui.azuriraj_podatke)
        edit_menu.add_command(label="Obriši odabrani kontakt", command=self.gui.obrisi_kontakt)
        self.add_cascade(label="Uredi", menu=edit_menu)

        # Prikaz
        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_command(label="Osvježi prikaz", command=self.gui.prikazi_kontakte)
        self.add_cascade(label="Prikaz", menu=view_menu)

        # Pomoć
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="O programu", command=self.show_about)
        self.add_cascade(label="Pomoć", menu=help_menu)

    def show_about(self):
        messagebox.showinfo("O programu", "Telefonski imenik\nVerzija 1.0\nAutor: Ivan Nenadic")

    def spremi_kao(self):
        # Implementirajte funkciju za "Spremi kao..."
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV datoteka", "*.csv")])
        if not filepath:
            return
        try:
            self.gui.data_manager.izvoz_kontakata(filepath)
            messagebox.showinfo("Uspjeh", "Kontakti su uspješno spremljeni.")
        except Exception as e:
            messagebox.showerror("Greška", f"Došlo je do greške prilikom spremanja: {e}")
