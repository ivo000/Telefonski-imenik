# data_manager.py

import csv
import os
from constants import FILENAME, FIELDNAMES
from utils import validiraj_email, validiraj_telefon, validiraj_datum, validiraj_web

class DataManager:
    def __init__(self):
        self.kontakti = []
        self.grupe = set()
        self.ucitaj_podatke()

    def ucitaj_podatke(self):
        if not os.path.exists(FILENAME):
            return

        with open(FILENAME, "r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.kontakti = [row for row in reader]
            for k in self.kontakti:
                if k['Grupa']:
                    self.grupe.add(k['Grupa'])

    def spremi_u_datoteku(self):
        with open(FILENAME, "w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(self.kontakti)

    def dodaj_kontakt(self, kontakt):
        # Provjera postoji li već kontakt s istim imenom
        if any(k['Ime'] == kontakt['Ime'] for k in self.kontakti):
            raise ValueError("Kontakt s tim imenom već postoji.")

        # Validacija unosa
        if not validiraj_email(kontakt['Email']):
            raise ValueError("E-mail adresa nije ispravna.")
        if not validiraj_telefon(kontakt['Telefon']):
            raise ValueError("Broj telefona nije ispravan.")
        if kontakt['Datum rođenja'] and not validiraj_datum(kontakt['Datum rođenja']):
            raise ValueError("Datum rođenja nije ispravan (očekivani format: DD.MM.GGGG).")
        if kontakt['Web stranica'] and not validiraj_web(kontakt['Web stranica']):
            raise ValueError("Web stranica nije ispravna.")

        self.kontakti.append(kontakt)
        if kontakt['Grupa']:
            self.grupe.add(kontakt['Grupa'])
        self.spremi_u_datoteku()

    def azuriraj_kontakt(self, stari_kontakt, novi_kontakt):
        indeks = self.kontakti.index(stari_kontakt)
        # Validacija unosa
        if not validiraj_email(novi_kontakt['Email']):
            raise ValueError("E-mail adresa nije ispravna.")
        if not validiraj_telefon(novi_kontakt['Telefon']):
            raise ValueError("Broj telefona nije ispravan.")
        if novi_kontakt['Datum rođenja'] and not validiraj_datum(novi_kontakt['Datum rođenja']):
            raise ValueError("Datum rođenja nije ispravan (očekivani format: DD.MM.GGGG).")
        if novi_kontakt['Web stranica'] and not validiraj_web(novi_kontakt['Web stranica']):
            raise ValueError("Web stranica nije ispravna.")

        self.kontakti[indeks] = novi_kontakt
        if novi_kontakt['Grupa']:
            self.grupe.add(novi_kontakt['Grupa'])
        self.spremi_u_datoteku()

    # Ostale metode ostaju iste
