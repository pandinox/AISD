# =============================================================================
# Zadanie 4 – Słownik (Dict) – Baza Synonimów
# =============================================================================
# OPIS PROBLEMU:
#   Tworzysz narzędzie wspomagające pracę copywritera. Program przechowuje
#   słowa oraz przypisane do nich listy synonimów.
#   Użycie słownika (hashmapy) pozwala na błyskawiczne odnalezienie
#   zamienników nawet przy bardzo dużej bazie haseł.
#
# METODY / OPERACJE do poznania:
#   - slownik[klucz] = wartosc       – dodawanie / aktualizacja wartości
#   - slownik.get(klucz, default)    – bezpieczne pobieranie z wartością domyślną
#   - slownik.setdefault(klucz, [])  – inicjalizacja brakującego klucza listą
#   - del slownik[klucz]             – usuwanie klucza wraz z wartością
#   - klucz in slownik               – sprawdzenie istnienia klucza
#   - len(slownik)                   – liczba kluczy w słowniku
# =============================================================================


# Globalna baza synonimów:
#   klucz  -> słowo bazowe (str)
#   wartość -> lista synonimów (list[str])
baza_synonimow: dict[str, list[str]] = {}


# =============================================================================
# FUNKCJE DO UZUPEŁNIENIA
# =============================================================================

def dodaj_synonim(slowo: str, synonim: str) -> None:
    """
    Dodaje synonim do podanego słowa w bazie.
    Jeśli słowo nie istnieje w słowniku, zostaje automatycznie utworzone.
    Nie dodaje duplikatów – ten sam synonim może wystąpić tylko raz.

    Args:
        slowo:   słowo bazowe (klucz w słowniku)
        synonim: synonim do dodania

    Przykład:
        dodaj_synonim("szybki", "prędki")
        dodaj_synonim("szybki", "błyskawiczny")
        # baza_synonimow["szybki"] == ["prędki", "błyskawiczny"]

    Wskazówka:
        Użyj metody baza_synonimow.setdefault(slowo, []) – zwraca ona
        istniejącą listę lub tworzy pustą, gdy klucz nie istnieje.
        Alternatywnie możesz sprawdzić: if slowo not in baza_synonimow.
    """
    # TODO: 1. Upewnij się, że klucz 'slowo' istnieje w baza_synonimow
    #          (użyj .setdefault() lub instrukcji if/not in).
    # TODO: 2. Sprawdź, czy 'synonim' nie znajduje się już na liście
    #          (unikamy duplikatów).
    # TODO: 3. Jeśli synonim jest nowy – dołącz go do listy (.append()).
    lista = baza_synonimow.setdefault(slowo, [])

    if synonim not in lista:
        lista.append(synonim)


def znajdz_synonimy(slowo: str) -> list[str] | str | None:  # type: ignore[return]
    """
    Zwraca listę synonimów dla podanego słowa.
    Jeśli słowo nie istnieje w bazie, zwraca czytelny komunikat.

    Args:
        slowo: szukane słowo bazowe

    Returns:
        lista synonimów (list[str]) lub komunikat o braku słowa (str)

    Przykład:
        znajdz_synonimy("szybki")  ->  ["prędki", "błyskawiczny"]
        znajdz_synonimy("wolny")   ->  "Słowo 'wolny' nie istnieje w bazie."

    Wskazówka:
        Użyj metody baza_synonimow.get(slowo) i sprawdź wynik,
        lub skorzystaj z operatora `in` przed bezpośrednim dostępem.
    """
    # TODO: 1. Sprawdź, czy 'slowo' istnieje w baza_synonimow.
    # TODO: 2. Jeśli tak – zwróć przypisaną listę synonimów.
    # TODO: 3. Jeśli nie – zwróć napis: f"Słowo '{slowo}' nie istnieje w bazie."
    if slowo in baza_synonimow:
        return baza_synonimow[slowo]

    return f"Słowo '{slowo}' nie istnieje w bazie."


def usun_slowo(slowo: str) -> None:
    """
    Usuwa słowo wraz ze wszystkimi jego synonimami z bazy.
    Jeśli słowo nie istnieje, wypisuje stosowny komunikat (nie rzuca wyjątku).

    Args:
        slowo: słowo bazowe do usunięcia

    Przykład:
        usun_slowo("szybki")
        # baza_synonimow nie zawiera już klucza "szybki"

    Wskazówka:
        Użyj instrukcji `del baza_synonimow[slowo]` wewnątrz bloku
        warunkowego sprawdzającego wcześniej, czy klucz istnieje.
    """
    # TODO: 1. Sprawdź, czy 'slowo' istnieje w baza_synonimow.
    # TODO: 2. Jeśli tak – usuń je za pomocą `del` i wypisz potwierdzenie.
    # TODO: 3. Jeśli nie – wypisz komunikat: f"Słowo '{slowo}' nie istnieje w bazie."
    if slowo in baza_synonimow:
        del baza_synonimow[slowo]
        print(f"Usunięto słowo '{slowo}' z bazy.")
    else:
        print(f"Słowo '{slowo}' nie istnieje w bazie.")


def wyswietl_statystyki() -> None:
    """
    Wypisuje statystyki bazy synonimów:
      - łączną liczbę słów (kluczy) w bazie,
      - łączną liczbę wszystkich przechowywanych synonimów (suma długości list).

    Przykład wydruku:
        Statystyki bazy synonimów:
          Liczba słów w bazie    :   5
          Łączna liczba synonimów:  17

    Wskazówka:
        Liczbę kluczy odczytasz przez len(baza_synonimow).
        Łączną liczbę synonimów możesz policzyć funkcją sum() z wyrażeniem
        generatorowym: sum(len(lista) for lista in baza_synonimow.values()).
    """
    # TODO: 1. Oblicz liczbę słów: len(baza_synonimow).
    # TODO: 2. Oblicz łączną liczbę synonimów przy użyciu sum() i .values().
    # TODO: 3. Wypisz obie wartości w czytelnym formacie.
    liczba_slow = len(baza_synonimow)
    liczba_synonimow = sum(len(lista) for lista in baza_synonimow.values())

    print("Statystyki bazy synonimów:")
    print(f"  Liczba słów w bazie    : {liczba_slow}")
    print(f"  Łączna liczba synonimów: {liczba_synonimow}")


# =============================================================================
# DEMONSTRACJA – uruchom plik, aby zobaczyć działanie po uzupełnieniu TODO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 4 – Baza Synonimów (słownik / hashmap)")
    print("=" * 60)

    # --- Dodawanie synonimów ---
    print("\n[1] Dodawanie synonimów do bazy...")
    dodaj_synonim("szybki",   "prędki")
    dodaj_synonim("szybki",   "błyskawiczny")
    dodaj_synonim("szybki",   "żwawy")
    dodaj_synonim("duży",     "wielki")
    dodaj_synonim("duży",     "ogromny")
    dodaj_synonim("duży",     "potężny")
    dodaj_synonim("mądry",    "inteligentny")
    dodaj_synonim("mądry",    "rozumny")
    dodaj_synonim("piękny",   "śliczny")
    dodaj_synonim("piękny",   "czarowny")
    dodaj_synonim("smutny",   "przygnębiony")
    # Próba dodania duplikatu – nie powinno nic zmienić
    dodaj_synonim("szybki",   "prędki")
    print("  Dodano synonimy dla słów: szybki, duży, mądry, piękny, smutny.")
    print("  (Próba dodania duplikatu 'prędki' dla 'szybki' – powinna być zignorowana.)")

    # --- Wyszukiwanie synonimów ---
    print("\n[2] Wyszukiwanie synonimów:")
    print(f"  znajdz_synonimy('szybki') -> {znajdz_synonimy('szybki')}")
    print(f"  znajdz_synonimy('duży')   -> {znajdz_synonimy('duży')}")
    print(f"  znajdz_synonimy('wolny')  -> {znajdz_synonimy('wolny')}")

    # --- Statystyki przed usunięciem ---
    print("\n[3] Statystyki bazy przed usunięciem słowa:")
    wyswietl_statystyki()

    # --- Usuwanie słowa ---
    print("\n[4] Usuwanie słowa 'smutny' z bazy...")
    usun_slowo("smutny")
    print("  Próba usunięcia nieistniejącego słowa 'wesoły':")
    usun_slowo("wesoły")

    # --- Statystyki po usunięciu ---
    print("\n[5] Statystyki bazy po usunięciu słowa:")
    wyswietl_statystyki()

    print("\n[Gotowe] Uzupełnij metody TODO i sprawdź, czy wyniki są zgodne z oczekiwaniami.")
