import random
import time

def generate_random_array(size: int, min_val: int, max_val: int) -> list[int]:
    """
    Generuje listę size losowych liczb całkowitych z zakresu [min_val, max_val].
    Obsługuje ujemne wartości min_val bez ryzyka overflow.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def print_array(array: list[int]) -> None:
    """Wypisuje zawartość listy w czytelnym formacie, np.: [ 3, 7, 1, 9, 4 ]"""
    print("[ " + ", ".join(str(x) for x in array) + " ]")


def is_sorted(array: list[int]) -> bool:
    """
    Sprawdza, czy lista jest posortowana niemalejąco (rosnąco).
    Przydatne do autoweryfikacji poprawności implementacji.
    """
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def swap(array: list[int], i: int, j: int) -> None:
    """Zamienia miejscami dwa elementy listy o indeksach i i j."""
    array[i], array[j] = array[j], array[i]


def bubble_sort(array: list[int]) -> None:
    stan = 0
    for i in range(len(array)):
        stan = 0
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                swap(array, j, j+1)
                stan +=1
        if stan == 0:
            return
        
    return

def selection_sort(array: list[int]) -> None:

    for i in range(len(array)):
        idx = i
        for j in range(i + 1, len(array)):
                if array[idx] > array[j]:
                    idx = j
        if idx != i:
           swap(array, i, idx)

    return

def insertion_sort(array: list[int]) -> None:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return

def _merge(array: list[int], left: int, mid: int, right: int) -> None:
    temp = []

    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= right:
        temp.append(array[j])
        j += 1

    array[left:right + 1] = temp

def _merge_sort(array: list[int], left: int, right: int) -> None:
    if left >= right:
        return

    mid = (left + right) // 2

    _merge_sort(array, left, mid)
    _merge_sort(array, mid + 1, right)

    _merge(array, left, mid, right)


def merge_sort(array: list[int]) -> None:
    """
    Interfejsowa funkcja sortowania przez scalanie (Merge Sort).
    Wywołuje funkcję _merge_sort z odpowiednimi parametrami początkowymi
    """
    _merge_sort(array, 0, len(array) - 1)


def _partition(array: list[int], low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def _quick_sort(array: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_index = _partition(array, low, high)

    _quick_sort(array, low, pivot_index - 1)
    _quick_sort(array, pivot_index + 1, high)

def quick_sort(array: list[int]) -> None:
    """
    Interfejsowa funkcja sortowania szybkiego (Quick Sort).
    Wywołuje funkcję _quick_sort z odpowiednimi parametrami początkowymi
    """
    _quick_sort(array, 0, len(array) - 1)



def linear_search(array: list[int], target: int) -> int:
    for i in range(len(array)):
        if array[i] == target:
            return i

    return -1


def binary_search(array: list[int], target: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
     
     # --- Konfiguracja testu ---
    SIZE = 25    # liczba elementów listy
    MIN  = 0     # minimalna wartość elementu
    MAX  = 100   # maksymalna wartość elementu

    print("=== Laboratorium: Algorytmy i Struktury Danych ===\n")

    # 1. Generowanie losowej listy
    array = generate_random_array(SIZE, MIN, MAX)
    target = array[SIZE // 2]  # wybieramy element ze środka jako cel wyszukiwania

    # 2. Wyświetlenie listy przed sortowaniem
    print("Lista przed sortowaniem: ", end="")
    print_array(array)

    # 3. Pomiar czasu sortowania
    #    Zamień wywołanie poniżej na funkcję, którą chcesz przetestować,
    #    np. selection_sort(array), insertion_sort(array) itp.
    #    Dla merge_sort użyj:  merge_sort(array, 0, len(array) - 1)
    #    Dla quick_sort użyj:  quick_sort(array, 0, len(array) - 1)
    start_time = time.perf_counter_ns()

    quick_sort(array)  # <-- ZMIEŃ NA WYBRANĄ FUNKCJĘ

    end_time = time.perf_counter_ns()
    elapsed  = end_time - start_time

    # 4. Wyświetlenie listy po sortowaniu
    print("Lista po sortowaniu:     ", end="")
    print_array(array)

    # 5. Weryfikacja poprawności sortowania
    if is_sorted(array):
        print("\n✔ Sortowanie zakończone sukcesem!")
    else:
        print("\n✘ Błąd: lista NIE jest posortowana. Sprawdź implementację.")

    print(f"Czas wykonania: {elapsed} ns")

    # --- Przykładowy test wyszukiwania liniowego ---
    print("\n--- Test wyszukiwania liniowego ---")
    linear_index = linear_search(array, target)
    if linear_index != -1:
        print(f"Znaleziono wartość {target} pod indeksem: {linear_index}")
    else:
        print(f"Wartość {target} nie została znaleziona (sprawdź implementację linear_search).")

    # --- Przykładowy test wyszukiwania binarnego ---
    print("\n--- Test wyszukiwania binarnego ---")
    start_search = time.perf_counter_ns()
    index = binary_search(array, target)
    end_search = time.perf_counter_ns()
    search_elapsed = end_search - start_search

    if index != -1:
        print(f"Znaleziono wartość {target} pod indeksem: {index}")
    else:
        print(f"Wartość {target} nie została znaleziona (sprawdź implementację binary_search).")

    print(f"Czas wyszukiwania: {search_elapsed} ns")