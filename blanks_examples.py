from textblob import TextBlob
from textblob import Word
import re
import random
with open('file.txt','r')as f:
	data = f.readlines()
# print(type(data))
listToStr = ''.join([str(x)for x in data])
print(type(listToStr))
text = TextBlob(listToStr)
Sentences = text.sentences
sentence_count = len(Sentences)
print("SENTENCE-COUNT:",sentence_count)
tags      = text.tags
word      = text.words
# print("WORDS:",word)
# print("Tags:",tags)
# print("Sentences:",Sentences)
poss = {}
for t in text.tags:
        tag = t[1]
        # print("tag:",tag)
        if tag not in poss:
            poss[tag] = []
        poss[tag].append(t[0])

# print("POSS:",poss)
# insensitive_hippo = re.compile(re.escape(word), re.IGNORECASE)
# print(insensitive_hippo.sub('__________________', sentence))
words = None
if 'NNP' in poss:
	words = poss['NNP']
	print("words1111:",words)
elif 'NN' in poss:
    # print("HELLLOOWW")
    words = poss['NN']
    # print("words222:",words)
else:
    print("NN and NNP not found")

print("words length:",len(words))
if len(words) > 0:
    # xx = random.choice(words)
    xx = words[0]
    print("XXX:",xx)
# # print("Sentences:",Sentences.sentences)
# # print("TAGS:",Sentences.tags)
# # bucket = {}

# For a sentence create a blank space.
# It first tries to randomly selection proper-noun 
# and if the proper noun is not found, it selects a noun randomly.
# def removeWord(sentence, poss):
#     words = None
#     if 'NNP' in poss:
#         print("HIIIIIIIIIIII")
#         words = poss['NNP']
#         print("Words:",words)
#     elif 'NN' in poss:
#         # print("HELLLOOWW")
#         words = poss['NN']
#     else:
#         print("NN and NNP not found")
#         return (None, sentence, None)