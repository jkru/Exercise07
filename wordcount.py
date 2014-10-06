import string

# Write a program, wordcount.py, that opens a file named on the command line and
# counts how many times each space-separated word occurs in that file. Your
# program should then print those counts to the screen

input_file = open("twain.txt","r")

text = {}

our_punct = list(string.punctuation) 
our_punct.remove("-")
our_punct = "".join(our_punct)

for line in input_file:
    line = line.replace("--"," ").lower()
    line = line.rstrip().split()

    for word in line:

        iterword = ""           # look for better way to strip punct only from beg/end
        for achar in word:       
            if achar not in our_punct:
                iterword += achar
        word = iterword

        text[word] = text.get(word, 0) + 1

freq = []

for word, count in text.iteritems():
    freq.append([count, word])

freq = sorted(freq)
freq.reverse()

for i in range(len(freq)):
    print freq[i][1], freq[i][0]

#setdefault

# "didn't" => "didnt"    
# "it's" != "its"

# """
# It was forgive mea grave error that she said ..."
# """



# "was forgive"