# coding: utf-8
from collections import Counter
import copy
import re
import argparse

# find word that contains n arbitrary letters (in place, or somewhere), does not contain p arbitrary letters
# sort them by combined highest letter frequency


def compute_word_to_score(words, counter):

    # the score of a word is the product of the frequencies of its letters
    # we return a dictionary sorted by ascending score value

    freq = counter
    tot = sum(counter.values())
    for k, v in freq.items():
        freq[k] = v / tot

    word2score = {}

    for word in words:
        score = 1
        for letter in word:
            score *= freq[letter]
        word2score[word] = score

    asc_score = dict(sorted(word2score.items(), key=lambda item: item[1]))
    return asc_score


def print_w2s(w2s):
    for k, v in w2s:
        print(k, "{:.2e}".format(v))


def start_wordle(all_words, nb_letters, DBG=True):

    # keep {nb_letters}-letters word only, in two lists, one with repeats, one with no repeats
    # count letter frequencies

    c_nbl = Counter()
    words_nbl = []
    c_nbl_no_repeat = Counter()
    words_nbl_no_repeat = []
    for ww in all_words:
        if len(ww) == nb_letters:
            words_nbl.append(ww)
            c_nbl.update(ww)
            if Counter(ww).most_common()[0][1] == 1:
                words_nbl_no_repeat.append(ww)
                c_nbl_no_repeat.update(ww)

    word2score = compute_word_to_score(words_nbl, c_nbl)
    word2score_norepeat = compute_word_to_score(
        words_nbl_no_repeat, c_nbl_no_repeat)

    for map in [word2score_norepeat, word2score]:
        print("Here are ten good words to start with:")
        print_w2s(reversed(list(map.items())[-10:]))
    print("***")

    return word2score, word2score_norepeat


def play_round(
    word2score,
    word2score_norepeat,
    excluded_letters_set,
    included_letters_set,
    patterns,
):
    candidates = {}
    for map in [word2score_norepeat, word2score]:
        for word, score in map.items():
            word_set = set(word)
            include_in_candidates = True
            # test for excluded letters
            if len(word_set.intersection(excluded_letters_set)) > 0:
                include_in_candidates = False

            if include_in_candidates:
                # test for included letters

                if len(word_set.intersection(included_letters_set)) != len(
                    included_letters_set
                ):
                    include_in_candidates = False

                if include_in_candidates:
                    # test for pattern matching
                    for patt in patterns:
                        if not re.match(patt, word):
                            include_in_candidates = False

            if include_in_candidates:
                candidates[word] = score

        to_propose = list(candidates.items())[-10:]
        if len(to_propose) > 0:
            print("Some good words to try:")
            print_w2s(reversed(to_propose))

    print("***")

    return -1

# Main


parser = argparse.ArgumentParser(
    description='Play Wordle and other similar games')

parser.add_argument("-n", "--nb_letters", type=int, default=5,
                    help="number of letters in the word to guess, default: 5")

parser.add_argument("-d", "--dictionary", type=str, default='wordle',
                    help="dictionary used for the game (default: worlde, supports wordle, sutom, lemot, primes, fr, en)")

args = parser.parse_args()
print(args)

nb_letters = args.nb_letters
dictionary = args.dictionary
INPUT_FILE = "words/"+dictionary+".txt"

print("input file=", INPUT_FILE)

f = open(INPUT_FILE, "r")
contents = f.read()
all_words = contents.splitlines()
f.close()

word2score, word2score_norepeat = start_wordle(
    all_words, nb_letters, DBG=False)

# part 2

excluded = set()
included = set()
patterns = []

while True:

    print("(Note: start with _ to clear the lists)")

    e = input("Additional exluded letters?")

    i = input("Additional included letters?")

    p = input("Additional pattern (regexp)?")

    if e.startswith("_"):
        excluded = set(e[1:])
    else:
        excluded.update(e)

    if i.startswith("_"):
        included = set(i[1:])
    else:
        included.update(i)

    if p.startswith("_"):
        patterns = []
        p = p[1:]

    if p != "":
        patterns.append(p)

    print("Excluded=", excluded)
    print("Included=", included)
    print("Patterns=", patterns)

    ret = play_round(word2score, word2score_norepeat,
                     excluded, included, patterns)
