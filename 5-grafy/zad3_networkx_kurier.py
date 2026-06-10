# =============================================================================
# Zadanie 3 – Biblioteka NetworkX – Optymalizacja trasy kurierskiej
# =============================================================================
# OPIS PROBLEMU:
#   Firma kurierska obsługuje sieć miast połączonych drogami. Każda droga ma
#   przypisany szacowany czas przejazdu w minutach (waga krawędzi).
#   Dyspozytor chce znaleźć NAJKRÓTSZĄ POD WZGLĘDEM CZASU trasę z magazynu
#   centralnego do wskazanego punktu odbioru przesyłki.
#
#   Zamiast implementować algorytm Dijkstry od zera, użyj gotowych funkcji
#   z biblioteki NetworkX. Twoje zadanie to poprawne wywołanie tych funkcji
#   z odpowiednimi parametrami – w szczególności z parametrem weight="czas",
#   który wskazuje NetworkX, której wagi ma używać przy obliczeniach.
#
# METODY / OPERACJE do poznania:
#   - nx.Graph()                    – graf nieskierowany
#   - G.add_edge(u, v, weight=w)    – krawędź z wagą (przez argument kluczowy)
#   - nx.shortest_path(G, src, tgt, weight="czas")
#                                   – zwraca listę węzłów tworzących trasę
#   - nx.shortest_path_length(G, src, tgt, weight="czas")
#                                   – zwraca łączny koszt (sumę wag) trasy
#   - Parametr weight=              – nazwa atrybutu krawędzi używanego jako waga
# =============================================================================

import networkx as nx


# =============================================================================
# DANE – mapa połączeń kurierskich (graf ważony)
# =============================================================================
# Format każdej krotki: (miasto_A, miasto_B, czas_przejazdu_w_minutach)
# Graf jest nieskierowany – krawędź działa w obie strony.

polaczenia_kurierskie: list[tuple[str, str, int]] = [
    ("Magazyn",    "Adamowo",    15),
    ("Magazyn",    "Brzeziny",   25),
    ("Adamowo",    "Centrum",    20),
    ("Adamowo",    "Dęblin",     40),
    ("Brzeziny",   "Centrum",    10),
    ("Brzeziny",   "Elbląg",     30),
    ("Centrum",    "Falenty",    15),
    ("Centrum",    "Dęblin",     20),
    ("Dęblin",     "Punkt_Cel",  10),
    ("Falenty",    "Punkt_Cel",  25),
    ("Elbląg",     "Punkt_Cel",  35),
]

# Wizualizacja struktury sieci (uproszczona):
#
#   Magazyn ──15──► Adamowo ──20──► Centrum ──15──► Falenty
#      │                │               │                │
#     25             40 │              20              25 │
#      │                ▼               ▼                ▼
#   Brzeziny ──10──► Centrum        Dęblin ──10──► Punkt_Cel
#      │
#     30
#      ▼
#   Elbląg ──35──► Punkt_Cel
#
# Najkrótsza trasa (oczekiwany wynik):
#   Magazyn → Brzeziny → Centrum → Dęblin → Punkt_Cel
#   Łączny czas: 25 + 10 + 20 + 10 = 65 minut


# =============================================================================
# BUDOWANIE GRAFU – kod gotowy, przeanalizuj go
# =============================================================================

def zbuduj_graf_kurierski(
    polaczenia: list[tuple[str, str, int]]
) -> nx.Graph:
    """
    Tworzy ważony graf nieskierowany na podstawie listy połączeń.
    Atrybut wagi krawędzi jest przechowywany pod kluczem 'czas'.
    """
    G = nx.Graph()

    for miasto_a, miasto_b, czas in polaczenia:
        # Dodajemy krawędź z atrybutem nazwanym 'czas'.
        # NetworkX przechowuje go jako: G[miasto_a][miasto_b]['czas']
        G.add_edge(miasto_a, miasto_b, czas=czas)

    return G


# =============================================================================
# FUNKCJA DO ZAIMPLEMENTOWANIA
# =============================================================================

def znajdz_optymalna_trase(
    G: nx.Graph,
    magazyn: str,
    punkt_odbioru: str
) -> tuple[list[str], float]:
    """
    Znajduje najkrótszą (optymalną pod względem czasu) trasę kurierską
    między magazynem a punktem odbioru.

    Parametry:
        G              – graf ważony zbudowany przez zbuduj_graf_kurierski()
        magazyn        – węzeł startowy (punkt nadania)
        punkt_odbioru  – węzeł docelowy (punkt odbioru przesyłki)

    Zwraca:
        Krotkę (trasa, laczny_czas), gdzie:
          trasa       – lista nazw miast od magazynu do punktu odbioru
          laczny_czas – suma wag krawędzi na wyznaczonej trasie (w minutach)
    """

    # TODO: Wywołaj funkcję nx.shortest_path() z parametrami:
    #         - G             (graf)
    #         - source=magazyn
    #         - target=punkt_odbioru
    #         - weight="czas" (nazwa atrybutu wagi krawędzi!)
    #       Wynik zapisz w zmiennej 'trasa'.
    # zamień None na właściwe wywołanie nx.shortest_path(...)
    trasa = nx.shortest_path(
        G,
        source=magazyn,
        target=punkt_odbioru,
        weight="czas"
    )

    # TODO: Wywołaj funkcję nx.shortest_path_length() z tymi samymi
    #       parametrami (G, source=..., target=..., weight="czas").
    #       Wynik zapisz w zmiennej 'laczny_czas'.
    # zamień 0.0 na właściwe wywołanie nx.shortest_path_length(...)
    laczny_czas = nx.shortest_path_length(
        G,
        source=magazyn,
        target=punkt_odbioru,
        weight="czas"
    )

    return trasa, laczny_czas


# =============================================================================
# PROGRAM GŁÓWNY – testy
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 3 – NetworkX: Optymalna trasa kurierska")
    print("=" * 55)

    # Budowanie grafu (kod gotowy)
    G_kurier = zbuduj_graf_kurierski(polaczenia_kurierskie)

    print(f"\nGraf wczytany poprawnie.")
    print(f"  Liczba miast (węzłów):        {G_kurier.number_of_nodes()}")
    print(f"  Liczba połączeń (krawędzi):   {G_kurier.number_of_edges()}")

    # Podgląd wag krawędzi
    print("\nPołączenia z czasami przejazdu:")
    for u, v, dane in G_kurier.edges(data=True):
        print(f"  {u:12} -- {v:12}  czas: {dane['czas']} min")

    # Wyznaczanie optymalnej trasy (do zaimplementowania)
    print("\n" + "-" * 55)
    print("Szukam optymalnej trasy: Magazyn → Punkt_Cel")
    print("-" * 55)

    trasa, czas = znajdz_optymalna_trase(G_kurier, "Magazyn", "Punkt_Cel")

    if trasa is not None:
        print(f"\nOptymalna trasa ({len(trasa) - 1} odcinków):")
        print(f"  {' → '.join(trasa)}")
        print(f"\nŁączny czas przejazdu: {czas} minut")
    else:
        print("\n  [!] Funkcja nie została jeszcze zaimplementowana.")

    # Oczekiwany wynik (po poprawnej implementacji):
    # Istnieją dwie trasy o identycznym czasie 65 minut:
    #   Trasa A: Magazyn → Brzeziny → Centrum → Dęblin → Punkt_Cel (25+10+20+10)
    #   Trasa B: Magazyn → Adamowo → Dęblin → Punkt_Cel (15+40+10)
    # NetworkX zwróci jedną z nich (obie są poprawne).
