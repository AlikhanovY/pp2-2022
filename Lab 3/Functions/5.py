from itertools import permutations
def find_permutations(s):
    char_list = [s[i] for i in range(0, len(s))]
    char_list.sort()
    prms = permutations(char_list)
    for permutation in prms:
        print(permutation)
find_permutations("bcad")