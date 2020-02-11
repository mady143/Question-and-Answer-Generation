from textblob import TextBlob
from textblob import Word
from collections import Counter
with open('file.txt','r')as f:
	data = f.readlines()
# print(type(data))
listToStr = ''.join([str(x)for x in data])
# print(type(listToStr))
text = TextBlob(listToStr)
# print("text:",text)
Sentences = text.sentences
sentence_count = len(Sentences)
print("Sentence Count:",sentence_count)
tags      = text.tags
tags_count = Counter(tag for word,tag in tags)
print("Tags Count:",tags_count)
print("Sentences:",Sentences)
# print("Sentences:",Sentences.sentences)
# print("TAGS:",Sentences.tags)
bucket = {}
for sentences in text.sentences: 
	for i,j in enumerate(sentences.tags):
		if j[1] not in bucket:
			bucket[j[1]] = i
			print(i)
# Create an empty string

question = ''




#     # Create a list of tag-combination

# l1 = ['NNP', 'VBG', 'VBZ', 'IN']
# # print(l1)
# l2 = ['NNP', 'VBG', 'VBZ']

# l3 = ['PRP', 'VBG', 'VBZ', 'IN']
# l4 = ['PRP', 'VBG', 'VBZ']
# l5 = ['PRP', 'VBG', 'VBD']
# l6 = ['NNP', 'VBG', 'VBD']
# l7 = ['NN', 'VBG', 'VBZ']

# l8 = ['NNP', 'VBZ', 'JJ']
# l9 = ['NNP', 'VBZ', 'NN']

# l10 = ['NNP', 'VBZ']
# l11 = ['PRP', 'VBZ']
# l12 = ['NNP', 'NN', 'IN']
# l13 = ['NN', 'VBZ']

# if all(key in  bucket for key in l1): #'NNP', 'VBG', 'VBZ', 'IN' in sentence.
    # question = 'What' + ' ' + sentences.words[bucket['VBZ']] +' '+ sentences.words[bucket['NNP']]+ ' '+ sentences.words[bucket['VBG']] + '?'


# if all(key in  bucket for key in l2): #'NNP', 'VBG', 'VBZ' in sentence.
#     question = 'What' + ' ' + sentences.words[bucket['VBZ']] +' '+ sentences.words[bucket['NNP']] +' '+ sentences.words[bucket['VBG']] + '?'


# elif all(key in  bucket for key in l3): #'PRP', 'VBG', 'VBZ', 'IN' in sentence.
#     question = 'What' + ' ' + sentences.words[bucket['VBZ']] +' '+ sentences.words[bucket['PRP']]+ ' '+ sentences.words[bucket['VBG']] + '?'


# elif all(key in  bucket for key in l4): #'PRP', 'VBG', 'VBZ' in sentence.
#     question = 'What ' + sentences.words[bucket['PRP']] +' '+  ' does ' + sentences.words[bucket['VBG']]+ ' '+  sentences.words[bucket['VBG']] + '?'

# elif all(key in  bucket for key in l7): #'NN', 'VBG', 'VBZ' in sentence.
#     question = 'What' + ' ' + sentences.words[bucket['VBZ']] +' '+ sentences.words[bucket['NN']] +' '+ sentences.words[bucket['VBG']] + '?'

# elif all(key in bucket for key in l8): #'NNP', 'VBZ', 'JJ' in sentence.
#     question = 'What' + ' ' + sentences.words[bucket['VBZ']] + ' ' + sentences.words[bucket['NNP']] + '?'

# elif all(key in bucket for key in l9): #'NNP', 'VBZ', 'NN' in sentence
#     question = 'What' + ' ' + sentences.words[bucket['VBZ']] + ' ' + sentences.words[bucket['NNP']] + '?'

# elif all(key in bucket for key in l11): #'PRP', 'VBZ' in sentence.
#     if sentences.words[bucket['PRP']] in ['she','he']:
#         question = 'What' + ' does ' + sentences.words[bucket['PRP']].lower() + ' ' + sentences.words[bucket['VBZ']].singularize() + '?'

# elif all(key in bucket for key in l10): #'NNP', 'VBZ' in sentence.
#     question = 'What' + ' does ' + sentences.words[bucket['NNP']] + ' ' + sentences.words[bucket['VBZ']].singularize() + '?'

# elif all(key in bucket for key in l13): #'NN', 'VBZ' in sentence.
#     question = 'What' + ' ' + sentences.words[bucket['VBZ']] + ' ' + sentences.words[bucket['NN']] + '?'

# if 'VBZ' in bucket and sentences.words[bucket['VBZ']] == "’":
# 	question = question.replace(" ’ ","'s ")
# 	# print("qqqqqqqqqq:",question)

# if question != '':
# 	print('Question: ',question)