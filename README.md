So, what strategy could we use with [Wordle](https://www.powerlanguage.co.uk/wordle/)? (You can also use it to play [Sutom](https://sutom.nocle.fr/))

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

Alternative strategy: use the first turns to "scan" the alphabet. Make a move that will maximize your future level of information.

The `en` dictionary comes from [dwyl](https://github.com/dwyl/english-words).  
The `fr` dictionary comes from [lorenbrichter](https://github.com/lorenbrichter/Words).


```
usage: play_wordle.py [-h] [-n NB_LETTERS] [-l LANG]

Play Wordle and other similar games

optional arguments:
  -h, --help            show this help message and exit
  -n NB_LETTERS, --nb_letters NB_LETTERS
                        number of letters in the word to guess, default: 5
  -l LANG, --lang LANG  language of the game (default = en, supports fr and
                        en)
```