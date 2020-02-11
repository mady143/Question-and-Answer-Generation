from textblob import TextBlob
 
# This is the text that we are going to use. 
# This text is from wikipedia on World War 2 - https://en.wikipedia.org/wiki/World_War_II
# Note: triple quotes are used for defining multi line string
# with open('file1.txt','r')as f:
with open('file1.txt','r')as f:
# with open('file3.txt','r')as f:
    data = f.readlines()
listToStr = ''.join([str(x)for x in data])
ww2 = TextBlob(listToStr)
tgs = ww2.tags
sentences = ww2.sentences
sentence_length = len(sentences)
# print(sentence_length)
sposs = {}
for sentence in ww2.sentences:
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
    # print(poss)

import random
import re

# Create the blank in string
def replaceIC(word, sentence):
    
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
        word = words[0]
        words_list1 = words[0:4]
        replaced = replaceIC(word, sentence)
        return (words_list1, sentence, replaced)
    else:
        print("words are empty")
        return (None, sentence, None)
question_count = 0
for sentence in sposs.keys():

    poss = sposs[sentence]
    (words_list1, osentence, replaced) = removeWord(sentence, poss)
    if replaced is None:
        print ("Founded none for ")
        print(sentence)
    else:
        # count =0
        print(str(question_count+1) + ": " + replaced)
        question_count+=1
        print("Possible answers are:")
        if 'NNP' in poss:
            ll = poss['NNP']
        elif 'NN' in poss:
            ll = poss['NN']



        distnict_list= list(dict.fromkeys(ll))
        total_words = ww2.words
        xx = total_words
        for b in xx:
            if len(distnict_list) <4:
                if not any(b in s for s in distnict_list):
                    distnict_list.append(b)
        count = 0 # list indexes start at 0 in python
        correct_answer = distnict_list[0]
        
        list1 = []
        list1.append(words_list1[0])
        numbers = [num for num in distnict_list if num != words_list1[0]]
        list1.extend(numbers[0:3])
        random.shuffle(list1)
        while count < len(list1[0:4]):
            print(str(count+1) + ": " + list1[count])
            count += 1
        print ("\n===============")
        print("Correct Answer:", correct_answer)
        print("\n")