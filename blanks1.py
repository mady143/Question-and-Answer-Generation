from textblob import TextBlob
 
# This is the text that we are going to use. 
# This text is from wikipedia on World War 2 - https://en.wikipedia.org/wiki/World_War_II
# Note: triple quotes are used for defining multi line string
with open('file1.txt','r')as f:
    data = f.readlines()
# print(type(data))
listToStr = ''.join([str(x)for x in data])
ww2 = TextBlob(listToStr)
tgs = ww2.tags

sposs = {}
for sentence in ww2.sentences:
    # print("Senetence:",sentence)
    # print("------------------")
    # We are going to prepare the dictionary of parts-of-speech as the key and value is a list of words:
    # {part-of-speech: [word1, word2]}
    # We are basically grouping the words based on the parts-of-speech
    
    poss = {}
    sposs[sentence.string] = poss;
    for t in sentence.tags:
        tag = t[1]
        if tag not in poss:
            poss[tag] = []
        poss[tag].append(t[0])
 
 
import random
import re
 
# Create the blank in string
def replaceIC(word, sentence):
    # print("words:",word)
    insensitive_hippo = re.compile(re.escape(word), re.IGNORECASE)
    return insensitive_hippo.sub('__________________', sentence)
 
# For a sentence create a blank space.
# It first tries to randomly selection proper-noun 
# and if the proper noun is not found, it selects a noun randomly.
def removeWord(sentence, poss):
    words = None
    if 'NNP' in poss:
        words = poss['NNP']
    elif 'NN' in poss:
        words = poss['NN']
    else:
        print("NN and NNP not found")
        return (None, sentence, None)
    if len(words) > 0:
        word = random.choice(words)
        replaced = replaceIC(word, sentence)
        print("word:",word)
        print("Sentence:",sentence)
        print("Replaced:",replaced)
        return (word, sentence, replaced)
    else:
        print("words are empty")
        return (None, sentence, None)
 
# Iterate over the sentenses 
for sentence in sposs.keys():
    poss = sposs[sentence]
    (word, osentence, replaced) = removeWord(sentence, poss)
    if replaced is None:
        print ("Founded none for ")
        print(sentence)
    else:
        print(replaced)
        print("Answer:",word)
 