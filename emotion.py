import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint
<<<<<<< HEAD
import sys
import json
import re
import nltk
from nltk.corpus import stopwords
from os import path
from textblob.blob import TextBlob
from textblob import Word
import string
import collections
 
my_project_dir = path.dirname(__file__)
stop = stopwords.words('english')

# Emotion dictionary, see more here: http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm
emo_file = my_project_dir+"data/"+'NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'

# Input test file
input_file = my_project_dir + "data/" + "test_data.txt"

# Saving the result plot
output_result_fig = my_project_dir + "figs/" + "plot.png"

# Output text result
output_result_file = my_project_dir + "results/" + "emotion_score_results.txt"

# Optional: you can override input text file and defaut output files
# by providing a command line argument.
# Run the script like this:
# pythonw emotion.py yourtestfile.txt yourresults.txt yourplot.png

if len(sys.argv) == 4:
    input_file = my_project_dir + "data/" + sys.argv[1]
    output_result_file = my_project_dir + "results/"+ sys.argv[2]
    output_result_fig = my_project_dir + "figs/" + sys.argv[3]
    
neg_list = []
pos_list = []
emo_dict = {}
emo_pol = {}
=======
import json

# change project directory to your own 
my_project_dir = '/Users/anna/Desktop/Projects/NLP/'

# Intput for saving the result plot
output_result_file = input("Enter the name of the output result file, like \"plot.png\": ")
# make emotion dictionary
emo_file = my_project_dir+'NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt' 

neg_list = []
pos_list = []
emo_dict = {}
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
with open(emo_file, 'r') as f:
    for emo_line in f.readlines()[46:]:
        emo_info = emo_line.split()
        word = emo_info[0]
        emo = emo_info[1]
        emo_score = int(emo_info[2].strip())
        if word not in emo_dict:
<<<<<<< HEAD
            emo_dict[word] = {}      
=======
            emo_dict[word] = {}
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
        emo_dict[word][emo] = emo_score

pos_emo_dict_chocolate = {'anger': 0,
                    'anticipation': 0,
                    'disgust': 0,
                    'fear': 0,
                    'joy': 0,
                    'negative': 0,
                    'positive': 0,
                    'sadness': 0,
                    'surprise': 0,
                    'trust': 0}

neg_emo_dict_chocolate = {'anger': 0,
                    'anticipation': 0,
                    'disgust': 0,
                    'fear': 0,
                    'joy': 0,
                    'negative': 0,
                    'positive': 0,
                    'sadness': 0,
                    'surprise': 0,
                    'trust': 0}

<<<<<<< HEAD

# Comparing emotion dictionary to the list of positive and negative words
rp = open(my_project_dir+"data/"+'pos_words.txt','r')
=======
rp = open(my_project_dir+'pos_words.txt','r')
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
pos_list = [line.rstrip() for line in rp]

n_words_pos = len(pos_list)

<<<<<<< HEAD
rn = open(my_project_dir+"data/"+'neg_words.txt','r')
=======
rn = open(my_project_dir+'neg_words.txt','r')
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
neg_list = [line.rstrip() for line in rn]

n_words_neg = len(neg_list)

for word in neg_list:
    if word not in emo_dict:
        continue
    for emo in emo_dict[word]:
        neg_emo_dict_chocolate[emo] += neg_list.count(word) * emo_dict[word][emo] #/ n_words_neg * 100.

for word in pos_list:
    if word not in emo_dict:
        continue
    for emo in emo_dict[word]:
        pos_emo_dict_chocolate[emo] += pos_list.count(word) * emo_dict[word][emo] #/ n_words_pos 

<<<<<<< HEAD

pos_emotions = ['positive', 'joy', 'surprise', 'trust','anticipation']
neg_emotions = ['negative', 'anger', 'disgust', 'fear', 'sadness']
emotions = pos_emotions + neg_emotions

# Sentiment score is calculated by looking up words in emotional dictionary
# Return the sum of positive emotional scores - the sum of negative emotional scores
def return_emo_score(word):
    neg_count = 0
    pos_count = 0
    if word in emo_dict:
        for emo in emotions:
            if emo in pos_emotions:
                pos_count += emo_dict[word][emo]
            if emo in neg_emotions:
                neg_count += emo_dict[word][emo]
    return pos_count - neg_count

# Weighed score: only the emotional scores of words that occur in training lists
# Look up words that occur exclusively in positive or negative word lists (not in both)
# Add emotional score for positive or negative emotion (not both)
# Multiply the resulting emotional score by word frequency in the list
# Return the sum of positive emotional scores - the sum of negative emotional scores
def return_corpus_weights(word):
    neg_count = 0
    pos_count = 0
    if word == 'not':
        neg_count += 1
    if word in emo_dict:    
        if (word in pos_list) and (word not in neg_list):
            for emo in emotions:
                if emo in pos_emotions:
                    pos_count += pos_list.count(word) * emo_dict[word][emo]  
        if (word in neg_list) and (word not in pos_list):
            for emo in emotions:
                if emo in neg_emotions:
                    neg_count += neg_list.count(word) * emo_dict[word][emo] 
    return pos_count - neg_count

# Remove non-word characters and numbers
# Lemmatize according to parts of speech
def clean_words(word, tag):
    word = word.lower()
    word = re.sub(r'\W|\d', '', word, flags=re.UNICODE)
    w = Word(word)
    if tag.startswith('J'):
        w = w.lemmatize("a")
# Nouns
    elif tag.startswith('N'):
        w = w.lemmatize()
#Verbs
    elif tag.startswith('V'):
        w = w.lemmatize("v")

# Adverbs
    elif tag.startswith('R'):
        w = w.lemmatize("r")
 
# Other POS             
    return w

# Deal with test data
test_doc = open(input_file,'r')
res_writer = open(output_result_file,'w')

for line in test_doc:
    word_list = []
    score = 0
    weighed_score = 0
    sentiment = ''
    emotions_dict = collections.OrderedDict()
    for emo in emotions:
        emotions_dict[emo] = 0

    linelen = len(line)
    res_writer.write(line)
    line = line[0:linelen-1]
    blob = TextBlob(line)

    for sentence in blob.sentences:
        for word, tag in sentence.tags:
            w = clean_words(word, tag)
            word_list.append(w)

# Calculate overall score and weighed score 
# by multiplying individual word scores and their respective word frequencies
# and adding them up for all words in a review
    u_list = list(set(word_list))
    for word in u_list:
        score += word_list.count(word) * return_emo_score(word)
        weighed_score += word_list.count(word) * return_corpus_weights(word)
        if word in emo_dict:
            for emo in emotions:
                emotions_dict[emo] += emo_dict[word][emo] 
    if score >0:
         sentiment = "positive"
    elif score <0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    res_writer.write("Sentiment: " + sentiment + "\n")
    res_writer.write("Score: " + str(score) + "\n")

    if weighed_score >0:
         sentiment = "positive"
    elif weighed_score <0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    res_writer.write("Weighed sentiment: " + sentiment + "\n")
    res_writer.write("Weighed score: " + str(weighed_score) + "\n")

    s = ''
    for emo in emotions_dict:
        s+="\""+ emo + "\": " + str(emotions_dict[emo]) + "\n"

    res_writer.write(s + "\n")


# Visualization of pos and neg words in a xkcd style bar chart
=======
print("Positive emotions:")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(pos_emo_dict_chocolate))
print("Negative emotions:")
pp.pprint(json.dumps(neg_emo_dict_chocolate))

emotions = ['negative','anger','disgust','fear','sadness', 'positive', 'joy', 'surprise', 'trust','anticipation']

>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
N = 10
ind = np.arange(N)  # the x locations for the groups
width = 0.5

pos = []
neg = []

for em in emotions:
	pos.append(pos_emo_dict_chocolate[em])
	neg.append(neg_emo_dict_chocolate[em])

<<<<<<< HEAD
# Using plt.xkcd() “Humor Sans” font should be installed: it is not included with matplotlib.
=======
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
plt.xkcd()
fig, ax = plt.subplots()

rects1 = ax.bar(ind, pos, width, color='y')
rects2 = ax.bar(ind + width, neg, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Word count')
ax.set_title('Emotion words corpus')
ax.set_xticks(ind + width / 2)
<<<<<<< HEAD
ax.set_xticklabels(emotions, rotation=45, fontsize=8)
ax.legend((rects1[0], rects2[0]), ('Positive', 'Negative'))
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(bottom=0.15)
plt.savefig(output_result_fig, dpi=400)
=======
ax.set_xticklabels(emotions, rotation=45, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Positive', 'Negative'))

plt.savefig(output_result_file,dpi=400)
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
plt.show()
