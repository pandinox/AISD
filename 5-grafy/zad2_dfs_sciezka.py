# =============================================================================
# Zadanie 2 – Przeszukiwanie Wgłąb (DFS) – Wykrywanie ścieżki
# =============================================================================
# OPIS PROBLEMU:
#   Wyobraź sobie, że chcesz sprawdzić, czy dwie osoby w sieci społecznościowej
#   są w ogóle ze sobą połączone – czy istnieje jakakolwiek ścieżka znajomości
#   łącząca osobę startową z osobą docelową (nawet przez wielu pośredników).
#
#   Zaimplementuj algorytm DFS (Depth-First Search) w wersji ITERACYJNEJ,
#   który odpowie: TAK lub NIE – czy istnieje ścieżka między dwoma węzłami.
#
#   *** WAŻNE – PORÓWNAJ Z ZADANIEM 1 (BFS) ***
#   Porównaj ten kod z BFS z Zadania 1. Zobacz, jak zmiana kolejki na stos
#   (popleft na pop) całkowicie zmienia strategię przeszukiwania:
#
#     BFS używa kolejki FIFO → pobiera element z POCZĄTKU → wszerz (warstwami)
#       kolejka.popleft()  ← usuwa z lewej strony (przód kolejki)
#
#     DFS używa stosu LIFO → pobiera element z KOŃCA  → wgłąb (jedna gałąź)
#       stos.pop()         ← usuwa z prawej strony (wierzchołek stosu)
#
#   Struktura pętli while, zarządzanie zbiorem "odwiedzonych" i przeglądanie
#   sąsiadów jest IDENTYCZNE w obu algorytmach. Różni je tylko jedna operacja!
#
# METODY / OPERACJE do poznania:
#   - list jako stos LIFO: stos.append(x) – push, stos.pop() – pop
#   - set() – zbiór odwiedzonych węzłów zapobiegający cyklom
#   - Porównanie podejść: kolejka FIFO (BFS) vs stos LIFO (DFS)
# =============================================================================


# =============================================================================
# DANE – sieć społecznościowa (10 osób)
# =============================================================================
# Ta sama sieć co w Zadaniu 1 – możesz porównać wyniki obu algorytmów.

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

# Dodatkowy graf z izolowanym komponentem – do testowania braku ścieżki.
# "Zofia" i "Konrad" są połączeni ze sobą, ale odcięci od reszty sieci.
siec_z_izolacja: dict[str, list[str]] = {
    **siec_spolecznosciowa,
    "Zofia":  ["Konrad"],
    "Konrad": ["Zofia"],
}


# =============================================================================
# FUNKCJA DO ZAIMPLEMENTOWANIA
# =============================================================================

def czy_istnieje_sciezka_dfs(
    graf: dict[str, list[str]],
    start: str,
    cel: str
) -> bool:
    """
    Sprawdza, czy istnieje ścieżka między węzłem 'start' a węzłem 'cel'
    przy użyciu iteracyjnego algorytmu DFS (przeszukiwanie wgłąb).

    Parametry:
        graf  – słownik list sąsiedztwa
        start – węzeł startowy (punkt wyjścia)
        cel   – węzeł docelowy (punkt docelowy)

    Zwraca:
        True  – jeśli ścieżka istnieje
        False – jeśli ścieżka nie istnieje (węzły w różnych komponentach)
    """

    # Przypadek brzegowy: start i cel to ten sam węzeł.
    if start == cel:
        return True

    # Zbiór odwiedzonych węzłów – zapobiega zapętleniu w grafach z cyklami.
    odwiedzone: set[str] = set()
    odwiedzone.add(start)

    # Stos DFS – zwykła lista Pythona.
    # .append() dodaje na wierzchołek stosu (prawa strona listy).
    # .pop()    zdejmuje z wierzchołka stosu (prawa strona listy) – LIFO!
    #
    # *** Porównaj z BFS: tam była kolejka deque z .popleft() ***
    stos: list[str] = [start]

    # --- Główna pętla DFS ---
    while stos:
        # TODO: Zdejmij węzeł z WIERZCHOŁKA stosu (użyj .pop() – LIFO!).
        #       Porównaj: w BFS było tu kolejka.popleft() (FIFO).
        #       To jedyna strukturalna różnica między DFS a BFS!


        # TODO: Przejrzyj wszystkich sąsiadów bieżącego węzła
        #       (skorzystaj z graf[biezacy_wezel]).
        #       Dla każdego sąsiada:
        #         a) Jeśli sąsiad == cel, ścieżka została znaleziona –
        #            zwróć True od razu.
        #         b) Jeśli sąsiad nie był jeszcze odwiedzony:
        #            - dodaj go do zbioru 'odwiedzone'
        #            - wrzuć go na stos (.append())
        biezacy_wezel = stos.pop()

        for sasiad in graf[biezacy_wezel]:
            if sasiad == cel:
                return True

            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                stos.append(sasiad)

    # Jeśli stos jest pusty, a cel nie został znaleziony – brak ścieżki.
    return False


# =============================================================================
# PROGRAM GŁÓWNY – testy
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 2 – DFS: Czy istnieje ścieżka?")
    print("=" * 55)

    # Pary do sprawdzenia (start, cel, oczekiwany wynik)
    testy = [
        ("Alicja",  "Jan",    True,  siec_spolecznosciowa),
        ("Alicja",  "Irena",  True,  siec_spolecznosciowa),
        ("Grażyna", "Jan",    True,  siec_spolecznosciowa),
        ("Alicja",  "Zofia",  False, siec_z_izolacja),
        ("Konrad",  "Henryk", False, siec_z_izolacja),
    ]

    for start, cel, oczekiwany, graf in testy:
        wynik = czy_istnieje_sciezka_dfs(graf, start, cel)
        status = "OK" if wynik == oczekiwany else "BŁĄD"
        odpowiedz = "TAK, istnieje" if wynik else "NIE, brak ścieżki"
        print(f"\n  [{status}] {start} → {cel}")
        print(f"        Wynik: {odpowiedz}  (oczekiwano: {oczekiwany})")

    # Oczekiwane wyniki (po poprawnej implementacji):
    # Alicja  → Jan    : TAK  (Alicja→Bartosz→Ewa→Jan)
    # Alicja  → Irena  : TAK  (Alicja→Bartosz→Damian→Irena)
    # Grażyna → Jan    : TAK  (Grażyna→Henryk→Damian→Irena→Jan)
    # Alicja  → Zofia  : NIE  (różne komponenty)
    # Konrad  → Henryk : NIE  (różne komponenty)
