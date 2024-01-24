import time

def digitalis_ora():
    while True:
        # Az aktuális idő lekérése
        jelenlegi_ido = time.localtime()
        ora = jelenlegi_ido.tm_hour
        perc = jelenlegi_ido.tm_min
        masodperc = jelenlegi_ido.tm_sec

        # Idő formázása és megjelenítése
        ido_str = f"{ora:02d}:{perc:02d}:{masodperc:02d}"
        print(ido_str, end='\r')  # '\r' karakter: visszaugrás a sor elejére

        # Várakozás egy másodpercig
        time.sleep(1)

try:
    digitalis_ora()
except KeyboardInterrupt:
    print("\nKilépés a digitális órából.")