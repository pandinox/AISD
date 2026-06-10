# =============================================================================
# Zadanie 2 – Lista (List) – dynamiczna struktura danych
# =============================================================================
# OPIS PROBLEMU:
#   Tworzysz prostą aplikację do zarządzania listą zakupów.
#   Lista jest dynamiczna – możesz w każdej chwili dodawać nowe produkty,
#   usuwać wybrane oraz sortować całą listę alfabetycznie.
#
#   Twoim zadaniem jest:
#     1. Dodanie kilku produktów do listy zakupów.
#     2. Sprawdzenie, czy dany produkt już się na liście znajduje.
#     3. Usunięcie konkretnego produktu z listy.
#     4. Posortowanie listy alfabetycznie.
#
# METODY / OPERACJE do poznania:
#   - Dodawanie na koniec:          lista.append(element)
#   - Dodawanie na pozycję:         lista.insert(indeks, element)
#   - Usuwanie pierwszego dopasowania: lista.remove(element)
#   - Sprawdzanie obecności:        element in lista
#   - Sortowanie w miejscu:         lista.sort()
#   - Długość listy:                len(lista)
#   - Wyświetlanie wszystkich:      for produkt in lista
# =============================================================================

# --- Inicjalizacja pustej listy zakupów -------------------------------------
lista_zakupow: list[str] = []


# ============================================================
# FUNKCJA 1 – Dodaj produkt do listy
# ============================================================
def dodaj_produkt(produkt: str) -> None:
    """
    Dodaje `produkt` na koniec listy zakupów,
    o ile jeszcze go tam nie ma.
    """
    # TODO: 1. Sprawdź, czy `produkt` już jest w liście_zakupow (użyj `in`).
    #       2. Jeśli NIE ma – dodaj go za pomocą .append().
    #       3. Jeśli już jest – wypisz komunikat, np.:
    #          f"'{produkt}' jest już na liście zakupów."
    if produkt in lista_zakupow:
        print(f"'{produkt}' jest już na liście zakupów.")
    else:
        lista_zakupow.append(produkt)



# ============================================================
# FUNKCJA 2 – Usuń produkt z listy
# ============================================================
def usun_produkt(produkt: str) -> None:
    """
    Usuwa pierwsze wystąpienie `produktu` z listy zakupów.
    Jeśli produktu nie ma na liście, informuje o tym użytkownika.
    """
    # TODO: 1. Sprawdź, czy `produkt` jest w liście_zakupow (użyj `in`).
    #       2. Jeśli jest – usuń go za pomocą .remove().
    #       3. Jeśli nie ma – wypisz komunikat, np.:
    #          f"'{produkt}' nie znaleziono na liście zakupów."
    if produkt in lista_zakupow:
        lista_zakupow.remove(produkt)
    else:
        
        print(f"'{produkt}' nie znaleziono na liście zakupów.")



# ============================================================
# FUNKCJA 3 – Posortuj listę zakupów
# ============================================================
def posortuj_liste() -> None:
    """
    Sortuje listę zakupów alfabetycznie (w miejscu).
    """
    # TODO: Wywołaj metodę .sort() na liście_zakupow.
    #       Możesz przekazać argument key=str.lower, aby ignorować
    #       wielkość liter podczas sortowania.
    lista_zakupow.sort(key=str.lower)


# ============================================================
# FUNKCJA 4 – Wyświetl listę zakupów
# ============================================================
def wyswietl_liste() -> None:
    """
    Wypisuje wszystkie produkty z listy zakupów wraz z ich
    numerem porządkowym.
    """
    if not lista_zakupow:
        print("Lista zakupów jest pusta.")
        return

    print(f"Lista zakupów ({len(lista_zakupow)} produkty/ów):")
    # TODO: Użyj enumerate(lista_zakupow, start=1), aby wypisać
    #       każdy produkt z jego numerem, np.:
    #         1. Mleko
    #         2. Chleb
    for i, produkt in enumerate(lista_zakupow):
        print(f"{i+1}. {produkt}")


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Zarządzanie listą zakupów ===\n")

    print("-- Dodawanie produktów --")
    dodaj_produkt("Mleko")
    dodaj_produkt("Chleb")
    dodaj_produkt("Jabłka")
    dodaj_produkt("Ser")
    dodaj_produkt("Masło")
    dodaj_produkt("Mleko")   # duplikat – powinien zostać odrzucony
    wyswietl_liste()

    print("\n-- Usuwanie produktu 'Ser' --")
    usun_produkt("Ser")
    usun_produkt("Herbata")  # nieistniejący – powinien wypisać komunikat
    wyswietl_liste()

    print("\n-- Sortowanie listy --")
    posortuj_liste()
    wyswietl_liste()

