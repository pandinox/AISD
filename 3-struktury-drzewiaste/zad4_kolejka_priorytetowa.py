# =============================================================================
# Zadanie 4 – Kolejka Priorytetowa (Priority Queue / Min-Heap)
# =============================================================================
# OPIS PROBLEMU:
#   Jesteś programistą w firmie i obsługujesz helpdesk IT.
#   Codziennie wpływają zgłoszenia od pracowników – od drobnych próśb
#   ("zmień mi tło tapety") po poważne awarie ("serwer produkcyjny nie żyje!").
#   Musisz obsługiwać zgłoszenia wg priorytetu, a nie kolejności zgłoszenia.
#
#   Standardowa lista czy deque nie nadają się tutaj – za każdym razem
#   musiałbyś szukać elementu z najwyższym priorytetem (O(n)).
#   Kopiec (heap) rozwiązuje ten problem: zawsze wiesz, kto jest na szczycie,
#   a dodawanie i pobieranie kosztuje tylko O(log n).
#
#   Twoim zadaniem jest:
#     1. Dodawanie nowego zgłoszenia do kolejki.
#     2. Obsłużenie (pobranie) najważniejszego zgłoszenia.
#     3. Podgląd całej kolejki bez jej niszczenia.
#
# METODY / OPERACJE do poznania:
#   - Import:                    import heapq
#   - Pusta kolejka:             kolejka = []          – zwykła lista Pythona!
#   - Dodaj element:             heapq.heappush(kolejka, element)   – O(log n)
#   - Pobierz najm. element:     heapq.heappop(kolejka)             – O(log n)
#   - Podgląd szczytu (bez pop): kolejka[0]                         – O(1)
#   - Rozmiar:                   len(kolejka)
#   - Sprawdź czy pusta:         not kolejka   lub   len(kolejka) == 0
#
# WAŻNE – jak działa heapq w Pythonie?
#   heapq implementuje MIN-HEAP: element z NAJMNIEJSZĄ wartością jest na szczycie.
#   Priorytet 1 = najważniejszy, priorytet 5 = najmniej pilny.
#   Gdy element to krotka (priorytet, dane), Python porównuje najpierw priorytet.
# =============================================================================

import heapq

# Typ reprezentujący zgłoszenie: (priorytet: int, id: int, opis: str)
# Używamy `id` jako drugiego pola, żeby uniknąć błędu porównania stringów
# gdy dwa zgłoszenia mają ten sam priorytet (Python próbuje wtedy porównać
# kolejne pole krotki – bez `id` porównywałby stringi opisu, co może się nie udać).
Zgloszenie = tuple[int, int, str]


# ============================================================
# FUNKCJA 1 – Dodaj zgłoszenie
# ============================================================
def dodaj_zgloszenie(kolejka: list, priorytet: int, id_zgloszenia: int, opis: str) -> None:
    """
    Dodaje nowe zgłoszenie do kolejki priorytetowej.

    Intuicja: wrzucamy krotkę (priorytet, id, opis) do kopca.
    heapq zadba o to, żeby najważniejsze zgłoszenie (najmniejszy priorytet)
    zawsze było dostępne jako pierwszy element listy.

    Złożoność czasowa:  O(log n) – kopiec "przesiewa" nowy element w górę
    Złożoność pamięciowa: O(1) – nie tworzymy nowych struktur
    """
    # TODO: Dodaj zgłoszenie jako krotkę do kopca używając heapq.heappush().
    #       Wypisz potwierdzenie dodania.
    zgloszenie = (priorytet, id_zgloszenia, opis)
    heapq.heappush(kolejka, zgloszenie)
    print(f"Dodano zgłoszenie #{id_zgloszenia}: '{opis}' [priorytet: {priorytet}]")


# ============================================================
# FUNKCJA 2 – Obsłuż zgłoszenie
# ============================================================
def obsluz_zgloszenie(kolejka: list) -> Zgloszenie | None:
    """
    Pobiera i zwraca zgłoszenie o NAJWYŻSZYM priorytecie (najniższa liczba).
    Jeśli kolejka jest pusta, zwraca None i wypisuje stosowny komunikat.

    Intuicja: heappop() zawsze oddaje element ze szczytu kopca (minimum),
    a następnie reorganizuje strukturę, żeby nowe minimum znalazło się na górze.

    Złożoność czasowa:  O(log n) – "przesiewanie" w dół po usunięciu szczytu
    Złożoność pamięciowa: O(1)
    """
    # TODO: Obsłuż przypadek pustej kolejki – zwróć None z komunikatem.
    #       Pobierz najważniejsze zgłoszenie z kopca za pomocą heapq.heappop(),
    #       wypisz komunikat o obsłużeniu i zwróć krotkę.
    if not kolejka:
        print("Brak zgłoszeń do obsłużenia.")
        return None

    zgloszenie = heapq.heappop(kolejka)
    priorytet, id_zgloszenia, opis = zgloszenie

    print(f"Obsłużono zgłoszenie #{id_zgloszenia}: '{opis}' [priorytet: {priorytet}]")
    return zgloszenie


# ============================================================
# FUNKCJA 3 – Wyświetl kolejkę
# ============================================================
def wyswietl_kolejke(kolejka: list) -> None:
    """
    Wypisuje wszystkie zgłoszenia w kolejce BEZ ich usuwania.
    Uwaga: lista kopca NIE jest w pełni posortowana wizualnie –
    gwarantuje tylko, że kolejka[0] jest minimum (własność kopca).
    Żeby wypisać w kolejności priorytetu, musimy posortować kopię.

    Złożoność czasowa:  O(n log n) – sortowanie kopii
    Złożoność pamięciowa: O(n) – tworzymy kopię listy
    """
    # TODO: Obsłuż przypadek pustej kolejki.
    #       Pamiętaj – lista kopca nie jest posortowana wizualnie, więc do
    #       wyświetlenia w kolejności priorytetu potrzebujesz posortowanej kopii
    #       (nie niszcz oryginalnego kopca!). Wypisz wszystkie zgłoszenia.
    if not kolejka:
        print("Kolejka zgłoszeń jest pusta.")
        return

    print(f"Kolejka zgłoszeń ({len(kolejka)} szt.):")

    kopia = sorted(kolejka)

    for pozycja, zgloszenie in enumerate(kopia, start=1):
        priorytet, id_zgloszenia, opis = zgloszenie
        print(f"{pozycja}. #{id_zgloszenia} [priorytet: {priorytet}] {opis}")


# =============================================================================
# FUNKCJE POMOCNICZE (dostarczone – nie musisz ich zmieniać)
# =============================================================================
def _separator(tytul: str) -> None:
    """Drukuje czytelny separator sekcji w demo."""
    print(f"\n{'=' * 50}")
    print(f"  {tytul}")
    print('=' * 50)


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Helpdesk IT – Kolejka Priorytetowa ===\n")

    kolejka_it: list = []

    # --- Napływają zgłoszenia w losowej kolejności ---
    _separator("Dodawanie zgłoszeń")
    dodaj_zgloszenie(kolejka_it, 3, 1, "Drukarka w sali 204 nie działa")
    dodaj_zgloszenie(kolejka_it, 1, 2, "AWARIA: serwer bazy danych nie odpowiada")
    dodaj_zgloszenie(kolejka_it, 5, 3, "Prośba o zmianę tapety pulpitu")
    dodaj_zgloszenie(kolejka_it, 2, 4, "Klient VIP nie może się zalogować do CRM")
    dodaj_zgloszenie(kolejka_it, 4, 5, "Brak dostępu do drukarki sieciowej")
    dodaj_zgloszenie(kolejka_it, 1, 6, "AWARIA: strona www zwraca błąd 500")

    # --- Podgląd stanu kolejki ---
    _separator("Stan kolejki (wszystkie zgłoszenia)")
    wyswietl_kolejke(kolejka_it)

    # --- Technik zaczyna obsługę ---
    _separator("Obsługa zgłoszeń (od najważniejszych)")
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)

    # --- Podgląd po obsłudze 3 zgłoszeń ---
    _separator("Stan kolejki po obsłudze 3 zgłoszeń")
    wyswietl_kolejke(kolejka_it)

    # --- Obsłuż pozostałe ---
    _separator("Obsługa pozostałych zgłoszeń")
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)

    # --- Próba obsługi pustej kolejki ---
    _separator("Próba obsługi pustej kolejki")
    obsluz_zgloszenie(kolejka_it)
