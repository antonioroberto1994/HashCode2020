import sys


class Book():
    def __init__(self, id, score):
        self.id = int(id)
        self.score = int(score)

    def __str__(self):
        return "(%d->score=%d)" % (self.id, self.score)

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return self.__str__()


class Library():
    def __init__(self, j, books_in_lib, nbooks_per_day, signup_time):
        self.books_in_lib = sorted(books_in_lib, reverse=True)
        self.nbooks_per_day = nbooks_per_day
        self.signup_time = signup_time
        self.id = j

    def get_score(self, remaining_days, scanned_books):
        score = 0
        time = remaining_days - self.signup_time
        books_in_time = time*self.nbooks_per_day
        for b in range(books_in_time):
            book = self.books_in_lib[b]
            if book not in scanned_books:
                score += book.score
        return score

    def get_books(self, scanned_books, max_days):
        x = []
        max_books = max_days*len(self.books_in_lib)
        for i,b in enumerate(self.books_in_lib):
            x.append(b)
            if i> max_books:
                break
        return x

    def get_books_in_order(self, scanned_books):
        # .join(' ')
        return [b.id for b in self.books_in_lib if b not in scanned_books]

    def __str__(self):
        return ("Library %d: " % self.id )+ str(self.books_in_lib) 

    def __repr__(self):
        return self.__str__()


def read_file(fname):
    libraries = []
    with open(fname, 'r') as f:
        xx = next(f).strip().split(' ')
        nbooks, nlibraries, days = [int(x) for x in xx]
        scores = next(f).strip().split(' ')
        books = [Book(i, s) for i, s in enumerate(scores)]
        for j in range(nlibraries):
            xx = next(f).strip().split(' ')
            Nj, Tj, Mj = [int(x) for x in xx]
            xx = next(f).strip().split(' ')
            books_in_lib = [books[int(x)] for x in xx]
            assert(len(books_in_lib) == Nj)
            libraries.append(Library(j, books_in_lib, Mj, Tj))
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
    loader = LoadData(fname)
    print([str(l) for l in loader.get_library_list()])


if "__main__" == __name__:
    main(sys.argv[1])
