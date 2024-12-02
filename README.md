Telefonski imenik
Verzija: 1.0
Autor: Vaše ime

Opis
Telefonski imenik je desktop aplikacija razvijena u Pythonu koja omogućuje upravljanje kontaktima na jednostavan i intuitivan način. Program omogućuje dodavanje, ažuriranje, brisanje i pretraživanje kontakata te podržava napredne značajke poput grupiranja kontakata, podsjetnika za rođendane i napredne pretrage.

Značajke
Dodavanje i ažuriranje kontakata: Unesite osnovne informacije o kontaktu, uključujući ime, e-mail, adresu, broj telefona i dodatne informacije poput datuma rođenja, tvrtke i socijalnih medija.
Validacija unosa: Program provjerava ispravnost unosa e-mail adrese, broja telefona, datuma rođenja i web stranice.
Grupiranje kontakata: Organizirajte kontakte u grupe (npr. Obitelj, Prijatelji, Posao) i filtrirajte ih po grupi.
Napredna pretraga: Pretražujte kontakte po različitim kriterijima kao što su ime, e-mail, telefon, tvrtka ili grupa.
Podsjetnici za rođendane: Program vas obavještava o nadolazećim rođendanima kontakata.
Sortiranje kontakata: Sortirajte kontakte po imenu ili prezimenu.
Izvoz i uvoz kontakata: Izvezite kontakte u CSV datoteku ili uvezite kontakte iz postojeće CSV datoteke.
Grafičko sučelje: Intuitivno i pregledno grafičko sučelje izrađeno pomoću Tkinter biblioteke.
Zahtjevi
Python 3.x: Program je razvijen u Pythonu 3 i nije kompatibilan s Pythonom 2.
Tkinter: Biblioteka za grafičko sučelje koja dolazi uz standardnu Python instalaciju.
Napomena za Linux korisnike: Možda ćete trebati instalirati tkinter ručno:
Ubuntu/Debian:
sudo apt-get install python3-tk
Fedora:
sudo dnf install python3-tkinter
Arch Linux:
sudo pacman -S tk
Standardne Python biblioteke: csv, os, re, datetime, tkinter.
Instalacija
Preuzmite ili klonirajte repozitorij u željeni direktorij:

git clone https://github.com/vaš-korisnički-račun/telefonski-imenik.git
Ili jednostavno preuzmite ZIP datoteku i raspakirajte je.

Navigirajte do direktorija programa:

cd telefonski-imenik
Provjerite imate li instaliran Python 3:

python3 --version
Ako nemate Python 3, preuzmite ga i instalirajte s službene stranice.

Provjerite imate li instaliran tkinter (posebno ako koristite Linux).

Pokretanje programa
Pokrenite program pomoću sljedeće naredbe:

python3 main.py
Ako koristite Windows, možda ćete trebati koristiti:

python main.py
Upute za korištenje
Glavni prozor
Nakon pokretanja programa, otvorit će se glavni prozor aplikacije koji je podijeljen na nekoliko dijelova:

Unos / Ažuriranje kontakta: Ovdje možete unijeti podatke novog kontakta ili ažurirati postojeći.
Pretraživanje i sortiranje: Omogućuje pretraživanje kontakata i sortiranje prema određenim kriterijima.
Prikaz kontakata: Lista svih kontakata u imeniku.
Izbornik: Dostupan na vrhu prozora s opcijama Datoteka, Uredi i Pomoć.
Dodavanje novog kontakta
Unesite potrebne podatke u polja za unos. Obavezna polja su:

Ime
E-mail
Adresa
Broj telefona
Opcionalno možete unijeti dodatne informacije:

Grupa
Datum rođenja (format: DD.MM.GGGG)
Tvrtka
Napomene
Web stranica
Socijalni mediji
Kliknite na gumb "Spremi" kako biste dodali kontakt u imenik.

Ažuriranje postojećeg kontakta
Dvostruko kliknite na kontakt u listi kako biste ga odabrali za ažuriranje. Podaci će se prikazati u poljima za unos.
Izmijenite željene podatke.
Kliknite na gumb "Ažuriraj" kako biste spremili promjene.
Brisanje kontakta
Odaberite kontakt u listi i kliknite na gumb "Obriši odabrani kontakt" ili koristite opciju u izborniku Uredi > Obriši odabrani kontakt.
Pretraživanje kontakata
U polje "Pretraži" unesite tekst za pretragu.
U padajućem izborniku "Po:" odaberite kriterij pretrage (Ime, Email, Telefon, Tvrtka, Grupa).
Program će automatski filtrirati kontakte na temelju unosa.
Sortiranje kontakata
U okviru "Sortiraj po:" odaberite kriterij sortiranja (Ime ili Prezime). Kontakti će se automatski sortirati.
Filtriranje po grupi
U padajućem izborniku "Filtriraj po grupi:" odaberite željenu grupu kako biste prikazali samo kontakte iz te grupe.
Izvoz i uvoz kontakata
Izvoz kontakata:
Kroz izbornik Datoteka > Izvoz kontakata.
Odaberite lokaciju i ime CSV datoteke u koju želite spremiti kontakte.
Uvoz kontakata:
Kroz izbornik Datoteka > Uvoz kontakata.
Odaberite CSV datoteku iz koje želite uvesti kontakte.
Podsjetnici za rođendane
Prilikom pokretanja programa, ako postoje kontakti čiji je rođendan danas ili u narednih 7 dana, pojavit će se obavijest s popisom tih kontakata.
Struktura projekta
TelefonskiImenik/
├── constants.py        # Definicija konstanti kao što su FILENAME i FIELDNAMES
├── data_manager.py     # Klasa za rukovanje podacima (učitavanje, spremanje, validacija)
├── gui.py              # Grafičko sučelje aplikacije
├── main.py             # Glavna skripta za pokretanje aplikacije
├── menu.py             # Definicija izbornika aplikacije
├── utils.py            # Pomoćne funkcije za validaciju unosa
└── imenik.csv          # CSV datoteka koja sadrži kontakte (generira se automatski)
Dodatne informacije
Validacija unosa: Program provjerava ispravnost e-mail adresa, brojeva telefona, datuma rođenja i web stranica.
Format datuma rođenja: Datum rođenja mora biti unesen u formatu DD.MM.GGGG.
Kodiranje znakova: Program koristi UTF-8 kodiranje za ispravan prikaz znakova s dijakritičkim znacima.
Mogući problemi
Tkinter nije instaliran: Ako dobijete grešku vezanu uz tkinter, provjerite je li instaliran na vašem sustavu.
Problemi s prikazom znakova: Ako se posebni znakovi ne prikazuju ispravno, provjerite je li vaša Python okolina postavljena na UTF-8 kodiranje.
Nedostatak dozvola: Osigurajte da imate dozvole za čitanje i pisanje u direktoriju gdje se nalazi program.
Planirana proširenja
Favoriti: Dodavanje mogućnosti označavanja kontakata kao favorita.
Sigurnosno kopiranje: Implementacija funkcije za sigurnosno kopiranje podataka.
Enkripcija podataka: Zaštita podataka enkripcijom prilikom spremanja.
Autentifikacija korisnika: Dodavanje sustava za prijavu korisnika radi zaštite podataka.
Kontakt
Ako imate pitanja, prijedloge ili trebate pomoć, slobodno me kontaktirajte na:

E-mail: vaša.email.adresa@example.com
GitHub: vaš-korisnički-račun
Licenca
Ovaj projekt je objavljen pod MIT licencom.
