# gui.py

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from data_manager import DataManager
from utils import validiraj_email, validiraj_telefon, validiraj_datum, validiraj_web
from menu import MenuBar  # Importanje klase MenuBar iz menu.py

class TelefonskiImenikGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Telefonski imenik")

        self.data_manager = DataManager()
        self.odabrani_kontakt = None

        self.create_menu()      # Kreiranje menija
        self.create_widgets()
        self.prikazi_kontakte()

    def create_menu(self):
        self.menu_bar = MenuBar(self.root, self)
        self.root.config(menu=self.menu_bar)

    def create_widgets(self):
        # Okvir za unos podataka
        frame_unos = tk.LabelFrame(self.root, text="Unos / Ažuriranje kontakta")
        frame_unos.pack(fill="x", padx=10, pady=5)

        # Prva kolona
        tk.Label(frame_unos, text="Ime:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.entry_ime = tk.Entry(frame_unos)
        self.entry_ime.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_unos, text="E-mail:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.entry_email = tk.Entry(frame_unos)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_unos, text="Adresa stanovanja:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.entry_adresa = tk.Entry(frame_unos)
        self.entry_adresa.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_unos, text="Broj telefona:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.entry_telefon = tk.Entry(frame_unos)
        self.entry_telefon.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_unos, text="Grupa:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.entry_grupa = tk.Entry(frame_unos)
        self.entry_grupa.grid(row=4, column=1, padx=5, pady=5)

        # Druga kolona
        tk.Label(frame_unos, text="Datum rođenja:").grid(row=0, column=2, padx=5, pady=5, sticky='e')
        self.entry_datum = tk.Entry(frame_unos)
        self.entry_datum.grid(row=0, column=3, padx=5, pady=5)
        tk.Label(frame_unos, text="(DD.MM.GGGG)").grid(row=0, column=4, padx=5, pady=5, sticky='w')

        tk.Label(frame_unos, text="Tvrtka:").grid(row=1, column=2, padx=5, pady=5, sticky='e')
        self.entry_tvrtka = tk.Entry(frame_unos)
        self.entry_tvrtka.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame_unos, text="Napomene:").grid(row=2, column=2, padx=5, pady=5, sticky='e')
        self.entry_napomene = tk.Entry(frame_unos)
        self.entry_napomene.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(frame_unos, text="Web stranica:").grid(row=3, column=2, padx=5, pady=5, sticky='e')
        self.entry_web = tk.Entry(frame_unos)
        self.entry_web.grid(row=3, column=3, padx=5, pady=5)

        tk.Label(frame_unos, text="Socijalni mediji:").grid(row=4, column=2, padx=5, pady=5, sticky='e')
        self.entry_socijalni_mediji = tk.Entry(frame_unos)
        self.entry_socijalni_mediji.grid(row=4, column=3, padx=5, pady=5)

        # Gumbi za spremanje i ažuriranje
        frame_gumbi = tk.Frame(frame_unos)
        frame_gumbi.grid(row=5, column=0, columnspan=5, pady=10)

        self.button_spremi = tk.Button(frame_gumbi, text="Spremi", command=self.spremi_podatke)
        self.button_spremi.pack(side="left", padx=5)

        self.button_azuriraj = tk.Button(frame_gumbi, text="Ažuriraj", command=self.azuriraj_podatke, state="disabled")
        self.button_azuriraj.pack(side="left", padx=5)

        # Okvir za pretraživanje i sortiranje
        frame_pretraga = tk.LabelFrame(self.root, text="Pretraživanje i sortiranje")
        frame_pretraga.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_pretraga, text="Pretraži po imenu:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_pretraga = tk.Entry(frame_pretraga)
        self.entry_pretraga.grid(row=0, column=1, padx=5, pady=5)
        self.entry_pretraga.bind("<KeyRelease>", self.pretrazi_kontakte)

        tk.Label(frame_pretraga, text="Sortiraj po:").grid(row=0, column=2, padx=5, pady=5)
        self.sort_var = tk.StringVar()
        self.sort_var.set("Ime")
        self.combo_sort = ttk.Combobox(frame_pretraga, textvariable=self.sort_var, values=["Ime", "Prezime"])
        self.combo_sort.grid(row=0, column=3, padx=5, pady=5)
        self.combo_sort.bind("<<ComboboxSelected>>", self.sortiraj_kontakte)

        tk.Label(frame_pretraga, text="Filtriraj po grupi:").grid(row=0, column=4, padx=5, pady=5)
        self.grupa_var = tk.StringVar()
        self.combo_grupa = ttk.Combobox(frame_pretraga, textvariable=self.grupa_var)
        self.combo_grupa.grid(row=0, column=5, padx=5, pady=5)
        self.combo_grupa.bind("<<ComboboxSelected>>", self.filtriraj_po_grupi)
        self.azuriraj_combo_grupa()

        # Okvir za prikaz kontakata
        frame_prikaz = tk.Frame(self.root)
        frame_prikaz.pack(fill="both", expand=True, padx=10, pady=5)

        columns = [
            "Ime", "Email", "Adresa", "Telefon", "Grupa",
            "Datum rođenja", "Tvrtka", "Napomene", "Web stranica", "Socijalni mediji"
        ]
        self.tree = ttk.Treeview(frame_prikaz, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=100, width=120)

        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<Double-1>", self.odaberi_kontakt)

        scrollbar = ttk.Scrollbar(frame_prikaz, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Gumbi za dodatne funkcije
        frame_dodatno = tk.Frame(self.root)
        frame_dodatno.pack(pady=5)

        self.button_obrisi = tk.Button(frame_dodatno, text="Obriši odabrani kontakt", command=self.obrisi_kontakt)
        self.button_obrisi.pack(side="left", padx=5)

        # Ove gumbi su sada dostupni kroz meni, ali ih možete ostaviti ako želite
        # self.button_izvoz = tk.Button(frame_dodatno, text="Izvoz kontakata", command=self.izvoz_kontakata)
        # self.button_izvoz.pack(side="left", padx=5)

        # self.button_uvoz = tk.Button(frame_dodatno, text="Uvoz kontakata", command=self.uvoz_kontakata)
        # self.button_uvoz.pack(side="left", padx=5)

    def spremi_podatke(self):
        ime = self.entry_ime.get()
        email = self.entry_email.get()
        adresa = self.entry_adresa.get()
        telefon = self.entry_telefon.get()
        grupa = self.entry_grupa.get()
        datum = self.entry_datum.get()
        tvrtka = self.entry_tvrtka.get()
        napomene = self.entry_napomene.get()
        web = self.entry_web.get()
        socijalni_mediji = self.entry_socijalni_mediji.get()

        if not (ime and email and adresa and telefon):
            messagebox.showwarning("Upozorenje", "Molimo popunite polja: Ime, E-mail, Adresa, Telefon.")
            return

        novi_kontakt = {
            'Ime': ime, 'Email': email, 'Adresa': adresa, 'Telefon': telefon, 'Grupa': grupa,
            'Datum rođenja': datum, 'Tvrtka': tvrtka, 'Napomene': napomene,
            'Web stranica': web, 'Socijalni mediji': socijalni_mediji
        }

        try:
            self.data_manager.dodaj_kontakt(novi_kontakt)
            self.azuriraj_combo_grupa()
            self.prikazi_kontakte()
            self.ocisti_polja()
            messagebox.showinfo("Uspjeh", "Kontakt je uspješno spremljen.")
        except ValueError as e:
            messagebox.showwarning("Upozorenje", str(e))

    def azuriraj_podatke(self):
        if not self.odabrani_kontakt:
            return

        ime = self.entry_ime.get()
        email = self.entry_email.get()
        adresa = self.entry_adresa.get()
        telefon = self.entry_telefon.get()
        grupa = self.entry_grupa.get()
        datum = self.entry_datum.get()
        tvrtka = self.entry_tvrtka.get()
        napomene = self.entry_napomene.get()
        web = self.entry_web.get()
        socijalni_mediji = self.entry_socijalni_mediji.get()

        if not (ime and email and adresa and telefon):
            messagebox.showwarning("Upozorenje", "Molimo popunite polja: Ime, E-mail, Adresa, Telefon.")
            return

        novi_kontakt = {
            'Ime': ime, 'Email': email, 'Adresa': adresa, 'Telefon': telefon, 'Grupa': grupa,
            'Datum rođenja': datum, 'Tvrtka': tvrtka, 'Napomene': napomene,
            'Web stranica': web, 'Socijalni mediji': socijalni_mediji
        }

        try:
            self.data_manager.azuriraj_kontakt(self.odabrani_kontakt, novi_kontakt)
            self.azuriraj_combo_grupa()
            self.prikazi_kontakte()
            self.ocisti_polja()
            self.button_spremi.config(state="normal")
            self.button_azuriraj.config(state="disabled")
            messagebox.showinfo("Uspjeh", "Kontakt je uspješno ažuriran.")
        except ValueError as e:
            messagebox.showwarning("Upozorenje", str(e))

    def obrisi_kontakt(self):
        odabrani = self.tree.selection()
        if not odabrani:
            messagebox.showwarning("Upozorenje", "Niste odabrali kontakt za brisanje.")
            return

        odgovor = messagebox.askyesno("Potvrda", "Jeste li sigurni da želite obrisati odabrani kontakt?")
        if odgovor:
            item = self.tree.item(odabrani)
            kontakt_ime = item['values'][0]
            kontakt = next((k for k in self.data_manager.kontakti if k['Ime'] == kontakt_ime), None)
            if kontakt:
                self.data_manager.obrisi_kontakt(kontakt)
                self.prikazi_kontakte()
                messagebox.showinfo("Uspjeh", "Kontakt je obrisan.")

    def odaberi_kontakt(self, event):
        odabrani = self.tree.selection()
        if not odabrani:
            return

        item = self.tree.item(odabrani)
        kontakt_podaci = item['values']

        # Očistiti polja
        self.entry_ime.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_adresa.delete(0, tk.END)
        self.entry_telefon.delete(0, tk.END)
        self.entry_grupa.delete(0, tk.END)
        self.entry_datum.delete(0, tk.END)
        self.entry_tvrtka.delete(0, tk.END)
        self.entry_napomene.delete(0, tk.END)
        self.entry_web.delete(0, tk.END)
        self.entry_socijalni_mediji.delete(0, tk.END)

        # Popuniti polja
        keys = [
            'Ime', 'Email', 'Adresa', 'Telefon', 'Grupa',
            'Datum rođenja', 'Tvrtka', 'Napomene', 'Web stranica', 'Socijalni mediji'
        ]
        for entry, value in zip(
            [
                self.entry_ime, self.entry_email, self.entry_adresa, self.entry_telefon,
                self.entry_grupa, self.entry_datum, self.entry_tvrtka,
                self.entry_napomene, self.entry_web, self.entry_socijalni_mediji
            ],
            kontakt_podaci
        ):
            entry.insert(0, value)

        self.odabrani_kontakt = dict(zip(keys, kontakt_podaci))
        self.button_spremi.config(state="disabled")
        self.button_azuriraj.config(state="normal")

    def pretrazi_kontakte(self, event):
        trazeni_tekst = self.entry_pretraga.get().lower()
        filtrirani_kontakti = [k for k in self.data_manager.kontakti if trazeni_tekst in k['Ime'].lower()]
        self.prikazi_kontakte(filtrirani_kontakti)

    def filtriraj_po_grupi(self, event):
        odabrana_grupa = self.grupa_var.get()
        if odabrana_grupa == "":
            self.prikazi_kontakte()
        else:
            filtrirani_kontakti = [k for k in self.data_manager.kontakti if k['Grupa'] == odabrana_grupa]
            self.prikazi_kontakte(filtrirani_kontakti)

    def sortiraj_kontakte(self, event):
        kriterij = self.sort_var.get()
        if kriterij == "Ime":
            self.data_manager.kontakti.sort(key=lambda x: x['Ime'])
        elif kriterij == "Prezime":
            self.data_manager.kontakti.sort(key=lambda x: x['Ime'].split()[-1])
        self.prikazi_kontakte()

    def prikazi_kontakte(self, kontakti=None):
        if kontakti is None:
            kontakti = self.data_manager.kontakti

        # Čisti prikaz
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Popunjava prikaz
        for kontakt in kontakti:
            values = [
                kontakt.get('Ime', ''), kontakt.get('Email', ''), kontakt.get('Adresa', ''),
                kontakt.get('Telefon', ''), kontakt.get('Grupa', ''),
                kontakt.get('Datum rođenja', ''), kontakt.get('Tvrtka', ''), kontakt.get('Napomene', ''),
                kontakt.get('Web stranica', ''), kontakt.get('Socijalni mediji', '')
            ]
            self.tree.insert("", "end", values=values)

    def ocisti_polja(self):
        self.entry_ime.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_adresa.delete(0, tk.END)
        self.entry_telefon.delete(0, tk.END)
        self.entry_grupa.delete(0, tk.END)
        self.entry_datum.delete(0, tk.END)
        self.entry_tvrtka.delete(0, tk.END)
        self.entry_napomene.delete(0, tk.END)
        self.entry_web.delete(0, tk.END)
        self.entry_socijalni_mediji.delete(0, tk.END)
        self.button_spremi.config(state="normal")
        self.button_azuriraj.config(state="disabled")
        self.odabrani_kontakt = None

    def azuriraj_combo_grupa(self):
        grupe = list(self.data_manager.grupe)
        grupe.insert(0, "")
        self.combo_grupa['values'] = grupe

    def izvoz_kontakata(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV datoteka", "*.csv")])
        if not filepath:
            return

        try:
            self.data_manager.izvoz_kontakata(filepath)
            messagebox.showinfo("Uspjeh", "Kontakti su uspješno izvezeni.")
        except Exception as e:
            messagebox.showerror("Greška", f"Došlo je do greške prilikom izvoza: {e}")

    def uvoz_kontakata(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV datoteka", "*.csv")])
        if not filepath:
            return

        try:
            self.data_manager.uvoz_kontakata(filepath)
            self.azuriraj_combo_grupa()
            self.prikazi_kontakte()
            messagebox.showinfo("Uspjeh", "Kontakti su uspješno uvezeni.")
        except Exception as e:
            messagebox.showerror("Greška", f"Došlo je do greške prilikom uvoza: {e}")
