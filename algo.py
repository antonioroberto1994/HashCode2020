import heapq
import os
from objs import Library, LoadData
from max_heap import MaxHeap


def update_queue(library_list):
    remaining_libraries = []

    for library in library_list:
        remaining_libraries.append(
            (library.get_score(remaining_days, scanned_books), library))

    priority_queue = MaxHeap(remaining_libraries)

    return priority_queue


def update_scanned_books(scanned_books, library):
    for book in library.get_books():
        scanned_books[book] = None


if __name__ == "__main__":

    data = LoadData('data'+os.sep+'b_read_on.txt')

    library_list = data.get_library_list()

    # Per aggiornare velocemente la lista delle librerie rimanenti
    library_dict = {}
    for library in library_list:
        library_dict[library] = None

    remaining_days = data.get_days()
    scanned_books = {}

    output_lib = []

    while len(library_list) != 0 and remaining_days > 0:
        # Prendo una versione aggiornata della priority queue
        priority_queue = update_queue(library_list)

        update_steps = 5

        while update_steps != 0:
            # prendo la libreria a massimo guadagno
            _ , next_library = priority_queue.max()

            # aggiungo per l'output
            output_lib.append(next_library)

            # Aggiorno le librerie da scansionare
            del library_dict[next_library]

            # Aggiorno i libri scannerizzati
            update_scanned_books(scanned_books, next_library)

            # update remaining days 
            remaining_days -= next_library.signup_time
            update_steps -= 1

        # Aggiorno library list 
        # le chiavi del dizionario sono le librerie che non ho allocato
        library_list = [library for library in library_dict.keys()]

       
