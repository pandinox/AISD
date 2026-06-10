# =============================================================================
# Zadanie 1 – Drzewo (Tree) – hierarchiczna struktura kategorii
# =============================================================================
# OPIS PROBLEMU:
#   Pracujesz jako programista w firmie prowadzącej sklep internetowy.
#   Kategorie produktów są zorganizowane hierarchicznie – każda kategoria
#   może mieć dowolną liczbę podkategorii, a te z kolei swoje własne
#   podkategorie (drzewo n-arne, ang. n-ary tree).
#
#   Przykład struktury:
#     Sklep
#     ├── Elektronika
#     │   ├── Laptopy
#     │   └── Telefony
#     │       ├── Android
#     │       └── iPhone
#     └── Dom i Ogród
#         ├── Meble
#         └── Narzędzia
#
#   Twoim zadaniem jest:
#     1. Uzupełnienie klasy KategoriaNode o metodę dodaj_podkategorie().
#     2. Implementacja funkcji wyswietl_drzewo() – rekurencyjne wypisywanie
#        drzewa z wcięciami (2 spacje na każdy poziom głębokości).
#     3. Implementacja funkcji policz_wszystkie() – zliczanie wszystkich węzłów.
#
# METODY / OPERACJE do poznania:
#   - Tworzenie węzła:              KategoriaNode("nazwa")
#   - Dodawanie dziecka:            rodzic.dodaj_podkategorie(dziecko)
#   - Dostęp do dzieci:             node.dzieci          – lista węzłów-dzieci
#   - Dostęp do nazwy:              node.nazwa
#   - Rekurencja:                   wywołanie funkcji na każdym z node.dzieci
#   - Wcięcie tekstowe:             " " * (poziom * 2)
# =============================================================================


# =============================================================================
# KLASA – Węzeł drzewa kategorii
# =============================================================================
class KategoriaNode:
    """
    Reprezentuje pojedynczy węzeł (kategorię) w drzewie kategorii sklepu.

    Atrybuty:
        nazwa  (str)             – nazwa kategorii
        dzieci (list[KategoriaNode]) – lista bezpośrednich podkategorii
    """

    # Deklaracje atrybutów (IDE hint) – wartości przypisujesz w __init__
    nazwa: str
    dzieci: list["KategoriaNode"]

    def __init__(self, nazwa: str) -> None:
        # TODO: Zainicjalizuj atrybuty węzła — nazwę kategorii i pustą listę dzieci.
        self.nazwa = nazwa
        self.dzieci = []

    def dodaj_podkategorie(self, podkategoria: "KategoriaNode") -> None:
        """
        Dodaje `podkategoria` jako bezpośrednie dziecko bieżącego węzła.

        Przykład użycia:
            elektronika = KategoriaNode("Elektronika")
            laptopy     = KategoriaNode("Laptopy")
            elektronika.dodaj_podkategorie(laptopy)
        """
        # TODO: Dodaj podkategorię do listy dzieci bieżącego węzła.
        self.dzieci.append(podkategoria)

    def __repr__(self) -> str:
        return f"KategoriaNode('{self.nazwa}', dzieci={len(self.dzieci)})"


# =============================================================================
# FUNKCJA 1 – Wyświetl drzewo (rekurencja)
# =============================================================================
def wyswietl_drzewo(node: KategoriaNode, poziom: int = 0) -> None:
    """
    Rekurencyjnie wypisuje drzewo kategorii w konsoli.
    Każdy poziom głębokości jest wcięty o 2 spacje.

    Oczekiwany wynik dla drzewa z opisu:
        Sklep
          Elektronika
            Laptopy
            Telefony
              Android
              iPhone
          Dom i Ogród
            Meble
            Narzędzia

    Args:
        node   – bieżący węzeł do wypisania
        poziom – głębokość węzła w drzewie (korzeń = 0)
    """
    # TODO: Wypisz nazwę bieżącego węzła z wcięciem proporcjonalnym do jego głębokości,
    #       a następnie rekurencyjnie wyświetl każde dziecko (o jeden poziom głębiej).
    print(" " * (poziom * 2) + node.nazwa)
    for dziecko in node.dzieci:
        wyswietl_drzewo(dziecko, poziom + 1)


# =============================================================================
# FUNKCJA 2 – Policz wszystkie węzły w drzewie (rekurencja)
# =============================================================================
def policz_wszystkie(node: KategoriaNode) -> int:
    """
    Rekurencyjnie zlicza wszystkie węzły w drzewie
    (łącznie z korzeniem i wszystkimi podkategoriami).

    Args:
        node – korzeń (lub poddrzewo) do zliczenia

    Zwraca:
        int – całkowita liczba węzłów
    """
    # TODO: Policz bieżący węzeł i rekurencyjnie dodaj liczbę węzłów
    #       ze wszystkich poddrzew dzieci. Zwróć sumę.
    licznik = 1

    for dziecko in node.dzieci:
        licznik += policz_wszystkie(dziecko)

    return licznik


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":

    # --- Budowa drzewa kategorii sklepu -------------------------------------
    # Gotowy kod – NIE modyfikuj tej sekcji.
    # Twoje funkcje muszą poprawnie obsłużyć poniższe drzewo.

    sklep = KategoriaNode("Sklep (korzeń)")

    # Gałąź 1: Elektronika
    elektronika = KategoriaNode("Elektronika")
    laptopy     = KategoriaNode("Laptopy")
    telefony    = KategoriaNode("Telefony")
    android     = KategoriaNode("Android")
    iphone      = KategoriaNode("iPhone")

    telefony.dodaj_podkategorie(android)
    telefony.dodaj_podkategorie(iphone)
    elektronika.dodaj_podkategorie(laptopy)
    elektronika.dodaj_podkategorie(telefony)

    # Gałąź 2: Dom i Ogród
    dom_i_ogrod = KategoriaNode("Dom i Ogród")
    meble       = KategoriaNode("Meble")
    narzedzia   = KategoriaNode("Narzędzia")
    fotele      = KategoriaNode("Fotele")
    sofy        = KategoriaNode("Sofy")

    meble.dodaj_podkategorie(fotele)
    meble.dodaj_podkategorie(sofy)
    dom_i_ogrod.dodaj_podkategorie(meble)
    dom_i_ogrod.dodaj_podkategorie(narzedzia)

    # Gałąź 3: Odzież
    odziez      = KategoriaNode("Odzież")
    meska       = KategoriaNode("Męska")
    damska      = KategoriaNode("Damska")
    odziez.dodaj_podkategorie(meska)
    odziez.dodaj_podkategorie(damska)

    # Podpięcie gałęzi do korzenia
    sklep.dodaj_podkategorie(elektronika)
    sklep.dodaj_podkategorie(dom_i_ogrod)
    sklep.dodaj_podkategorie(odziez)

    # --- Test 1: Wyświetlenie całego drzewa ----------------------------------
    print("=" * 50)
    print("Test 1 – Struktura drzewa kategorii:")
    print("=" * 50)
    wyswietl_drzewo(sklep)

    # --- Test 2: Zliczanie węzłów --------------------------------------------
    print("\n" + "=" * 50)
    print("Test 2 – Liczba kategorii w drzewie:")
    print("=" * 50)
    liczba = policz_wszystkie(sklep)
    print(f"Łączna liczba kategorii (węzłów): {liczba}")
    print("(Oczekiwana wartość: 14)")

