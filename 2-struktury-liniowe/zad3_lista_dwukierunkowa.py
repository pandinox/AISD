# =============================================================================
# Zadanie 3 – Lista dwukierunkowa (Doubly Linked List)
# =============================================================================
# OPIS PROBLEMU:
#   Symulujesz historię przeglądania stron w przeglądarce internetowej.
#   Przeglądarka przechowuje listę odwiedzonych adresów URL i pozwala
#   użytkownikowi cofać się (Wstecz) oraz iść do przodu (Dalej).
#
#   Jako strukturę danych wykorzystujesz collections.deque, która jest
#   Pythonową implementacją listy dwukierunkowej – umożliwia wydajne
#   dodawanie i usuwanie elementów z OBU końców w czasie O(1).
#
#   Twoim zadaniem jest:
#     1. Odwiedzenie kilku stron (dodawanie do historii).
#     2. Cofnięcie się o jedną stronę (operacja „Wstecz").
#     3. Przejście do przodu o jedną stronę (operacja „Dalej").
#     4. Wyświetlenie całej historii z zaznaczeniem aktualnej strony.
#
# METODY / OPERACJE do poznania:
#   - Tworzenie deque:              from collections import deque; d = deque()
#   - Dodawanie na prawy koniec:    d.append(element)         – odwiedź stronę
#   - Dodawanie na lewy koniec:     d.appendleft(element)
#   - Usuwanie z prawego końca:     d.pop()                   – cofnij (Wstecz)
#   - Usuwanie z lewego końca:      d.popleft()               – Dalej (z bufora)
#   - Długość:                      len(d)
#   - Podgląd ostatniego elementu:  d[-1]
#   - Podgląd pierwszego elementu:  d[0]
# =============================================================================

from collections import deque

# --- Historia stron: strony odwiedzone do tej pory --------------------------
historia: deque[str] = deque()

# --- Bufor „Dalej": strony, które można jeszcze odwiedzić ponownie ----------
# Gdy cofasz się (Wstecz), bieżąca strona trafia do bufora_dalej.
# Gdy odwiedzasz nową stronę, bufor jest czyszczony.
bufor_dalej: deque[str] = deque()


# ============================================================
# FUNKCJA 1 – Odwiedź stronę
# ============================================================
def odwiedz_strone(url: str) -> None:
    """
    Dodaje `url` jako nową bieżącą stronę.
    Odwiedzenie nowej strony kasuje bufor „Dalej"
    (tak jak w prawdziwej przeglądarce).
    """
    # TODO: 1. Dodaj `url` na prawy koniec `historia` za pomocą .append().
    #       2. Wyczyść `bufor_dalej` za pomocą .clear() – nowa gałąź historii
    #          usuwa możliwość przejścia „Dalej".
    #       3. Wypisz komunikat, np.: f"Otwarto: {url}"
    historia.append(url)
    bufor_dalej.clear()
    print(f"Otwarto: {url}")


# ============================================================
# FUNKCJA 2 – Cofnij (Wstecz)
# ============================================================
def cofnij() -> None:
    """
    Cofa się o jedną stronę w historii.
    Bieżąca strona jest przenoszona do bufora_dalej.
    Jeśli historia ma tylko jedną stronę, cofnięcie nie jest możliwe.
    """
    # TODO: 1. Sprawdź, czy len(historia) > 1.
    #          Jeśli nie – wypisz "Nie można cofnąć – to pierwsza strona."
    #       2. Jeśli tak:
    #          a. Usuń ostatni element z `historia` za pomocą .pop() i zapisz go.
    #          b. Dodaj ten element na lewy koniec `bufor_dalej` za pomocą
    #             .appendleft() (zachowujemy kolejność do odtworzenia).
    #          c. Wypisz komunikat, np.: f"Cofnięto do: {historia[-1]}"
    if len(historia) > 1:
        obecna = historia.pop()
        bufor_dalej.appendleft(obecna)
        print(f"Cofnięto do: {historia[-1]}")
    else:
        print("Nie można cofnąć – to pierwsza strona.")


# ============================================================
# FUNKCJA 3 – Dalej (Naprzód)
# ============================================================
def dalej() -> None:
    """
    Przechodzi do przodu o jedną stronę (jeśli bufor_dalej nie jest pusty).
    """
    # TODO: 1. Sprawdź, czy bufor_dalej nie jest pusty (użyj len() lub bool).
    #          Jeśli pusty – wypisz "Brak stron do przejścia dalej."
    #       2. Jeśli nie jest pusty:
    #          a. Pobierz pierwszy element z `bufor_dalej` za pomocą .popleft().
    #          b. Dodaj go na prawy koniec `historia` za pomocą .append().
    #          c. Wypisz komunikat, np.: f"Przejście do: {historia[-1]}"
    if bufor_dalej:
        strona = bufor_dalej.popleft()
        historia.append(strona)
        print(f"Przejście do: {historia[-1]}")
    else:
        print("Brak stron do przejścia dalej.")


# ============================================================
# FUNKCJA 4 – Wyświetl historię
# ============================================================
def wyswietl_historie() -> None:
    """
    Wypisuje całą historię przeglądania.
    Aktualnie otwarta strona jest oznaczona symbolem '>>'.
    """
    if not historia:
        print("Historia jest pusta.")
        return

    print("Historia przeglądania:")
    # TODO: Iteruj po `historia`. Dla każdej strony:
    #       - jeśli jest to ostatni element (historia[-1]), wypisz ją ze strzałką:
    #           f"  >> {url}  ← (bieżąca)"
    #       - w przeciwnym razie:
    #           f"     {url}"
    if not historia:
        print("Historia jest pusta.")
        return

    print("Historia przeglądania:")

    for url in historia:
        if url == historia[-1]:
            print(f"  >> {url}  ← (bieżąca)")
        else:
            print(f"     {url}")

    if bufor_dalej:
        print("  (można przejść Dalej do:", bufor_dalej[0], ")")


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Symulacja historii przeglądarki ===\n")

    odwiedz_strone("https://google.com")
    odwiedz_strone("https://wikipedia.org")
    odwiedz_strone("https://python.org")
    wyswietl_historie()

    print("\n-- Cofnij (Wstecz) --")
    cofnij()
    wyswietl_historie()

    print("\n-- Cofnij jeszcze raz --")
    cofnij()
    wyswietl_historie()

    print("\n-- Próba cofnięcia z pierwszej strony --")
    cofnij()

    print("\n-- Dalej (Naprzód) --")
    dalej()
    wyswietl_historie()

    print("\n-- Odwiedź nową stronę (kasuje bufor Dalej) --")
    odwiedz_strone("https://github.com")
    wyswietl_historie()

    print("\n-- Próba przejścia Dalej po nowej stronie --")
    dalej()

