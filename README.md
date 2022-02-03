So, what strategy could we use with [Wordle](https://www.powerlanguage.co.uk/wordle/)?  
(You can also use it to play [Sutom](https://sutom.nocle.fr/) or [Le Mot](https://wordle.louan.me/) or even [Primel](https://converged.yt/primel/))

Suppose you have a list of all valid English words.  
First, keep only the five-letters word, and count how often each letter comes up.  
As a first guess, pick a word that has letters that are all quite frequent.  
Then, based on the result, you can use:
- grey letters to exclude words that have them - they are forbidden;
- yellow letters to keep words that have them - they are somewhere in the solution;
- yellow letters again to exclude words that have them where they are yellow - they are somewhere else in the solution;
- green letters to keep words that have them at the right place like in the solution.

In this updated word list, again pick a word that has letters that are frequent.  
Do that a few times and you will find the word.

Here is the Python code to do so, it's an interactive script.
In practice I use two lists, one with words that have repeated letters, one with words that do not.  
For the last two cases described earlier, you can use regular expressions, such as `..a..` (has an 'a' in third place) or `.[^b]...` (does not have an 'b' in second place)

No mathematical guarantee, just basic code using collections and pragmatism. It's not an automatic solver.  
You can pick and choose what you want in the output, because as a human you will have an intuition of what the word to guess could be in reality.  
My word of choice to start with is "raise".

Could be made better by showing some sort of "popularity" of the word in the english language (frequency in a huge corpus for instance).  
Also Wordle gives you additional info sometimes (a letter can be green, and grey somewhere else), which is not leveraged in the script, you will have to use your head!  
We could also compute letter frequency for each position in the word.

Alternative strategy: use the first turns to "scan" the alphabet. Make a move that will maximize your future level of information.

Dictionaries:
- The Wordle and Le Mot dictionaries were built by looking into the javacript code of each site.
- The Sutom dictionary come from [JonathanMM](https://framagit.org/JonathanMM/sutom)
- The primes dictionary was built manually from [this prime list from UTM](https://primes.utm.edu/lists/small/100000.txt).
- The `en` and `fr` dictionaries comes from [lorenbrichter](https://github.com/lorenbrichter/Words).
- `words_alpha.txt` comes from [dwyl](https://github.com/dwyl/english-words)
- `sowpods.txt` comes from [jesstess](https://github.com/jesstess/Scrabble/tree)
```
usage: play_wordle.py [-h] [-n NB_LETTERS] [-d DICTIONARY]

Play Wordle and other similar games

optional arguments:
  -h, --help            show this help message and exit
  -n NB_LETTERS, --nb_letters NB_LETTERS
                        number of letters in the word to guess, default: 5
  -d DICTIONARY, --dictionary DICTIONARY
                        dictionary used for the game (default: worlde,
                        supports wordle, sutom, lemot, primes, fr, en)
```