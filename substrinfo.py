# substrinfo.py
# Class for information about a substring.

class SubstrInfo:
    def __init__(self, left_rank, right_rank, index):
        self.left_rank = left_rank
        self.right_rank = right_rank
        self.index = index

    def get_index(self):
        return self.index

    def __str__(self):
        return str(self.left_rank) + ' ' + str(self.right_rank) + ' ' + str(self.index)

    def __lt__(self, other):
        return self.left_rank < other.left_rank \
               or (self.left_rank == other.left_rank and self.right_rank < other.right_rank)

    def __le__(self, other):
        return self.left_rank <= other.left_rank \
               or (self.left_rank == other.left_rank and self.right_rank <= other.right_rank)

    def __gt__(self, other):
        return self.left_rank > other.left_rank \
               or (self.left_rank == other.left_rank and self.right_rank > other.right_rank)

    def __ge__(self, other):
        return self.left_rank >= other.left_rank \
               or (self.left_rank == other.left_rank and self.right_rank >= other.right_rank)

    def __eq__(self, other):
        return self.left_rank == other.left_rank and self.right_rank == other.right_rank

    def __ne__(self, other):
        return self.left_rank != other.left_rank or self.right_rank != other.right_rank
