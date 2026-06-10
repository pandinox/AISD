# =============================================================================
# Playground – Grafy w Pythonie – Wprowadzenie i podstawy NetworkX
# =============================================================================
# OPIS PROBLEMU:
#   Ten plik to interaktywny plac zabaw (playground) do analizy gotowego kodu.
#   Zobaczysz, jak reprezentować graf nieskierowany jako listę sąsiedztwa
#   przy użyciu zwykłego słownika Pythona (dict[str, list[str]]).
#   Następnie ten sam graf zostanie odwzorowany w bibliotece NetworkX,
#   która dostarcza gotowe algorytmy i narzędzia do wizualizacji.
#
# METODY / OPERACJE do poznania:
#   - Reprezentacja grafu jako słownik: { wierzcholek: [sasiedzi] }
#   - nx.Graph()          – tworzenie obiektu grafu nieskierowanego
#   - G.add_edges_from()  – dodawanie krawędzi z listy par
#   - nx.draw()           – rysowanie grafu (wymaga matplotlib)
#   - G.nodes(), G.edges()– dostęp do wierzchołków i krawędzi
# =============================================================================

import networkx as nx
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Dane globalne – mała sieć społecznościowa (5 osób)
# ---------------------------------------------------------------------------
# Klucz = osoba, wartość = lista jej bezpośrednich znajomych.
# Graf jest nieskierowany, więc każda relacja pojawia się po obu stronach.

GRAF_SLOWNIK: dict[str, list[str]] = {
    "Alicja":  ["Bartosz", "Celina"],
    "Bartosz": ["Alicja", "Celina", "Damian"],
    "Celina":  ["Alicja", "Bartosz", "Ewa"],
    "Damian":  ["Bartosz", "Ewa"],
    "Ewa":     ["Celina", "Damian"],
}


# =============================================================================
# CZĘŚĆ 1 – Reprezentacja grafu jako słownik Pythona
# =============================================================================

def pokaz_graf_jako_slownik(graf: dict[str, list[str]]) -> None:
    """Wypisuje wierzchołki i unikalne krawędzie grafu zapisanego jako słownik."""

    print("=" * 50)
    print("CZĘŚĆ 1 – Graf jako słownik Pythona")
    print("=" * 50)

    print("\nWierzchołki (osoby) w grafie:")
    for osoba in graf:
        print(f"  {osoba}")

    print("\nKrawędzie (znajomości) w grafie:")
    wypisane: set[frozenset] = set()
    for osoba, znajomi in graf.items():
        for znajomy in znajomi:
            krawedz = frozenset({osoba, znajomy})
            if krawedz not in wypisane:
                print(f"  {osoba} -- {znajomy}")
                wypisane.add(krawedz)

    print(f"\nLiczba wierzchołków: {len(graf)}")
    print(f"Liczba krawędzi:     {len(wypisane)}")


# =============================================================================
# CZĘŚĆ 2 – Ten sam graf w bibliotece NetworkX
# =============================================================================

def pokaz_graf_networkx(graf: dict[str, list[str]]) -> nx.Graph:
    """
    Tworzy obiekt nx.Graph z podanego słownika list sąsiedztwa,
    wypisuje podstawowe informacje i zwraca gotowy obiekt grafu.
    """

    print("\n" + "=" * 50)
    print("CZĘŚĆ 2 – Graf w bibliotece NetworkX")
    print("=" * 50)

    # Tworzymy pusty graf nieskierowany
    G = nx.Graph()

    # Dodajemy krawędzie bezpośrednio ze słownika listy sąsiedztwa.
    # add_edges_from() akceptuje iterowalny zbiór par (u, v).
    for osoba, znajomi in graf.items():
        for znajomy in znajomi:
            G.add_edge(osoba, znajomy)

    print(f"\nWierzchołki NetworkX: {list(G.nodes())}")
    print(f"Krawędzie NetworkX:   {list(G.edges())}")
    print(f"Liczba wierzchołków:  {G.number_of_nodes()}")
    print(f"Liczba krawędzi:      {G.number_of_edges()}")

    # Stopień wierzchołka = liczba bezpośrednich sąsiadów
    print("\nStopień każdego wierzchołka (liczba znajomych):")
    for osoba, stopien in G.degree():
        print(f"  {osoba}: {stopien} znajomych")

    return G


# =============================================================================
# CZĘŚĆ 3 – Wizualizacja grafu
# =============================================================================

def wizualizuj_graf(G: nx.Graph, nazwa_pliku: str = "playground_siec_spolecznosciowa.png") -> None:
    """
    Rysuje graf przy użyciu NetworkX i Matplotlib oraz zapisuje obraz do pliku.
    Aby wyświetlić wykres w oknie, odkomentuj wywołanie plt.show().
    """

    print("\n" + "=" * 50)
    print("CZĘŚĆ 3 – Wizualizacja (NetworkX + Matplotlib)")
    print("=" * 50)

    # Układ wierzchołków na płaszczyźnie (spring = wierzchołki odpychają się)
    uklad = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(7, 5))
    plt.title("Sieć społecznościowa – 5 osób", fontsize=14)

    nx.draw(
        G,
        pos=uklad,
        with_labels=True,       # wyświetl nazwy wierzchołków
        node_color="skyblue",   # kolor węzłów
        node_size=1800,         # rozmiar węzłów
        font_size=11,
        font_weight="bold",
        edge_color="gray",
        width=2,
    )

    # Odkomentuj poniższą linię, aby wyświetlić okno z wykresem:
    plt.show()

    # Zapis wykresu do pliku PNG (działa bez okna graficznego)
    plt.savefig(nazwa_pliku, dpi=120, bbox_inches="tight")
    print(f"\nWykres zapisano do pliku: {nazwa_pliku}")
    print("Aby wyświetlić wykres w oknie, odkomentuj linię 'plt.show()' w kodzie.")

if __name__ == "__main__":
    pokaz_graf_jako_slownik(GRAF_SLOWNIK)
    G = pokaz_graf_networkx(GRAF_SLOWNIK)
    wizualizuj_graf(G)
