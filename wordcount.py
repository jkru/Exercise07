import string
from operator import itemgetter

# Write a program, wordcount.py, that opens a file named on the command line and
# counts how many times each space-separated word occurs in that file. Your
# program should then print those counts to the screen

input_file = open("twain.txt","r")

text = {}

our_punct = list(string.punctuation)    # Creating custom punctuation list that doesn't include dashes.
our_punct.remove("-")                   # We will handle dashes separately later on.
our_punct = "".join(our_punct)

fix_split = False

for line in input_file:
    line = line.replace("--"," ").lower()
    line = line.rstrip().split()

    if line:
        if fix_split == True:
            line[0] = split_word + line[0]
            fix_split = False

        lastword = line[-1]
        if lastword[-1] == "-":
            split_word = lastword[:-1]
            del line[-1]
            fix_split = True

    for word in line:

        word = word.strip(our_punct)   # Strips punctuation at beginning and end of words

        text[word] = text.get(word, 0) + 1  # Searches for word in dict. Sets new word counts = 1 and increments existing words by 1

freq = []               # Turning word count dictionary into a list of tuples
for word, count in text.iteritems():
    freq.append([word,count])   

freq = sorted(freq)         # sort words alphabetically
freq = sorted(freq, key = itemgetter(1), reverse = True)  # sort by 2nd item in tuple (count) in descending order

for i in range(len(freq)):
    print freq[i][1], freq[i][0]
