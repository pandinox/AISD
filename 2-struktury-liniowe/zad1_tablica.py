# =============================================================================
# Zadanie 1 – Tablica (Array) o stałym rozmiarze
# =============================================================================
# OPIS PROBLEMU:
#   Pracujesz jako meteorolog i chcesz zapisać temperatury (w °C) zmierzone
#   przez 7 kolejnych dni tygodnia. Ponieważ liczba dni jest znana z góry i
#   stała, przechowujesz dane w "tablicy" o stałej długości (lista z 7 None).
#
#   Twoim zadaniem jest:
#     1. Wpisanie temperatur do tablicy przez indeksowanie (nie używaj append!).
#     2. Obliczenie średniej temperatury w tygodniu.
#     3. Znalezienie numeru dnia (1–7) z najwyższą temperaturą.
#
# METODY / OPERACJE do poznania:
#   - Tworzenie listy o stałym rozmiarze: [None] * N
#   - Dostęp i zapis przez indeks:        tablica[i] = wartość
#   - Iteracja po elementach:             for t in tablica
#   - Długość tablicy:                    len(tablica)
#   - Wyszukiwanie maksimum:              max(tablica)  /  tablica.index(...)
# =============================================================================

LICZBA_DNI = 7
DNI_TYGODNIA = ["Poniedziałek", "Wtorek", "Środa", "Czwartek",
                "Piątek", "Sobota", "Niedziela"]

# --- Inicjalizacja tablicy o stałym rozmiarze -------------------------------
# Tablica jest już gotowa – nie zmieniaj jej rozmiaru!
temperatury: list = [None] * LICZBA_DNI


# ============================================================
# FUNKCJA 1 – Wpisz temperatury do tablicy
# ============================================================
def wpisz_temperatury() -> None:
    """
    Wpisuje przykładowe temperatury do tablicy `temperatury`
    za pomocą indeksowania (tablica[i] = wartość).
    """
    przykladowe_temp = [12.5, 14.0, 9.8, 11.3, 16.7, 20.1, 18.4]

    # TODO: Korzystając z pętli for i zakresu range(LICZBA_DNI),
    #       przypisz kolejne wartości z listy `przykladowe_temp`
    #       do tablicy `temperatury` przez indeksowanie.
    #       Pamiętaj: tablica[i] = przykladowe_temp[i]
    for i in range(len(przykladowe_temp)):
        temperatury[i] = przykladowe_temp[i]


# ============================================================
# FUNKCJA 2 – Oblicz średnią temperaturę
# ============================================================
def oblicz_srednia() -> float:
    """
    Oblicza i zwraca średnią arytmetyczną temperatur z tygodnia.
    """
    # TODO: Zsumuj wszystkie elementy tablicy `temperatury`
    #       (możesz użyć sum() lub pętli), a następnie podziel
    #       przez liczbę dni (len(temperatury)).
    #       Zwróć wynik jako float (round(..., 2)).
    srednia = sum(temperatury)/len(temperatury)
    return round(srednia, 2)


# ============================================================
# FUNKCJA 3 – Znajdź najcieplejszy dzień
# ============================================================
def najcieplejszy_dzien() -> tuple[str, float]:
    """
    Zwraca krotkę (nazwa_dnia, temperatura) dla dnia
    z najwyższą temperaturą w tygodniu.
    """
    # TODO: 1. Znajdź maksymalną wartość w tablicy `temperatury` (użyj max()).
    #       2. Znajdź jej indeks (użyj .index(...)).
    #       3. Zwróć krotkę: (DNI_TYGODNIA[indeks], maks_temp)
    idx = temperatury.index(max(temperatury))

    return (DNI_TYGODNIA[idx], temperatury[idx])


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    wpisz_temperatury()

    print("=== Temperatury w tygodniu ===")
    for i in range(LICZBA_DNI):
        print(f"  {DNI_TYGODNIA[i]:<14}: {temperatury[i]} °C")

    srednia = oblicz_srednia()
    print(f"\nŚrednia temperatura: {srednia} °C")

    dzien, temp = najcieplejszy_dzien()
    print(f"Najcieplejszy dzień: {dzien} ({temp} °C)")