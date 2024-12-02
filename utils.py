# utils.py

import re
from datetime import datetime

def validiraj_email(email):
    # Jednostavna validacija e-maila
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email) is not None

def validiraj_telefon(telefon):
    # Dozvoljava brojeve, razmake, zagrade i znak +
    regex = r'^[\d\s\+\-\(\)]+$'
    return re.fullmatch(regex, telefon) is not None

def validiraj_datum(dat):
    try:
        datetime.strptime(dat, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def validiraj_web(web):
    regex = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?' \
            r'[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}' \
            r'(:[0-9]{1,5})?(\/.*)?$'
    return re.fullmatch(regex, web) is not None
