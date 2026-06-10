# =============================================================================
# Zadanie 1 – MAPA HASHOWA – Implementacja własnej struktury słownikowej
# =============================================================================
# OPIS PROBLEMU:
#   Słowniki (mapy) są jedną z najważniejszych struktur danych w informatyce.
#   W tym zadaniu zaimplementujesz uproszczoną mapę hashową od podstaw.
#   Kluczowym pojęciem jest funkcja hashująca, która przekształca klucz (tekst)
#   na indeks tablicy. Gdy dwa różne klucze trafią do tego samego kubełka,
#   dochodzi do KOLIZJI – Twoim zadaniem jest jej obsługa metodą łańcuchową
#   (ang. chaining), czyli przechowywanie wielu par w jednym kubełku jako listy.
#
# METODY / OPERACJE do poznania:
#   - _funkcja_hashujaca(klucz)  – obliczanie indeksu kubełka na podstawie klucza
#   - wstaw(klucz, wartosc)      – dodawanie lub aktualizacja pary klucz-wartość
#   - pobierz(klucz)             – wyszukiwanie wartości na podstawie klucza
#   - wypisz()                   – podgląd wewnętrznej struktury mapy (gotowe)
# =============================================================================


class ProstaMapa:
    """Uproszczona mapa hashowa z obsługą kolizji metodą łańcuchową (chaining)."""

    def __init__(self, rozmiar: int = 10):
        """
        Inicjalizacja mapy hashowej.

        Args:
            rozmiar: liczba kubełków (domyślnie 10)
        """
        self.rozmiar = rozmiar
        # Tworzymy listę 'rozmiar' pustych kubełków.
        # Każdy kubełek to lista, która może przechowywać wiele par (klucz, wartosc).
        self.kubełki = [[] for _ in range(self.rozmiar)]

    # -------------------------------------------------------------------------

    def _funkcja_hashujaca(self, klucz: str) -> int:
        """
        Oblicza indeks kubełka dla podanego klucza.

        Algorytm: zsumuj kody ASCII wszystkich znaków klucza,
        następnie zastosuj operację modulo względem rozmiaru tablicy.

        Args:
            klucz: klucz tekstowy (str)

        Returns:
            indeks kubełka (int) z zakresu [0, rozmiar-1]
        """
        # TODO: Oblicz sumę kodów ASCII znaków klucza za pomocą funkcji ord()
        #       i wbudowanej funkcji sum(), a następnie zastosuj operator %
        #       z self.rozmiar, aby otrzymać prawidłowy indeks kubełka.
        suma = sum(ord(znak) for znak in klucz)
        indeks = suma % self.rozmiar
        return indeks

    # -------------------------------------------------------------------------

    def wstaw(self, klucz: str, wartosc) -> None:
        """
        Wstawia parę (klucz, wartosc) do mapy.
        Jeśli klucz już istnieje – aktualizuje jego wartość.
        Jeśli klucz nie istnieje  – dodaje nową parę do odpowiedniego kubełka.

        Obsługa kolizji: metoda łańcuchowa (chaining).
        Wiele par może współistnieć w tym samym kubełku jako lista krotek.

        Args:
            klucz:   klucz tekstowy identyfikujący element
            wartosc: dowolna wartość przypisana do klucza
        """
        # TODO: 1. Oblicz indeks kubełka używając self._funkcja_hashujaca(klucz).
        # TODO: 2. Pobierz kubełek spod obliczonego indeksu z self.kubełki.
        # TODO: 3. Przejrzyj kubełek w pętli – sprawdź, czy klucz już istnieje
        #          (porównaj pierwszy element każdej krotki z szukanym kluczem).
        #          Jeśli tak: zaktualizuj wartość (zastąp krotkę nową) i zakończ.
        # TODO: 4. Jeśli klucz NIE istnieje w kubełku: dołącz nową krotkę
        #          (klucz, wartosc) na koniec kubełka.
        indeks = self._funkcja_hashujaca(klucz)
        kubełek = self.kubełki[indeks]

        for i in range(len(kubełek)):
            zapisany_klucz, zapisana_wartosc = kubełek[i]

            if zapisany_klucz == klucz:
                kubełek[i] = (klucz, wartosc)
                return

        kubełek.append((klucz, wartosc))

    # -------------------------------------------------------------------------

    def pobierz(self, klucz: str):
        """
        Zwraca wartość skojarzoną z podanym kluczem.
        Jeśli klucz nie istnieje, zwraca stosowny komunikat.

        Args:
            klucz: klucz tekstowy do wyszukania

        Returns:
            wartość przypisana do klucza lub komunikat o jego braku
        """
        # TODO: 1. Oblicz indeks kubełka używając self._funkcja_hashujaca(klucz).
        # TODO: 2. Pobierz kubełek spod obliczonego indeksu.
        # TODO: 3. Przejrzyj kubełek w pętli – gdy znajdziesz krotkę,
        #          której pierwszy element jest równy kluczowi, zwróć drugi element.
        # TODO: 4. Jeśli pętla zakończy się bez znalezienia klucza,
        #          zwróć napis: f"Klucz '{klucz}' nie istnieje w mapie."
        indeks = self._funkcja_hashujaca(klucz)
        kubełek = self.kubełki[indeks]

        for zapisany_klucz, zapisana_wartosc in kubełek:
            if zapisany_klucz == klucz:
                return zapisana_wartosc

        return f"Klucz '{klucz}' nie istnieje w mapie."

    # -------------------------------------------------------------------------

    def wypisz(self) -> None:
        """Wypisuje zawartość wszystkich kubełków – metoda pomocnicza (gotowa)."""
        print("\n--- Zawartość mapy hashowej ---")
        for indeks, kubełek in enumerate(self.kubełki):
            if kubełek:
                print(f"  Kubełek [{indeks:2d}]: {kubełek}")
            else:
                print(f"  Kubełek [{indeks:2d}]: (pusty)")
        print("-------------------------------\n")


# =============================================================================
# DEMONSTRACJA – uruchom plik, aby zobaczyć działanie swojej implementacji
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 1 – Własna implementacja mapy hashowej")
    print("=" * 60)

    mapa = ProstaMapa(rozmiar=10)

    # --- Wstawianie par klucz-wartość ---
    print("\n[1] Wstawianie danych do mapy...")
    mapa.wstaw("imie",    "Aleksander")
    mapa.wstaw("nazwisko", "Kowalski")
    mapa.wstaw("wiek",    "23")
    mapa.wstaw("miasto",  "Kraków")
    mapa.wstaw("język",   "Python")
    # Klucze "ab" i "ba" mają ten sam hash – celowa kolizja do testów
    mapa.wstaw("ab",      "wartość_ab")
    mapa.wstaw("ba",      "wartość_ba")
    print("  Wstawiono 7 par (w tym jedna celowa kolizja: 'ab' i 'ba').")

    # --- Podgląd wewnętrznej struktury ---
    mapa.wypisz()

    # --- Pobieranie wartości ---
    print("[2] Pobieranie wartości:")
    print(f"  mapa.pobierz('imie')     -> {mapa.pobierz('imie')}")
    print(f"  mapa.pobierz('miasto')   -> {mapa.pobierz('miasto')}")
    print(f"  mapa.pobierz('ab')       -> {mapa.pobierz('ab')}")
    print(f"  mapa.pobierz('ba')       -> {mapa.pobierz('ba')}")
    print(f"  mapa.pobierz('brakujący')-> {mapa.pobierz('brakujący')}")

    # --- Aktualizacja istniejącego klucza ---
    print("\n[3] Aktualizacja klucza 'wiek' (23 -> 24):")
    mapa.wstaw("wiek", "24")
    print(f"  mapa.pobierz('wiek')     -> {mapa.pobierz('wiek')}")

    print("\n[Gotowe] Uzupełnij metody TODO i sprawdź, czy wyniki są poprawne.")
