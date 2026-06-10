# =============================================================================
# Zadanie 1 – Przeszukiwanie Wszerz (BFS) – Znajomi drugiego stopnia
# =============================================================================
# OPIS PROBLEMU:
#   W sieciach społecznościowych "znajomi drugiego stopnia" to osoby, które znam
#   przez pośrednika – są znajomymi moich znajomych, ale ja sam nie mam z nimi
#   bezpośredniej relacji (nie ma krawędzi między mną a nimi w grafie).
#
#   Twoim zadaniem jest zaimplementowanie algorytmu BFS (Breadth-First Search),
#   który dla podanej osoby startowej zwróci zbiór jej znajomych 2. stopnia.
#
#   Algorytm BFS eksploruje graf "warstwami": najpierw odwiedza wszystkich
#   bezpośrednich sąsiadów (warstwa 1 = dystans 1), a dopiero potem sąsiadów
#   tych sąsiadów (warstwa 2 = dystans 2). Dzięki temu łatwo znaleźć węzły
#   dokładnie w zadanej odległości od punktu startowego.
#
# METODY / OPERACJE do poznania:
#   - collections.deque      – kolejka dwustronna; używamy jako kolejkę FIFO
#   - kolejka.append(x)      – dodanie elementu na koniec kolejki
#   - kolejka.popleft()      – pobranie elementu z POCZĄTKU kolejki (FIFO!)
#   - set()                  – zbiór odwiedzonych węzłów (brak duplikatów)
#   - zbior.add(x)           – dodanie elementu do zbioru
# =============================================================================

from collections import deque


# =============================================================================
# DANE – sieć społecznościowa (10 osób)
# =============================================================================
# Graf nieskierowany zapisany jako słownik list sąsiedztwa.
# Relacja jest symetryczna: jeśli Alicja zna Bartosza, to Bartosz zna Alicję.

siec_spolecznosciowa: dict[str, list[str]] = {
    "Alicja":   ["Bartosz", "Celina", "Filip"],
    "Bartosz":  ["Alicja", "Damian", "Ewa"],
    "Celina":   ["Alicja", "Grażyna"],
    "Damian":   ["Bartosz", "Henryk", "Irena"],
    "Ewa":      ["Bartosz", "Filip", "Jan"],
    "Filip":    ["Alicja", "Ewa"],
    "Grażyna":  ["Celina", "Henryk"],
    "Henryk":   ["Damian", "Grażyna"],
    "Irena":    ["Damian", "Jan"],
    "Jan":      ["Ewa", "Irena"],
}

# Przykładowe oczekiwane wyniki dla osoby startowej "Alicja":
#   - Znajomi 1. stopnia (bezpośredni): Bartosz, Celina, Filip
#   - Znajomi 2. stopnia (przez pośrednika):
#       przez Bartosza → Damian, Ewa
#       przez Celinę   → Grażyna
#       przez Filipa   → Ewa (już zliczona)
#   - Wynik końcowy (bez duplikatów, bez siebie): {Damian, Ewa, Grażyna}


# =============================================================================
# FUNKCJA DO ZAIMPLEMENTOWANIA
# =============================================================================

def bfs_znajomi_drugiego_stopnia(
    graf: dict[str, list[str]],
    osoba_startowa: str
) -> set[str]:
    """
    Znajduje znajomych drugiego stopnia podanej osoby przy użyciu algorytmu BFS.

    Znajomi drugiego stopnia to osoby, które:
      - są w odległości dokładnie 2 kroków od osoby startowej,
      - NIE są bezpośrednimi znajomymi osoby startowej,
      - NIE są samą osobą startową.

    Parametry:
        graf           – słownik list sąsiedztwa reprezentujący sieć społecznościową
        osoba_startowa – imię osoby, dla której szukamy znajomych 2. stopnia

    Zwraca:
        Zbiór (set) imion znajomych drugiego stopnia.
    """

    # Słownik przechowujący odległość każdego węzła od osoby startowej.
    # Klucz = imię osoby, wartość = liczba kroków od osoby startowej.
    odleglosci: dict[str, int] = {osoba_startowa: 0}

    # Kolejka BFS – zaczynamy od osoby startowej z odległością 0.
    # Każdy element kolejki to krotka (osoba, odleglosc).
    kolejka: deque[tuple[str, int]] = deque()
    kolejka.append((osoba_startowa, 0))

    # Zbiór wynikowy – znajomi dokładnie na dystansie 2.
    znajomi_drugiego_stopnia: set[str] = set()

    # --- Główna pętla BFS ---
    while kolejka:
        # TODO: Pobierz pierwszą parę (aktualna_osoba, aktualna_odleglosc)
        #       z POCZĄTKU kolejki (użyj .popleft() – to właśnie czyni BFS
        #       przeszukiwaniem WSZERZ, a nie WGŁĄB).
        

        # TODO: Jeśli aktualna_odleglosc wynosi już 2, nie trzeba iść dalej
        #       w głąb – pomiń bieżącą iterację (użyj 'continue').
        

        # TODO: Przejdź przez każdego sąsiada bieżącej osoby
        #       (skorzystaj z graf[aktualna_osoba]).
        #       Dla każdego sąsiada:
        #         a) Sprawdź, czy sąsiad był już odwiedzony
        #            (czy znajduje się w słowniku 'odleglosci').
        #         b) Jeśli NIE był odwiedzony:
        #            - oblicz nową odległość = aktualna_odleglosc + 1
        #            - zapisz ją w słowniku 'odleglosci'
        #            - dodaj parę (sasiad, nowa_odleglosc) do kolejki
        #            - jeśli nowa odległość == 2, dodaj sąsiada
        #              do zbioru 'znajomi_drugiego_stopnia'
        
        aktualna_osoba, aktualna_odleglosc = kolejka.popleft()

        if aktualna_odleglosc == 2:
            continue

        for sasiad in graf[aktualna_osoba]:

            if sasiad not in odleglosci:

                nowa_odleglosc = aktualna_odleglosc + 1

                odleglosci[sasiad] = nowa_odleglosc

                kolejka.append((sasiad, nowa_odleglosc))

                if nowa_odleglosc == 2:
                    znajomi_drugiego_stopnia.add(sasiad)
    return znajomi_drugiego_stopnia


# =============================================================================
# PROGRAM GŁÓWNY – testy
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 1 – BFS: Znajomi drugiego stopnia")
    print("=" * 55)

    osoby_testowe = ["Alicja", "Damian", "Jan"]

    for osoba in osoby_testowe:
        wynik = bfs_znajomi_drugiego_stopnia(siec_spolecznosciowa, osoba)
        bezposredni = set(siec_spolecznosciowa[osoba])

        print(f"\nOsoba startowa : {osoba}")
        print(f"Znajomi 1. st. : {sorted(bezposredni)}")
        print(f"Znajomi 2. st. : {sorted(wynik)}")

    # Oczekiwane wyniki (po poprawnej implementacji):
    # Alicja → znajomi 2. st.: ['Damian', 'Ewa', 'Grażyna']
    # Damian → znajomi 2. st.: ['Alicja', 'Ewa', 'Grażyna', 'Jan']
    # Jan    → znajomi 2. st.: ['Bartosz', 'Damian', 'Filip']
