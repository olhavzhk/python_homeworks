class Mathematician:
    @staticmethod
    def square_nums(list_of_integers):
        return [i**2 for i in list_of_integers]

    @staticmethod
    def remove_positives(list_of_integers):
        return [i for i in list_of_integers if i < 0]

    @staticmethod
    def filter_leaps(list_of_integers):
        return [i for i in list_of_integers if not i % 4]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]