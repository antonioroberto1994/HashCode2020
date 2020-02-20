import sys

class Book():
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Library():
    def __init__(self, books_in_lib, nbooks_per_day, signup_time):
        self.books_in_lib = books_in_lib
        self.nbooks_per_day = nbooks_per_day
        self.signup_time = signup_time
    def get_score(self, remaining_days, scanned_books):
        pass
    def get_books(self):
        pass
    def get_books_next_day(self, remaining_books):
        pass



def read_file(fname):
    libraries = []
    with open(fname, 'r') as f:
        nbooks = int(next(f))
        nlibraries = int(next(f))
        days = int(next(f))
        scores = next(f).strip().split(' ')
        books = [Book(i,s) for i,s in enumerate(scores)]
        xx = next(f).strip().split(' ')
        for j in range(nlibraries):
            Nj, Tj, Mj = [int(x) for x in xx]
            xx = next(f).strip().split(' ')
            books_in_lib = [books[int(x)] for x in xx]
            assert(len(books_in_lib)==Nj)
            libraries.append(Library(books_in_lib, Mj, Tj))
    return libraries, nbooks, days, scores
    

class LoadData():
    def __init__(self, path):
        self.libraries, self.nbooks, self.days, self.scores = read_file(path)
    def get_books_scores(self):
        return self.scores
    def get_library_list(self):
        return self.libraries
    def get_days(self):
        return self.days



def main(fname):
    pass

if "__main__" == __name__:
    main(sys.argv[1])
