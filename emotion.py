import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint
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
with open(emo_file, 'r') as f:
    for emo_line in f.readlines()[46:]:
        emo_info = emo_line.split()
        word = emo_info[0]
        emo = emo_info[1]
        emo_score = int(emo_info[2].strip())
        if word not in emo_dict:
            emo_dict[word] = {}
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

rp = open(my_project_dir+'pos_words.txt','r')
pos_list = [line.rstrip() for line in rp]

n_words_pos = len(pos_list)

rn = open(my_project_dir+'neg_words.txt','r')
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

print("Positive emotions:")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(pos_emo_dict_chocolate))
print("Negative emotions:")
pp.pprint(json.dumps(neg_emo_dict_chocolate))

emotions = ['negative','anger','disgust','fear','sadness', 'positive', 'joy', 'surprise', 'trust','anticipation']

N = 10
ind = np.arange(N)  # the x locations for the groups
width = 0.5

pos = []
neg = []

for em in emotions:
	pos.append(pos_emo_dict_chocolate[em])
	neg.append(neg_emo_dict_chocolate[em])

plt.xkcd()
fig, ax = plt.subplots()

rects1 = ax.bar(ind, pos, width, color='y')
rects2 = ax.bar(ind + width, neg, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Word count')
ax.set_title('Emotion words corpus')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(emotions, rotation=45, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Positive', 'Negative'))

plt.savefig(output_result_file,dpi=400)
plt.show()
