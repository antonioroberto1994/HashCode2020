import sys

class Book():
    def __init__(self):
        pass

class Library():
    def __init__(self, books_in_lib, nbooks_per_day, signup_time):
        self.books_in_lib = books_in_lib
        self.nbooks_per_day = nbooks_per_day
        self.signup_time = signup_time
    def get_score(self, remaining_days):
        pass


def main(fname):
    pass

def read_file(fname):
    libraries = []
    with open(fname, 'r') as f:
        nbooks = int(next(f))
        nlibraries = int(next(f))
        days = int(next(f))
        scores = next(f).strip().split(' ')
        xx = next(f).strip().split(' ')
        for j in range(nlibraries):
            Nj, Tj, Mj = [int(x) for x in xx]
            xx = next(f).strip().split(' ')
            books_in_lib = [int(x) for x in xx]
            assert(len(books_in_lib)==Nj)
            libraries.append(Library(books_in_lib, Mj, Tj))
    
    
if "__main__" == __name__:
    main(sys.argv[1])