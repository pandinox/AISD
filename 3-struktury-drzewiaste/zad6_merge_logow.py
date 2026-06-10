# =============================================================================
# Zadanie 6 – Scalanie Logów z Wielu Serwerów (heapq.merge)
# =============================================================================
# OPIS PROBLEMU:
#   Pracujesz w zespole DevOps. Masz klaster 3 serwerów aplikacyjnych –
#   każdy produkuje logi zdarzeń posortowane chronologicznie.
#   Gdy dzieje się coś złego, musisz połączyć logi ze wszystkich serwerów
#   w jeden chronologiczny strumień, żeby zobaczyć pełny obraz sytuacji.
#
#   Naiwne podejście: wrzuć wszystko do jednej listy i posortuj – O(n log n).
#   Mądre podejście: użyj heapq.merge() – scala K posortowanych sekwencji
#   w jeden posortowany strumień w O(n log K), bez ładowania wszystkiego
#   do pamięci naraz (generator!).
#
#   Twoim zadaniem jest:
#     1. Scalenie logów z wielu serwerów w jeden chronologiczny strumień.
#     2. Filtrowanie logów po poziomie (INFO / WARNING / ERROR / CRITICAL).
#     3. Wypisanie N najnowszych wpisów (największy timestamp).
#
# METODY / OPERACJE do poznania:
#   - Scalanie posortowanych sekwencji: heapq.merge(*sekwencje)  – O(n log k)
#     Zwraca GENERATOR – nie listę! Użyj list(...) aby zmaterializować.
#   - N największych elementów:  heapq.nlargest(n, iterable, key=func) – O(n log k)
#   - Klucz sortowania:          key=lambda log: log.timestamp
#   - Porównywanie dataclass:    @dataclass(order=True) lub własny __lt__
#
# WAŻNE:
#   heapq.merge() zakłada, że KAŻDA wejściowa sekwencja jest już posortowana.
#   Jeśli podasz nieposortowane dane – wynik też będzie błędny (brak wyjątku!).
# =============================================================================

import heapq
import random
from dataclasses import dataclass, field


# =============================================================================
# MODEL DANYCH (dostarczony – nie musisz zmieniać)
# =============================================================================
POZIOMY = ["INFO", "WARNING", "ERROR", "CRITICAL"]

# Wagi dla generatora – realistyczny rozkład: głównie INFO, mało CRITICAL
_WAGI_POZIOMOW = [70, 20, 8, 2]


@dataclass(order=True)
class LogEntry:
    """
    Reprezentacja jednego wpisu logu.
    `order=True` sprawia, że Python automatycznie generuje metody porównania
    (<, >, ==) na podstawie kolejności pól – sortujemy głównie po `timestamp`.
    """
    timestamp: int          # Unix timestamp w sekundach (klucz sortowania)
    serwer: str = field(compare=False)   # Nazwa serwera (nie porównujemy)
    poziom: str = field(compare=False)   # INFO / WARNING / ERROR / CRITICAL
    komunikat: str = field(compare=False)  # Treść logu

    def __str__(self) -> str:
        return f"[{self.timestamp}] {self.serwer:<12} {self.poziom:<9} {self.komunikat}"


# =============================================================================
# FUNKCJE POMOCNICZE (dostarczone – nie musisz ich zmieniać)
# =============================================================================
def generuj_logi_serwera(nazwa: str, start_ts: int, ile: int, seed: int) -> list[LogEntry]:
    """
    Generuje `ile` wpisów logu dla serwera `nazwa`, zaczynając od `start_ts`.
    Logi są POSORTOWANE rosnąco po timestamp (wymagane przez heapq.merge).
    """
    rng = random.Random(seed)
    komunikaty = {
        "INFO":     ["Żądanie obsłużone", "Połączenie nawiązane", "Cache odświeżony",
                     "Użytkownik zalogowany", "Sesja wygasła"],
        "WARNING":  ["Wysokie użycie CPU (85%)", "Wolne zapytanie SQL (>2s)",
                     "Retry połączenia z DB", "Bufor kolejki zapełniony w 80%"],
        "ERROR":    ["Timeout połączenia z Redis", "Błąd parsowania JSON",
                     "Nieudana autentykacja", "Wyjątek NullPointerError"],
        "CRITICAL": ["Brak miejsca na dysku!", "Serwer bazy danych niedostępny",
                     "OOM Killer uruchomiony"],
    }
    logi = []
    ts = start_ts
    for _ in range(ile):
        ts += rng.randint(1, 15)          # losowy przyrost czasu (1–15 s)
        poziom = rng.choices(POZIOMY, weights=_WAGI_POZIOMOW)[0]
        komunikat = rng.choice(komunikaty[poziom])
        logi.append(LogEntry(ts, nazwa, poziom, komunikat))
    return logi   # już posortowane, bo timestamp rośnie


def _separator(tytul: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {tytul}")
    print('=' * 60)


# =============================================================================
# ZADANIE DO IMPLEMENTACJI
# =============================================================================

# ============================================================
# FUNKCJA 1 – Scal logi z wielu serwerów
# ============================================================
def scalaj_logi(*strumienie: list[LogEntry]) -> list[LogEntry]:
    """
    Scala dowolną liczbę posortowanych list logów w jeden
    posortowany chronologicznie strumień.

    Intuicja: heapq.merge() działa jak "zamek błyskawiczny" –
    trzyma wskaźnik na początek każdej listy i za każdym razem
    wybiera najmniejszy element (O(log K) na krok, gdzie K = liczba serwerów).
    Nie ładuje wszystkich logów do pamięci naraz – to generator!

    Złożoność czasowa:  O(n log K), gdzie n = łączna liczba logów, K = serwerów
    Złożoność pamięciowa: O(K) – tylko K wskaźników w kopcu
    """
    # TODO: Scal wszystkie strumienie w jeden posortowany chronologicznie strumień
    #       używając heapq.merge(). Pamiętaj, że wynik to generator —
    #       musisz go zmaterializować do listy.
    #       Wypisz ile strumieni i łącznie ile wpisów scalono. Zwróć listę.
    scalone = list(heapq.merge(*strumienie))

    print(f"Scalono {len(strumienie)} strumienie logów.")
    print(f"Łączna liczba wpisów: {len(scalone)}")

    return scalone


# ============================================================
# FUNKCJA 2 – Filtruj logi po poziomie
# ============================================================
def filtruj_bledy(logi: list[LogEntry], poziom: str) -> list[LogEntry]:
    """
    Zwraca tylko te logi, których poziom pasuje do podanego.
    Przydatne do szybkiego odfiltrowania np. tylko ERROR i CRITICAL.

    Intuicja: zwykłe filtrowanie listy – O(n). Nie wymaga kopca,
    ale często używamy tej funkcji razem ze scalonymi logami.

    Złożoność czasowa:  O(n)
    Złożoność pamięciowa: O(k), gdzie k = liczba pasujących wpisów
    """
    # TODO: Zwróć tylko wpisy pasujące do podanego poziomu.
    #       Wypisz ile wpisów znaleziono i zwróć listę.
    wynik = []

    for log in logi:
        if log.poziom == poziom:
            wynik.append(log)

    print(f"Znaleziono {len(wynik)} wpisów poziomu {poziom}.")

    return wynik


# ============================================================
# FUNKCJA 3 – N najnowszych wpisów
# ============================================================
def najnowsze_logi(logi: list[LogEntry], n: int) -> list[LogEntry]:
    """
    Zwraca n logów z NAJWIĘKSZYM timestamp (najnowsze zdarzenia).

    Intuicja: nlargest() z kluczem `key=lambda log: log.timestamp`
    wyciąga n elementów z największą wartością pola timestamp –
    bez sortowania całej listy.

    Złożoność czasowa:  O(n log k), gdzie k = n (żądana liczba wyników)
    Złożoność pamięciowa: O(k)
    """
    # TODO: Użyj heapq.nlargest() z kluczem sortowania po polu timestamp,
    #       aby pobrać n najnowszych wpisów. Wypisz je i zwróć listę.
    wynik = heapq.nlargest(n, logi, key=lambda log: log.timestamp)

    print(f"{n} najnowszych wpisów:")
    for log in wynik:
        print(f"  {log}")

    return wynik


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Monitoring klastra – scalanie logów (heapq.merge) ===\n")

    # --- Generujemy posortowane logi z każdego serwera ---
    # Serwery startują o różnych porach, żeby logi się przeplatały
    _separator("Generowanie logów z 3 serwerów")
    logi_web_01  = generuj_logi_serwera("web-01",  start_ts=1_700_000_000, ile=15, seed=1)
    logi_web_02  = generuj_logi_serwera("web-02",  start_ts=1_700_000_005, ile=15, seed=2)
    logi_db_01   = generuj_logi_serwera("db-01",   start_ts=1_700_000_003, ile=10, seed=3)

    print(f"  web-01 : {len(logi_web_01)} wpisów  "
          f"(od {logi_web_01[0].timestamp} do {logi_web_01[-1].timestamp})")
    print(f"  web-02 : {len(logi_web_02)} wpisów  "
          f"(od {logi_web_02[0].timestamp} do {logi_web_02[-1].timestamp})")
    print(f"  db-01  : {len(logi_db_01)} wpisów  "
          f"(od {logi_db_01[0].timestamp} do {logi_db_01[-1].timestamp})")

    # --- Krok 1: Scal logi ---
    _separator("Scalanie logów (heapq.merge)")
    wszystkie = scalaj_logi(logi_web_01, logi_web_02, logi_db_01)

    # --- Krok 2: Podgląd pierwszych 10 wpisów scalonych logów ---
    _separator("Pierwsze 10 wpisów scalonych logów (chronologicznie)")
    for log in wszystkie[:10]:
        print(f"  {log}")

    # --- Krok 3: Znajdź błędy ---
    _separator("Filtrowanie: tylko ERROR")
    bledy = filtruj_bledy(wszystkie, "ERROR")
    for log in bledy:
        print(f"  {log}")

    _separator("Filtrowanie: tylko CRITICAL")
    krytyczne = filtruj_bledy(wszystkie, "CRITICAL")
    for log in krytyczne:
        print(f"  {log}")
    if not krytyczne:
        print("  Brak wpisów CRITICAL – klaster działa stabilnie.")

    # --- Krok 4: Najnowsze logi ---
    _separator("5 najnowszych wpisów z klastra")
    najnowsze_logi(wszystkie, 5)

    # --- Krok 5: Najnowsze błędy ---
    _separator("3 najnowsze wpisy ERROR lub CRITICAL")
    powazne = [log for log in wszystkie if log.poziom in ("ERROR", "CRITICAL")]
    najnowsze_logi(powazne, 3)
