# =============================================================================
# Zadanie 2 – ZBIÓR (SET) – Porównanie wydajności wyszukiwania O(n) vs O(1)
# =============================================================================
# OPIS PROBLEMU:
#   Jedną z największych zalet struktur hashujących jest błyskawiczne wyszukiwanie.
#   Sprawdzenie, czy element należy do listy, wymaga przejrzenia jej element
#   po elemencie – złożoność O(n). Zbiór (set) oparty na tablicy hashowej
#   potrafi odpowiedzieć na to samo pytanie w czasie O(1) – niezależnie od
#   liczby elementów! W tym zadaniu zmierzysz tę różnicę empirycznie.
#
# METODY / OPERACJE do poznania:
#   - time.perf_counter()              – precyzyjny pomiar czasu wykonania
#   - operator `in` dla list           – wyszukiwanie liniowe O(n)
#   - operator `in` dla zbiorów (set)  – wyszukiwanie hashowe O(1)
#   - set(lista)                       – konwersja listy na zbiór
# =============================================================================

import time
import random

# =============================================================================
# PRZYGOTOWANIE DANYCH – kod gotowy, nie modyfikuj tej sekcji
# =============================================================================

ROZMIAR_DANYCH = 100_000
LICZBA_POWTORZEN = 1_000   # ile razy powtarzamy wyszukiwanie w benchmarku

# Tworzymy listę 100 000 losowych liczb całkowitych z zakresu [0, 200 000].
# Zakres jest większy niż rozmiar danych – część wartości NIE będzie w strukturze.
random.seed(42)  # ziarno losowości – każdy student dostanie te same dane
lista_danych: list[int] = [random.randint(0, 200_000) for _ in range(ROZMIAR_DANYCH)]

# Konwersja listy na zbiór – ta operacja wykonywana jest RAZ, nie mierzy jej czasu
zbior_danych: set[int] = set(lista_danych)

# Wybieramy element do wyszukania: wartość spoza zakresu (najgorszy przypadek)
# – gwarantuje, że lista będzie musiała przejrzeć WSZYSTKIE elementy
SZUKANY_ELEMENT = 999_999


# =============================================================================
# FUNKCJE DO UZUPEŁNIENIA
# =============================================================================

def zmierz_czas_listy(lista: list[int], element: int) -> float | None:  # type: ignore[return]
    """
    Mierzy łączny czas LICZBA_POWTORZEN wyszukiwań elementu w liście.

    Args:
        lista:   lista liczb całkowitych
        element: szukana wartość

    Returns:
        łączny czas wyszukiwań w sekundach (float)
    """
    # TODO: 1. Zapisz czas startowy za pomocą time.perf_counter().
    # TODO: 2. W pętli wykonaj LICZBA_POWTORZEN razy operację: element in lista
    #          (wynik operacji możesz zignorować – użyj zmiennej _).
    # TODO: 3. Zapisz czas końcowy za pomocą time.perf_counter().
    # TODO: 4. Oblicz i zwróć różnicę: czas_konca - czas_startu.
    czas_startu = time.perf_counter()

    for _ in range(LICZBA_POWTORZEN):
        _ = element in lista

    czas_konca = time.perf_counter()

    return czas_konca - czas_startu


def zmierz_czas_zbioru(zbior: set[int], element: int) -> float | None:  # type: ignore[return]
    """
    Mierzy łączny czas LICZBA_POWTORZEN wyszukiwań elementu w zbiorze.

    Args:
        zbior:   zbiór liczb całkowitych
        element: szukana wartość

    Returns:
        łączny czas wyszukiwań w sekundach (float)
    """
    # TODO: 1. Zapisz czas startowy za pomocą time.perf_counter().
    # TODO: 2. W pętli wykonaj LICZBA_POWTORZEN razy operację: element in zbior
    #          (wynik operacji możesz zignorować – użyj zmiennej _).
    # TODO: 3. Zapisz czas końcowy za pomocą time.perf_counter().
    # TODO: 4. Oblicz i zwróć różnicę: czas_konca - czas_startu.
    czas_startu = time.perf_counter()

    for _ in range(LICZBA_POWTORZEN):
        _ = element in zbior

    czas_konca = time.perf_counter()

    return czas_konca - czas_startu


def wypisz_wyniki(czas_listy: float | None, czas_zbioru: float | None) -> None:
    """
    Wypisuje sformatowane wyniki benchmarku w konsoli.
    Metoda pomocnicza – gotowa, nie modyfikuj.

    Args:
        czas_listy: łączny czas wyszukiwań w liście [s]
        czas_zbioru: łączny czas wyszukiwań w zbiorze [s]
    """
    print("\n" + "=" * 60)
    print("  WYNIKI BENCHMARKU – wyszukiwanie elementu")
    print("=" * 60)
    print(f"  Rozmiar danych      : {ROZMIAR_DANYCH:>10,} elementów")
    print(f"  Liczba powtórzeń    : {LICZBA_POWTORZEN:>10,} wyszukiwań")
    print(f"  Szukany element     : {SZUKANY_ELEMENT:>10,}  (nieobecny – najgorszy przypadek)")
    print("-" * 60)

    if czas_listy is None or czas_zbioru is None:
        print("  [!] Brak wyników – uzupełnij metody zmierz_czas_listy()")
        print("      i zmierz_czas_zbioru(), a następnie uruchom ponownie.")
        print("=" * 60)
        return

    print(f"  Czas dla listy  (O(n)): {czas_listy:>10.4f} s")
    print(f"  Czas dla zbioru (O(1)): {czas_zbioru:>10.6f} s")
    print("-" * 60)

    if czas_zbioru > 0:
        krotnosc = czas_listy / czas_zbioru
        print(f"  Zbiór był SZYBSZY o : {krotnosc:>9.1f}x")
    print("=" * 60)
    print()
    print("  Wniosek:")
    print("  Przy 100 000 elementach różnica jest wyraźna.")
    print("  Wyobraź sobie bazę danych z milionami rekordów – ")
    print("  O(1) vs O(n) to różnica między milisekundami a minutami!")
    print("=" * 60)


# =============================================================================
# DEMONSTRACJA – uruchom plik, aby zobaczyć wyniki benchmarku
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 2 – Benchmark: lista O(n) vs zbiór O(1)")
    print("=" * 60)
    print(f"\n  Przygotowano {ROZMIAR_DANYCH:,} elementów danych.")
    print(f"  Każde wyszukiwanie zostanie powtórzone {LICZBA_POWTORZEN:,} razy.\n")

    print("  [>>] Uruchamiam pomiar dla listy ...")
    wynik_listy = zmierz_czas_listy(lista_danych, SZUKANY_ELEMENT)

    print("  [>>] Uruchamiam pomiar dla zbioru ...")
    wynik_zbioru = zmierz_czas_zbioru(zbior_danych, SZUKANY_ELEMENT)

    wypisz_wyniki(wynik_listy, wynik_zbioru)
