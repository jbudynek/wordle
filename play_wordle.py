# coding: utf-8
from collections import Counter
import copy
import re
import argparse

# find word that contains n arbitrary letters (in place, or somewhere), does not contain p arbitrary letters
# sort them by combined highest letter frequency

def compute_word_to_score(words, counters, nb_letters):

    # the score of a word is the product of the frequencies of its letters
    # we return a dictionary sorted by ascending score value

    freq = []

    for i in range(nb_letters):
        freq.append(counters[i])
        tot = sum(counters[i].values())
        for k, v in freq[i].items():
            freq[i][k] = v / tot

    word2score = {}

    for word in words:
        score = 1
        for i in range(nb_letters):
            letter = word[i]
            score *= freq[i][letter]
        word2score[word] = score

    asc_score = dict(sorted(word2score.items(), key=lambda item: item[1]))
    return asc_score


def print_w2s(w2s, word2count):
    for k, v in w2s:
        print(k, "{:.2e}".format(v), word2count.get(k))


def build_word_to_score(all_words, nb_letters):

    # keep {nb_letters}-letters word only, in two lists, one with repeats, one with no repeats
    # count letter frequencies

    c_nbl = []  # array of Counters()
    for i in range(nb_letters):
        c_nbl.append(Counter())
    words_nbl = []
    for ww in all_words:
        if len(ww) == nb_letters:
            words_nbl.append(ww)
            for i in range(nb_letters):
                c_nbl[i].update(ww[i])

    word2score = compute_word_to_score(words_nbl, c_nbl, nb_letters)

    return word2score


def play_round(
    word2score, excluded_letters_set, included_letters_set, patterns, word2count
):
    print("Nb words:", len(word2score))
    candidates = {}
    map = word2score
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

    print("Nb candidates:", len(candidates))

    to_propose = list(candidates.items())[-10:]
    if len(to_propose) > 0:
        print("Some good words to try:")
        print_w2s(reversed(to_propose), word2count)

    print("***")

    return candidates

def read_all_words(dictionary):
    input_file = "words/" + dictionary + ".txt"

    print("input file=", input_file)

    f = open(input_file, "r")
    contents = f.read()
    all_words = contents.splitlines()
    f.close()
    return all_words


def read_word2count(fred):

    f = open("words/"+freq, "r")
    contents = f.read()
    f.close()
    lines = contents.splitlines()
    del lines[0]
    w2c = {}
    for l in lines:
        wc = l.split(",")
        w2c[wc[0]] = int(wc[1])
    return w2c


# read inputs


parser = argparse.ArgumentParser(description="Play Wordle and other similar games")

parser.add_argument(
    "-n",
    "--nb_letters",
    type=int,
    default=5,
    help="number of letters in the word to guess, default: 5",
)

parser.add_argument(
    "-d",
    "--dictionary",
    type=str,
    default="wordle",
    help="dictionary used for the game (default: wordle, supports wordle, sutom, lemot, primes, fr, en...)",
)

parser.add_argument(
    "-f",
    "--freq",
    type=str,
    default="en_unigram_freq.csv",
    help="frequency file for unigrames (default: en_unigram_freq.csv)",
)

args = parser.parse_args()
print(args)

nb_letters = args.nb_letters
dictionary = args.dictionary
freq = args.freq

all_words = read_all_words(dictionary)

word2count = read_word2count(freq)

# initiate

word2score = build_word_to_score(all_words, nb_letters)

print("Here are ten good words to start with:")
print_w2s(reversed(list(word2score.items())[-10:]), word2count)
print("***")

initial_w2s = copy.deepcopy(word2score)

# play rounds

excluded = set()
included = set()
patterns = []

while True:

    to_clear = False
    print("(Note: start with _ to clear the lists)")

    e = input("Additional exluded letters?")

    i = input("Additional included letters?")

    p = input("Additional pattern (regexp)?")

    if e.startswith("_"):
        to_clear = True
        excluded = set(e[1:])
    else:
        excluded.update(e)

    if i.startswith("_"):
        to_clear = True
        included = set(i[1:])
    else:
        included.update(i)

    if p.startswith("_"):
        to_clear = True
        patterns = []
        p = p[1:]

    if p != "":
        patterns.append(p)

    if to_clear:
        word2score = build_word_to_score(initial_w2s, nb_letters)

    print("Excluded=", excluded)
    print("Included=", included)
    print("Patterns=", patterns)

    candidates = play_round(word2score, excluded, included, patterns, word2count)
    word2score = build_word_to_score(candidates, nb_letters)

