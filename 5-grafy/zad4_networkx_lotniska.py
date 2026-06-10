# =============================================================================
# Zadanie 4 – Analiza sieci lotniczej – Praca z Dokumentacją NetworkX
# =============================================================================
# OPIS PROBLEMU:
#   Analizujesz siatkę połączeń linii lotniczych. Każde połączenie to krawędź
#   między dwoma kodami lotnisk (np. "WAW" i "LHR"). Twoim zadaniem jest
#   znalezienie głównego węzła przesiadkowego (hubu) – lotniska, które
#   posiada największą liczbę bezpośrednich połączeń (najwyższy stopień
#   wierzchołka, ang. degree).
#
#   Nie ma tutaj gotowego przepisu – musisz samodzielnie przeszukać
#   dokumentację NetworkX (lub skorzystać z autouzupełniania IDE), aby
#   dowiedzieć się, jak pobrać stopnie wszystkich wierzchołków grafu.
#   Wskazówka: zacznij od obiektu G i sprawdź, co oferuje G.degree().
#
# METODY / OPERACJE do poznania:
#   - G.degree()          – zwraca stopnie wszystkich wierzchołków
#   - dict(G.degree())    – konwersja do słownika { lotnisko: stopien }
#   - max() z key=        – znajdowanie maksimum według wartości
#   - sorted() z key=     – sortowanie listy krotek według wartości
#   - Praca z dokumentacją biblioteki jako umiejętność inżynierska
# =============================================================================

import networkx as nx


# =============================================================================
# DANE – sieć połączeń lotniczych
# =============================================================================
# Format każdej krotki: (kod_lotniska_A, kod_lotniska_B)
# Graf nieskierowany: połączenie działa w obie strony.

polaczenia_lotnicze: list[tuple[str, str]] = [
    ("WAW", "LHR"),
    ("WAW", "CDG"),
    ("WAW", "FRA"),
    ("JFK", "LHR"),
    ("JFK", "LAX"),
    ("JFK", "CDG"),
    ("LHR", "CDG"),
    ("LHR", "DXB"),
    ("LHR", "JFK"),   # duplikat kierunkowy – NetworkX zignoruje
    ("CDG", "DXB"),
    ("LAX", "DXB"),
    ("FRA", "DXB"),
]

# Intuicja: Londyn (LHR) ma połączenia z WAW, JFK, CDG, DXB – powinien wygrać.
# Pełna analiza stopni (oczekiwana po implementacji):
#   LHR: 4  ← największy hub
#   CDG: 4  (LHR, WAW, JFK, DXB)
#   DXB: 4  (LHR, CDG, LAX, FRA)
#   JFK: 3, WAW: 3, LAX: 2, FRA: 2


# =============================================================================
# BUDOWANIE GRAFU – kod gotowy, przeanalizuj go
# =============================================================================

def zbuduj_graf_lotniczy(polaczenia: list[tuple[str, str]]) -> nx.Graph:
    """Tworzy graf nieskierowany z listy par kodów lotnisk."""
    G = nx.Graph()
    G.add_edges_from(polaczenia)
    return G


# =============================================================================
# FUNKCJA DO ZAIMPLEMENTOWANIA
# =============================================================================

def znajdz_glowny_hub(G: nx.Graph) -> tuple[str, int]:
    """
    Znajduje lotnisko z największą liczbą bezpośrednich połączeń (hub).

    Wskazówka krok po kroku:
      1. Pobierz stopnie wszystkich wierzchołków – sprawdź G.degree() w docs.
      2. Przekonwertuj wynik na słownik: dict(G.degree())
         Słownik ma postać: { "LHR": 4, "WAW": 3, ... }
      3. Znajdź klucz o maksymalnej wartości.
         Możesz użyć: max(slownik, key=slownik.get)
         lub: max(slownik.items(), key=lambda x: x[1])
      4. Zwróć krotkę (nazwa_hubu, liczba_polaczen).

    Parametry:
        G – graf lotniczy zbudowany przez zbuduj_graf_lotniczy()

    Zwraca:
        Krotkę (hub, liczba_polaczen):
          hub              – kod IATA lotniska z największą liczbą połączeń
          liczba_polaczen  – stopień tego wierzchołka
    """

    # TODO: Pobierz stopnie wszystkich wierzchołków korzystając z G.degree().
    #       Przekonwertuj wynik na słownik przy użyciu dict().
    #       Zapisz go w zmiennej 'stopnie'.
    stopnie = dict(G.degree())

    # TODO: Znajdź lotnisko z maksymalną wartością stopnia.
    #       Zapisz kod lotniska w zmiennej 'hub', a jego stopień w 'max_stopien'.
    hub = max(stopnie, key=stopnie.get)
    max_stopien = stopnie[hub]

    return hub, max_stopien


# =============================================================================
# PROGRAM GŁÓWNY – testy
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 4 – NetworkX: Analiza sieci lotniczej")
    print("=" * 55)

    # Budowanie grafu (kod gotowy)
    G_loty = zbuduj_graf_lotniczy(polaczenia_lotnicze)

    print(f"\nGraf wczytany poprawnie.")
    print(f"  Liczba lotnisk (węzłów):       {G_loty.number_of_nodes()}")
    print(f"  Liczba połączeń (krawędzi):    {G_loty.number_of_edges()}")

    print("\nWszystkie lotniska w sieci:")
    for lotnisko in sorted(G_loty.nodes()):
        print(f"  {lotnisko}")

    # Analiza stopni (do zaimplementowania)
    print("\n" + "-" * 55)
    print("Szukam głównego hubu przesiadkowego...")
    print("-" * 55)

    hub, liczba = znajdz_glowny_hub(G_loty)

    if hub:
        print(f"\nGłówny hub: {hub}  ({liczba} bezpośrednich połączeń)")

        # Bonus: wypisz pełny ranking lotnisk posortowany malejąco
        print("\nRanking lotnisk wg liczby połączeń:")
        wszystkie_stopnie = dict(G_loty.degree())
        ranking = sorted(wszystkie_stopnie.items(), key=lambda x: x[1], reverse=True)
        for miejsce, (lotnisko, stopien) in enumerate(ranking, start=1):
            znacznik = " ← HUB" if lotnisko == hub else ""
            print(f"  {miejsce}. {lotnisko}: {stopien} połączeń{znacznik}")
    else:
        print("\n  [!] Funkcja nie została jeszcze zaimplementowana.")

    # Oczekiwane wyniki (po poprawnej implementacji):
    # Główny hub: LHR  (4 bezpośrednie połączenia)
    # lub CDG / DXB (też 4) – zależy od kolejności przy remisie
