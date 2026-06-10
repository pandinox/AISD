# =============================================================================
# Zadanie 4 – Kolejka (Queue) – FIFO (First In, First Out)
# =============================================================================
# OPIS PROBLEMU:
#   Symulujesz kolejkę zadań drukowania w biurowej drukarce sieciowej.
#   Każdy pracownik może wysłać dokument do druku – trafia on na koniec
#   kolejki. Drukarka obsługuje zadania w kolejności ich nadsyłania:
#   pierwsze przysłane = pierwsze wydrukowane (FIFO).
#
#   Twoim zadaniem jest:
#     1. Dodanie kilku dokumentów do kolejki drukowania.
#     2. Wydrukowanie (przetworzenie) dokumentów jeden po drugim, w kolejności.
#     3. Sprawdzenie, ile dokumentów oczekuje w kolejce.
#     4. Wyświetlenie całej kolejki bez jej modyfikowania.
#
# METODY / OPERACJE do poznania:
#   - Tworzenie kolejki:            from collections import deque; q = deque()
#   - Dodawanie na koniec (enqueue): kolejka.append(element)
#   - Pobieranie z początku (dequeue): kolejka.popleft()
#   - Podgląd pierwszego elementu:  kolejka[0]
#   - Sprawdzanie długości:         len(kolejka)
#   - Sprawdzanie czy pusta:        not kolejka  /  len(kolejka) == 0
# =============================================================================

from collections import deque

# --- Inicjalizacja pustej kolejki drukowania --------------------------------
kolejka_drukowania: deque[str] = deque()


# ============================================================
# FUNKCJA 1 – Dodaj dokument do kolejki
# ============================================================
def dodaj_dokument(nazwa: str) -> None:
    """
    Dodaje `nazwa` dokumentu na koniec kolejki drukowania (enqueue).
    """
    # TODO: 1. Dodaj `nazwa` na koniec `kolejka_drukowania` za pomocą .append().
    #       2. Wypisz komunikat, np.:
    #          f"Dodano do kolejki: '{nazwa}'  [pozycja: {len(kolejka_drukowania)}]"
    kolejka_drukowania.append(nazwa)
    print(f"Dodano do kolejki: '{nazwa}'  [pozycja: {len(kolejka_drukowania)}]")


# ============================================================
# FUNKCJA 2 – Wydrukuj następny dokument
# ============================================================
def drukuj_nastepny() -> None:
    """
    Pobiera i przetwarza (drukuje) pierwszy dokument z kolejki (dequeue).
    Jeśli kolejka jest pusta, informuje o tym użytkownika.
    """
    # TODO: 1. Sprawdź, czy `kolejka_drukowania` nie jest pusta (użyj not lub len).
    #          Jeśli jest pusta – wypisz "Kolejka drukowania jest pusta."
    #       2. Jeśli nie jest pusta:
    #          a. Pobierz dokument z początku kolejki za pomocą .popleft().
    #          b. Wypisz komunikat, np.:
    #             f"Drukowanie: '{dokument}'..."
    #          c. Wypisz ile dokumentów pozostało:
    #             f"Pozostało w kolejce: {len(kolejka_drukowania)}"
    if not kolejka_drukowania:
        print(f"Kolejka drukowania jest pusta.")
    else:
        dokument = kolejka_drukowania.popleft()
        print(f"Drukowanie: '{dokument}'...")
        print(f"Pozostało w kolejce: {len(kolejka_drukowania)}")


# ============================================================
# FUNKCJA 3 – Sprawdź rozmiar kolejki
# ============================================================
def ile_dokumentow() -> int:
    """
    Zwraca liczbę dokumentów oczekujących w kolejce.
    """
    # TODO: Zwróć len(kolejka_drukowania).
    return len(kolejka_drukowania)


# ============================================================
# FUNKCJA 4 – Wyświetl kolejkę drukowania
# ============================================================
def wyswietl_kolejke() -> None:
    """
    Wypisuje wszystkie dokumenty oczekujące w kolejce,
    bez ich usuwania. Pierwszy na liście = następny do druku.
    """
    if not kolejka_drukowania:
        print("Kolejka drukowania jest pusta.")
        return

    print(f"Kolejka drukowania ({len(kolejka_drukowania)} dok.):")
    # TODO: Użyj enumerate(kolejka_drukowania, start=1), aby wypisać
    #       każdy dokument z jego pozycją w kolejce, np.:
    #         1. raport_kwartalny.pdf   ← (następny)
    #         2. prezentacja.pptx
    #         3. faktura_042.pdf
    #       Wskazówka: pozycja 1 oznacza "następny do druku".
    for pozycja, dokument in enumerate(kolejka_drukowania, start=1):
        if pozycja == 1:
            print(f"{pozycja}. {dokument}   ← (następny)")
        else:
            print(f"{pozycja}. {dokument}")


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Kolejka drukowania (FIFO) ===\n")

    print("-- Dodawanie dokumentów --")
    dodaj_dokument("raport_kwartalny.pdf")
    dodaj_dokument("prezentacja.pptx")
    dodaj_dokument("faktura_042.pdf")
    dodaj_dokument("umowa_serwisowa.docx")
    wyswietl_kolejke()

    print(f"\nDokumentów w kolejce: {ile_dokumentow()}")

    print("\n-- Drukowanie dokumentów --")
    drukuj_nastepny()
    drukuj_nastepny()
    wyswietl_kolejke()

    print("\n-- Drukowanie pozostałych --")
    drukuj_nastepny()
    drukuj_nastepny()

    print("\n-- Próba drukowania z pustej kolejki --")
    drukuj_nastepny()

