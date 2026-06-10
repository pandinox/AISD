# =============================================================================
# Zadanie 3 – Drzewo Trie (Prefix Tree) – Autouzupełnianie
# =============================================================================
# OPIS PROBLEMU:
#   Implementujesz mechanizm podpowiedzi (autocomplete) dla wyszukiwarki
#   produktów w sklepie internetowym.
#   Gdy użytkownik wpisuje "la", system powinien błyskawicznie podpowiedzieć:
#   "laptop", "lampa", "lato".
#
#   Zwykłe przeszukiwanie listy słów po każdym naciśnięciu klawisza kosztuje
#   O(n * m) – za wolne przy dużym katalogu. Drzewo Trie pozwala znaleźć
#   wszystkie słowa zaczynające się od prefiksu w O(m + k), gdzie m = długość
#   prefiksu, k = liczba wyników.
#
#   Jak działa Trie?
#     Każda litera słowa to osobny węzeł. Słowa "la", "laptop", "lampa"
#     współdzielą węzły dla "l" i "a":
#
#       (root)
#         └── l
#               └── a  [koniec: "la"]
#                     ├── p
#                     │     └── t
#                     │           └── o
#                     │                 └── p  [koniec: "laptop"]
#                     └── m
#                           └── p
#                                 └── a  [koniec: "lampa"]
#
#   Twoim zadaniem jest:
#     1. Implementacja wstawiania słowa do drzewa Trie.
#     2. Sprawdzenie, czy dane słowo istnieje w słowniku.
#     3. Znalezienie wszystkich słów zaczynających się od podanego prefiksu.
#
# METODY / OPERACJE do poznania:
#   - Dzieci węzła:        node.dzieci           – słownik {litera: TrieNode}
#   - Sprawdzenie litery:  litera in node.dzieci  – O(1), jak klucz w dict
#   - Dodanie litery:      node.dzieci[litera] = TrieNode()
#   - Przejście do litery: node = node.dzieci[litera]
#   - Koniec słowa:        node.czy_koniec = True  – flaga na ostatniej literze
#   - Zbieranie wyników:   rekurencja DFS z budowaniem prefiksu
# =============================================================================


# =============================================================================
# MODEL DANYCH (dostarczony – nie musisz zmieniać)
# =============================================================================
class TrieNode:
    """Pojedynczy węzeł drzewa Trie — reprezentuje jedną literę."""

    def __init__(self):
        # Słownik dzieci: {'l': TrieNode, 'a': TrieNode, ...}
        self.dzieci: dict[str, TrieNode] = {}
        # Czy w tym miejscu kończy się jakieś słowo ze słownika
        self.czy_koniec: bool = False


class Trie:
    """
    Drzewo Trie (Prefix Tree) — struktura do przechowywania i wyszukiwania słów
    po prefiksie. Idealna do autouzupełniania, sprawdzania pisowni i słowników.

    Wszystkie operacje zaczynają się od korzenia (self.root), który jest pustym
    węzłem — nie reprezentuje żadnej litery.
    """

    def __init__(self):
        self.root = TrieNode()

    # ============================================================
    # FUNKCJA 1 – Dodawanie słowa
    # ============================================================
    def wstaw(self, slowo: str) -> None:
        """
        Wstawia słowo do drzewa Trie litera po literze.

        Intuicja: idziemy od korzenia w dół — dla każdej litery sprawdzamy,
        czy węzeł już istnieje. Jeśli nie, tworzymy go. Na końcu oznaczamy
        węzeł ostatniej litery jako koniec słowa.

        Złożoność czasowa:  O(m), gdzie m = długość słowa
        Złożoność pamięciowa: O(m) w najgorszym razie (zupełnie nowe słowo)
        """
        # TODO: Iteruj po literach słowa. Dla każdej litery sprawdź, czy istnieje
        #       odpowiedni węzeł — jeśli nie, utwórz go. Przejdź do węzła tej litery.
        #       Po przetworzeniu wszystkich liter oznacz bieżący węzeł jako koniec słowa.
        node = self.root

        for litera in slowo:
            if litera not in node.dzieci:
                node.dzieci[litera] = TrieNode()

            node = node.dzieci[litera]

        node.czy_koniec = True

    # ============================================================
    # FUNKCJA 2 – Wyszukiwanie słowa
    # ============================================================
    def szukaj(self, slowo: str) -> bool:
        """
        Sprawdza, czy podane słowo w całości istnieje w słowniku.
        Zwraca True tylko wtedy, gdy słowo zostało wcześniej wstawione przez wstaw().

        Intuicja: schodzimy po literach — jeśli którejś litery brakuje w węźle,
        słowa nie ma. Dotarcie do końca liter nie wystarczy: trzeba sprawdzić,
        czy ostatni węzeł był oznaczony jako koniec słowa (odróżnia "la" od "laptop").

        Złożoność czasowa:  O(m), gdzie m = długość słowa
        Złożoność pamięciowa: O(1)
        """
        # TODO: Przejdź po literach słowa — jeśli brakuje litery w węźle, zwróć False.
        #       Po dojściu do końca zwróć wartość flagi czy_koniec ostatniego węzła.
        node = self.root

        for litera in slowo:
            if litera not in node.dzieci:
                return False

            node = node.dzieci[litera]

        return node.czy_koniec

    # ============================================================
    # FUNKCJA 3 – Autouzupełnianie (podpowiedzi)
    # ============================================================
    def podpowiedzi(self, prefiks: str) -> list[str]:
        """
        Zwraca listę wszystkich słów ze słownika, które zaczynają się od `prefiks`.
        Jeśli żadne słowo nie pasuje, zwraca pustą listę.

        Intuicja: najpierw schodzimy do węzła odpowiadającego ostatniej literze
        prefiksu (tak jak w szukaj). Jeśli węzeł istnieje, rekurencyjnie
        przechodzimy po wszystkich gałęziach poddrzewa, zbierając kompletne słowa.

        Złożoność czasowa:  O(m + k), gdzie m = długość prefiksu, k = liczba wyników
        Złożoność pamięciowa: O(k) – lista wynikowa

        Przykład:
            słownik: ["laptop", "lampa", "lato", "monitor"]
            podpowiedzi("la") → ["laptop", "lampa", "lato"]
            podpowiedzi("mon") → ["monitor"]
            podpowiedzi("xyz") → []
        """
        # TODO: Zejdź do węzła odpowiadającego ostatniej literze prefiksu.
        #       Jeśli którejś litery brakuje po drodze — zwróć pustą listę.
        #       Następnie wywołaj pomocniczą funkcję _zbierz_slowa(), która
        #       rekurencyjnie zbierze wszystkie słowa z poddrzewa.
        #       Zwróć posortowaną listę wyników.
        node = self.root

        for litera in prefiks:
            if litera not in node.dzieci:
                return []

            node = node.dzieci[litera]

        wyniki = []
        self._zbierz_slowa(node, prefiks, wyniki)

        return sorted(wyniki)

    def _zbierz_slowa(self, node: TrieNode, prefiks: str, wyniki: list[str]) -> None:
        """
        Pomocnicza metoda do podpowiedzi() — rekurencyjnie odwiedza wszystkie
        węzły w poddrzewie i zbiera kompletne słowa do listy `wyniki`.

        Dostarczona – nie musisz jej zmieniać. Wywołuje ją podpowiedzi().

        Złożoność: O(n), gdzie n = liczba węzłów w poddrzewie
        """
        if node.czy_koniec:
            wyniki.append(prefiks)
        for litera, dziecko in node.dzieci.items():
            self._zbierz_slowa(dziecko, prefiks + litera, wyniki)


# =============================================================================
# FUNKCJE POMOCNICZE (dostarczone – nie musisz ich zmieniać)
# =============================================================================
def _separator(tytul: str) -> None:
    print(f"\n{'=' * 50}")
    print(f"  {tytul}")
    print('=' * 50)


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== System Autouzupełniania – Trie ===\n")

    slownik = Trie()
    produkty = [
        "laptop", "lampa", "lato", "lawa",
        "monitor", "mysz", "myszka",
        "kabel", "kamera", "karta",
    ]

    _separator("Budowanie słownika Trie")
    for p in produkty:
        slownik.wstaw(p)
    print(f"  Wstawiono {len(produkty)} produktów do słownika.")

    # --- Test 1: Wyszukiwanie pełnych słów ---
    _separator("Test 1 – Wyszukiwanie słów (szukaj)")
    testy_szukaj = [
        ("laptop",  True),
        ("lampa",   True),
        ("la",      False),   # prefiks, nie pełne słowo
        ("rower",   False),
        ("myszka",  True),
        ("myszkaa", False),   # błąd w słowie
    ]
    for slowo, oczekiwane in testy_szukaj:
        wynik = slownik.szukaj(slowo)
        status = "OK" if wynik == oczekiwane else "BŁĄD"
        print(f"  [{status}] szukaj('{slowo}') = {wynik}  (oczekiwano: {oczekiwane})")

    # --- Test 2: Autouzupełnianie ---
    _separator("Test 2 – Autouzupełnianie (podpowiedzi)")
    testy_auto = [
        ("la",   ["lampa", "laptop", "lato", "lawa"]),
        ("mo",   ["monitor"]),
        ("my",   ["mysz", "myszka"]),
        ("ka",   ["kabel", "kamera", "karta"]),
        ("xyz",  []),
    ]
    for prefiks, oczekiwane in testy_auto:
        wyniki = slownik.podpowiedzi(prefiks)
        status = "OK" if sorted(wyniki) == sorted(oczekiwane) else "BŁĄD"
        print(f"  [{status}] podpowiedzi('{prefiks}') = {wyniki}")

    # --- Test 3: Pusty prefiks — wszystkie słowa ---
    _separator("Test 3 – Pusty prefiks (wszystkie słowa)")
    wszystkie = slownik.podpowiedzi("")
    print(f"  Liczba słów w słowniku: {len(wszystkie)}")
    print(f"  Słowa: {sorted(wszystkie)}")
