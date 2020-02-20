import heapq
import os, sys
from objs import Library, LoadData
from max_heap import MaxHeap

updating_frequency = 5


def update_queue(library_list):
    remaining_libraries = []

    for library in library_list:
        remaining_libraries.append(
            (library.get_score(remaining_days, scanned_books), library))

    priority_queue = MaxHeap(remaining_libraries)

    return priority_queue


def update_scanned_books(scanned_books, library, remaining_days):
    for book in library.get_books(scanned_books, remaining_days):
        scanned_books[book] = None


if __name__ == "__main__":

    data = LoadData(sys.argv[1])

    library_list = data.get_library_list()

    # Per aggiornare velocemente la lista delle librerie rimanenti
    library_dict = {}
    for library in library_list:
        library_dict[library] = None

    remaining_days = data.get_days()
    scanned_books = {}

    output_scanned = []
    output_lib = []

    while len(library_list) != 0 and remaining_days > 0:
        # Prendo una versione aggiornata della priority queue
        priority_queue = update_queue(library_list)

        remaining_update_steps = updating_frequency

        while remaining_update_steps != 0 and len(priority_queue) > 0:
            # prendo la libreria a massimo guadagno
            _, next_library = priority_queue.remove_max()

            # aggiungo per l'output
            output_scanned.append( library_list.copy() )
            output_lib.append(next_library)

            # Aggiorno le librerie da scansionare
            del library_dict[next_library]

            # Aggiorno i libri scannerizzati
            update_scanned_books(scanned_books, next_library, remaining_days)

            # update remaining days
            remaining_days -= next_library.signup_time
            remaining_update_steps -= 1

        # Aggiorno library list
        # le chiavi del dizionario sono le librerie che non ho allocato
        library_list = [library for library in library_dict.keys()]

    print("Bravo a zia")
    
    print(len(output_lib))
    for l,s in zip(output_lib, output_scanned):
        books = l.get_books_in_order(s)
        print(l.id,len(books))
        print(' '.join([str(b.id) for b in books]))