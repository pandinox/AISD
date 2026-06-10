# =============================================================================
# Zadanie 3 – SŁOWNIK (DICT) i ZBIÓR (SET) – Analityka logów sieciowych
# =============================================================================
# OPIS PROBLEMU:
#   Wyobraź sobie, że jesteś inżynierem bezpieczeństwa i otrzymujesz logi
#   z serwera WWW. Każdy wpis to adres IP klienta, który nawiązał połączenie.
#   Masz dwa zadania:
#     1. Znaleźć wszystkie UNIKALNE adresy IP (kto w ogóle się łączył?).
#     2. Policzyć, ile razy każdy adres IP wystąpił (kto łączył się najczęściej?).
#   Oba zadania można rozwiązać "brutalnie" zagnieżdżonymi pętlami – O(n²).
#   Struktury hashujące (set, dict) rozwiązują je elegancko w czasie O(n).
#
# METODY / OPERACJE do poznania:
#   - set()                        – znajdowanie unikalnych wartości w O(n)
#   - dict.get(klucz, domyślna)    – bezpieczne odczytywanie z domyślną wartością
#   - dict[klucz] = wartość        – wstawianie / aktualizacja w O(1)
#   - sorted(..., key=..., reverse=True) – sortowanie wg wartości słownika
# =============================================================================

import random

# =============================================================================
# PRZYGOTOWANIE DANYCH – kod gotowy, nie modyfikuj tej sekcji
# =============================================================================

# Pula adresów IP – celowo mała (200 adresów), by wymuszać powtórzenia w logach
random.seed(7)
PULA_ADRESOW_IP = [
    f"192.168.{random.randint(0, 9)}.{random.randint(1, 254)}"
    for _ in range(200)
]


def generuj_logi(liczba_wpisow: int = 50_000) -> list[str]:
    """
    Generuje symulowane logi serwera jako listę adresów IP.
    Adresy są losowane z małej puli, więc wiele z nich się powtarza.

    Args:
        liczba_wpisow: ile wpisów logów wygenerować (domyślnie 50 000)

    Returns:
        lista adresów IP (str) – może zawierać powtórzenia
    """
    return [random.choice(PULA_ADRESOW_IP) for _ in range(liczba_wpisow)]


# =============================================================================
# FUNKCJE DO UZUPEŁNIENIA
# =============================================================================

def unikalne_ip(lista_logow: list[str]) -> set[str] | None:  # type: ignore[return]
    """
    Zwraca zbiór unikalnych adresów IP obecnych w logach.

    Użyj struktury set – automatycznie eliminuje duplikaty.

    Args:
        lista_logow: lista adresów IP (może zawierać duplikaty)

    Returns:
        zbiór (set) zawierający każdy adres IP dokładnie raz
    """
    # TODO: Przekształć listę lista_logow na zbiór (set) i zwróć wynik.
    return set(lista_logow)


def licznik_wystapien(lista_logow: list[str]) -> dict[str, int]:
    """
    Zlicza, ile razy każdy adres IP pojawił się w logach.

    Użyj słownika (dict): klucz = adres IP, wartość = liczba wystąpień.

    Args:
        lista_logow: lista adresów IP (może zawierać duplikaty)

    Returns:
        słownik {adres_ip: liczba_wystapien}
    """
    licznik: dict[str, int] = {}

    # TODO: Dla każdego ip zlicz ile razy pojawił się w logach
    #       Wskazówka: użyj licznik.get(ip, 0) aby bezpiecznie
    #       odczytać aktualną wartość lub 0, gdy klucz jeszcze nie istnieje.
    for ip in lista_logow:
        licznik[ip] = licznik.get(ip, 0) + 1

    return licznik


def top_adresow(licznik: dict[str, int], ile: int = 10) -> list[tuple[str, int]]:
    """
    Zwraca listę 'ile' najczęściej pojawiających się adresów IP.
    Metoda pomocnicza – gotowa, nie modyfikuj.

    Args:
        licznik: słownik {adres_ip: liczba_wystapien}
        ile:     liczba adresów do zwrócenia (domyślnie 10)

    Returns:
        lista krotek (adres_ip, liczba_wystapien) posortowana malejąco
    """
    posortowane = sorted(licznik.items(), key=lambda para: para[1], reverse=True)
    return posortowane[:ile]


def wypisz_raport(logi: list[str], unikalne: set[str] | None,
                  licznik: dict[str, int] | None) -> None:
    """
    Wypisuje sformatowany raport z analizy logów.
    Metoda pomocnicza – gotowa, nie modyfikuj.
    """
    print("\n" + "=" * 60)
    print("  RAPORT ANALIZY LOGÓW SIECIOWYCH")
    print("=" * 60)
    print(f"  Łączna liczba wpisów w logach : {len(logi):>8,}")

    if unikalne is None:
        print("  Unikalne adresy IP            :  [!] uzupełnij unikalne_ip()")
    else:
        print(f"  Unikalne adresy IP            : {len(unikalne):>8,}")

    if licznik is None or len(licznik) == 0:
        print("  Licznik wystąpień             :  [!] uzupełnij licznik_wystapien()")
        print("=" * 60)
        return

    print("-" * 60)
    print("  TOP 10 najczęstszych adresów IP:")
    print(f"  {'Adres IP':<22} {'Liczba połączeń':>15}")
    print(f"  {'-' * 22} {'-' * 15}")
    for adres, liczba in top_adresow(licznik, ile=10):
        print(f"  {adres:<22} {liczba:>15,}")
    print("=" * 60)
    print()
    print("  Wniosek:")
    print("  Słownik pozwolił policzyć 50 000 wpisów w jednym")
    print("  przebiegu pętli (O(n)) zamiast zagnieżdżonych pętli O(n²).")
    print("  To różnica między milisekundami a sekundami!")
    print("=" * 60)


# =============================================================================
# DEMONSTRACJA – uruchom plik, aby zobaczyć wyniki analizy logów
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 3 – Analityka logów sieciowych")
    print("=" * 60)

    print("\n  [>>] Generuję 50 000 wpisów logów...")
    logi_serwera = generuj_logi(50_000)
    print(f"  Przykładowe wpisy: {logi_serwera[:5]}")

    print("\n  [>>] Szukam unikalnych adresów IP...")
    wynik_unikalnych = unikalne_ip(logi_serwera)

    print("  [>>] Zliczam wystąpienia każdego adresu IP...")
    wynik_licznika = licznik_wystapien(logi_serwera)

    wypisz_raport(logi_serwera, wynik_unikalnych, wynik_licznika)
