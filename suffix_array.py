# suffix_array.py
# Python program to compute a suffix array and lcp list for a text.
# Written by THC for CS 1.

from substrinfo import SubstrInfo

# Return the suffix array for a text t.
def make_suffix_array(t):
    n = len(t)

    # Make the initial substring ranks, based on the ASCII character codes.
    substr_ranks = []
    for i in range(n-1):
        substr_ranks.append(SubstrInfo(ord(t[i]), ord(t[i+1]), i))
    # The last one is special, since there's no second character in the pair.
    substr_ranks.append(SubstrInfo(ord(t[n-1]), -1, n-1))

    if verbose:
        print("Initial substring ranks before sorting:")
        for i in range(n):
            print(substr_ranks[i], t[i:i+2])

    # Sort the initial substring ranks.
    substr_ranks.sort()

    if verbose:
        print("\nInitial substring ranks after sorting:")
        for i in range(n):
            index = substr_ranks[i].get_index()
            print(substr_ranks[i], t[index:index+2])

    length = 2

    # Double the substring length, going as long as some right substring in a combination
    # could be nonempty.
    while length < n:
        rank, max_rank = make_rank(substr_ranks)
        if max_rank == n-1:
            break   # no further changes will occur

        # Make new substring ranks.
        substr_ranks = []
        for i in range(n):
            if i + length < n:
                right_substr_rank = rank[i + length]    # right substring not empty
            else:
                right_substr_rank = -1                  # right substring is empty
            substr_ranks.append(SubstrInfo(rank[i], right_substr_rank, i))

        if verbose:
            print("\nSubstring ranks for length " + str(length) +" before sorting:")
            for i in range(n):
                index = substr_ranks[i].get_index()
                print(substr_ranks[i], t[index:index + 2*length])

        # Re-sort.
        substr_ranks.sort()

        if verbose:
            print("\nSubstring ranks for length " + str(length) +" after sorting:")
            for i in range(n):
                index = substr_ranks[i].get_index()
                print(substr_ranks[i], t[index:index + 2*length])

        length *= 2     # double the substring length for the next iteration

    # The suffix array is just the index part of the last sorted list of substr_ranks.
    suffix_array = []
    for i in range(n):
        suffix_array.append(substr_ranks[i].get_index())

    return suffix_array

# Given lexically sorted substring ranks, return a list of new ranks and
# the maximum rank assigned.
def make_rank(substr_ranks):
    n = len(substr_ranks)
    rank = [None] * n

    # The first one always has rank 0.
    r = 0
    rank[substr_ranks[0].get_index()] = r

    for i in range(1, n):
        # If the ranks of the left and right substrings are the same as for the previous
        # one, they get the same rank.  Otherwise, increment the rank.
        if substr_ranks[i] != substr_ranks[i-1]:
            r += 1
        rank[substr_ranks[i].get_index()] = r

    return rank, r

# Compute and return the lcp list of the lengths of the longest common prefixes.
# Takes a text t and its suffix array.
def make_lcp(t, suffix_array):
    n = len(t)
    rank = [None] * n
    lcp = [0] * n

    for i in range(n):
        rank[suffix_array[i]] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            k = suffix_array[rank[i]-1]
            m = max(i, k)

            while m+h < n and t[i+h] == t[k+h]:
                h += 1

            lcp[rank[i]] = h

            if h > 0:
                h -= 1

    return lcp

# Pretty-print a suffix array of text t, the lcp list, and the sorted suffixes.
def print_suffix_array(t, suffix_array, lcp):
    # Determine the number of characters in the highest index.
    n = len(t)
    width = len(str(n-1))

    for i in range(n):
        sa_value = suffix_array[i]
        print(str(i).rjust(width) + ' ' + str(sa_value).rjust(width) + ' ' + \
              str(lcp[i]).rjust(width) + ' ' + t[sa_value:])

if __name__ == '__main__':
    verbose = True
    t = 'bippityboppityboo'
    suffix_array = make_suffix_array(t)
    lcp = make_lcp(t, suffix_array)
    if verbose:
        print("\n\nThe suffix array and lcp list:")
    print_suffix_array(t, suffix_array, lcp)
else:
    verbose = False
