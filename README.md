So, what strategy could we use with [Wordle](https://www.powerlanguage.co.uk/wordle/)?  
(You can also use it to play [Sutom](https://sutom.nocle.fr/) or [Le Mot](https://wordle.louan.me/) or even [Primel](https://converged.yt/primel/) or [Nerdle](https://nerdlegame.com/))

Suppose you have a list of all valid English words.  
First, keep only the five-letters word, and count how often each letter comes up. We do that for each position in the word.  
As a first guess, pick a word that has letters that are quite frequent in their position.  
Then, based on the result, you can use:
- grey letters to exclude words that have them - they are forbidden;
- yellow letters to keep words that have them - they are somewhere in the solution;
- yellow letters again to exclude words that have them where they are yellow - they are somewhere else in the solution;
- green letters to keep words that have them at the right place like in the solution.

In this updated word list, again pick a word that has letters that are frequent.  
Do that a few times and you will find the word.

Here is the Python code to do so, it's an interactive script.
For the last two cases described earlier, you can use regular expressions, such as `..a..` (has an 'a' in third place) or `.[^b]...` (does not have an 'b' in second place)

No mathematical guarantee, just basic code using collections and pragmatism. It's not an automatic solver.  
This program also shows the frequency of the word in the english language, to make choosing easier (a word that is not too obscure but also not too obvious).  
You can pick and choose what you want in the output, because as a human you will have an intuition of what the word to guess could be in reality.  

Wordle gives you additional info sometimes (a letter can be green, and grey somewhere else), which is not leveraged in the script, you will have to use your head!  
The script could be made better by explicitly computing the expected level of information of the next word to play.

Alternative strategy: use the first turns to "scan" the alphabet. 

My word of choice to start with is "raise".  
Some nice series of three words to start Worlde with:
- raise, clout, nymph
- arose, tunic, glyph
- arose, clint, dumpy
- cares, monty, build
- sores, canty, build
- cares, ponty, build

Dictionaries:
- The Wordle and Le Mot dictionaries were built by looking into the javacript code of each site.
- The Sutom dictionary comes from [JonathanMM](https://framagit.org/JonathanMM/sutom)
- The primes dictionary was built manually from [this prime list from UTM](https://primes.utm.edu/lists/small/100000.txt).
- The `en` and `fr` dictionaries comes from [lorenbrichter](https://github.com/lorenbrichter/Words).
- `words_alpha.txt` comes from [dwyl](https://github.com/dwyl/english-words)
- `sowpods.txt` comes from [jesstess](https://github.com/jesstess/Scrabble/tree)
- the `nerdle` dictionary was built manually in python (see in `tools`)

Word frequencies:
- English Word Frequency comes from [rtatman](https://www.kaggle.com/rtatman/english-word-frequency)
- French Word Frequency built from  [Lexique](http://www.lexique.org/) (see in `tools`)

```
Play Wordle and other similar games

optional arguments:
  -h, --help            show this help message and exit
  -n NB_LETTERS, --nb_letters NB_LETTERS
                        number of letters in the word to guess, default: 5
  -d DICTIONARY, --dictionary DICTIONARY
                        dictionary used for the game (default: wordle, supports wordle, sutom, lemot, primes, fr, en...)
  -f FREQ, --freq FREQ  frequency file for unigrames (default: en_unigram_freq.csv)
```