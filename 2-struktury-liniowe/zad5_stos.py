# =============================================================================
# Zadanie 5 – Stos (Stack) – LIFO (Last In, First Out)
# =============================================================================
# OPIS PROBLEMU:
#   Implementujesz mechanizm „Cofnij" (Undo) w prostym edytorze tekstu.
#   Każda operacja wykonana przez użytkownika (wpisanie tekstu, usunięcie,
#   formatowanie) trafia na stos historii. Naciśnięcie Ctrl+Z zdejmuje
#   ostatnią operację ze stosu i cofa jej efekt.
#
#   Jako stos wykorzystujesz collections.deque, ponieważ
#   operacje append() i pop() działają na jej końcu w czasie O(1) –
#   dokładnie tak, jak push/pop na stosie.
#
#   Twoim zadaniem jest:
#     1. Wykonanie kilku operacji edytorskich (push na stos).
#     2. Podejrzenie ostatniej operacji bez jej usuwania (peek).
#     3. Cofnięcie ostatniej operacji (pop ze stosu).
#     4. Wyświetlenie całego stosu historii.
#
# METODY / OPERACJE do poznania:
#   - Tworzenie stosu:              from collections import deque; stos = deque()
#   - Odkładanie operacji (push):   stos.append(element)
#   - Zdejmowanie operacji (pop):   stos.pop()           – zwraca i usuwa wierzchołek
#   - Podgląd wierzchołka (peek):   stos[-1]             – bez usuwania
#   - Sprawdzanie czy pusty:        not stos  /  len(stos) == 0
#   - Długość stosu:                len(stos)
# =============================================================================

from collections import deque

# --- Stos historii operacji edytora -----------------------------------------
historia_operacji: deque[str] = deque()


# ============================================================
# FUNKCJA 1 – Wykonaj operację (push)
# ============================================================
def wykonaj_operacje(opis: str) -> None:
    """
    Odkłada `opis` wykonywanej operacji na wierzchołek stosu (push).
    """
    # TODO: 1. Dodaj `opis` na koniec (wierzchołek) `historia_operacji`
    #          za pomocą .append().
    #       2. Wypisz komunikat, np.:
    #          f"Wykonano: '{opis}'  [operacji na stosie: {len(historia_operacji)}]"
    historia_operacji.append(opis)
    print(f"Wykonano: '{opis}'  [operacji na stosie: {len(historia_operacji)}]")


# ============================================================
# FUNKCJA 2 – Cofnij (Undo / pop)
# ============================================================
def cofnij() -> None:
    """
    Zdejmuje ostatnią operację ze stosu (pop) i symuluje jej cofnięcie.
    Jeśli stos jest pusty, informuje o tym użytkownika.
    """
    # TODO: 1. Sprawdź, czy `historia_operacji` nie jest pusta.
    #          Jeśli jest pusta – wypisz "Brak operacji do cofnięcia."
    #       2. Jeśli nie jest pusta:
    #          a. Zdejmij ostatnią operację za pomocą .pop() i zapisz ją.
    #          b. Wypisz komunikat, np.:
    #             f"Cofnięto: '{operacja}'"
    #          c. Wypisz ile operacji pozostało:
    #             f"Pozostało na stosie: {len(historia_operacji)}"
    if not historia_operacji:
        print("Brak operacji do cofnięcia.")
    else:
        operacja = historia_operacji.pop()
        print(f"Cofnięto: '{operacja}'")
        print(f"Pozostało na stosie: {len(historia_operacji)}")


# ============================================================
# FUNKCJA 3 – Podejrzyj wierzchołek (peek)
# ============================================================
def podejrzyj_ostatnia() -> None:
    """
    Wypisuje ostatnią operację na stosie bez jej usuwania.
    Jeśli stos jest pusty, informuje o tym użytkownika.
    """
    # TODO: 1. Sprawdź, czy `historia_operacji` nie jest pusta.
    #          Jeśli jest pusta – wypisz "Stos jest pusty – brak operacji."
    #       2. Jeśli nie jest pusta, użyj indeksu [-1], aby odczytać
    #          wierzchołek stosu i wypisz, np.:
    #          f"Ostatnia operacja (peek): '{historia_operacji[-1]}'"
    if not historia_operacji:
        print("Stos jest pusty – brak operacji.")
    else:
        print(f"Ostatnia operacja (peek): '{historia_operacji[-1]}'")


# ============================================================
# FUNKCJA 4 – Wyświetl historię operacji
# ============================================================
def wyswietl_stos() -> None:
    """
    Wypisuje wszystkie operacje na stosie.
    Wierzchołek stosu (ostatnia operacja) jest na górze listy.
    """
    if not historia_operacji:
        print("Stos operacji jest pusty.")
        return

    print(f"Historia operacji ({len(historia_operacji)} szt.) – wierzchołek na górze:")
    # TODO: Iteruj po `historia_operacji` od końca (reversed(...)), aby
    #       wypisać najpierw najnowszą operację (wierzchołek stosu), np.:
    #         [TOP]  3. Usunięto słowo 'przykład'   ← (ostatnia)
    #                2. Wpisano tekst 'Hello World'
    #         [BOT]  1. Otwarto nowy dokument
    #       Wskazówka: enumerate(reversed(...), start=1) może się przydać.


    ile = len(historia_operacji)

    for nr, operacja in enumerate(reversed(historia_operacji), start=1):
        prawdziwy_nr = ile - nr + 1

        if nr == 1:
            print(f"[TOP]  {prawdziwy_nr}. {operacja}   ← (ostatnia)")
        elif nr == ile:
            print(f"[BOT]  {prawdziwy_nr}. {operacja}")
        else:
            print(f"       {prawdziwy_nr}. {operacja}")


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Mechanizm Cofnij / Undo (LIFO) ===\n")

    print("-- Wykonywanie operacji --")
    wykonaj_operacje("Otwarto nowy dokument")
    wykonaj_operacje("Wpisano tekst 'Hello World'")
    wykonaj_operacje("Zmieniono czcionkę na Bold")
    wykonaj_operacje("Usunięto słowo 'przykład'")
    wyswietl_stos()

    print("\n-- Podgląd wierzchołka (peek) --")
    podejrzyj_ostatnia()

    print("\n-- Cofnij (Undo) --")
    cofnij()
    wyswietl_stos()

    print("\n-- Cofnij jeszcze dwa razy --")
    cofnij()
    cofnij()
    wyswietl_stos()

    print("\n-- Cofnij ostatnią operację --")
    cofnij()

    print("\n-- Próba cofnięcia na pustym stosie --")
    cofnij()

