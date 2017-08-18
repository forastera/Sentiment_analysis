from textblob.blob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
import string
import json
import re

# change project directory to your own 
my_project_dir = '/Users/anna/Desktop/Projects/NLP/'

# console input for training, testing, and results files
training_file = input("Enter the name of the training file, like \"json_train.json\": ")
input_test_file = input("Enter the name of the test file, like \"test_data.txt\": ")
output_result_file = input("Enter the name of the output result file, like \"results.txt\": ")

stop = stopwords.words('english')

#positive and negative dictionaries for adjectives, nouns, verbs and adverbs
pos_dict_a = defaultdict(int)
neg_dict_a = defaultdict(int)

pos_dict_n = defaultdict(int)
neg_dict_n = defaultdict(int)

pos_dict_v = defaultdict(int)
neg_dict_v = defaultdict(int)

pos_dict_r = defaultdict(int)
neg_dict_r = defaultdict(int)

# Write prossessed positive and negative words into correponding .txt files
res_writer_p = open(my_project_dir+'pos_words.txt','w')
res_writer_n = open(my_project_dir+'neg_words.txt','w')

train_list = []

# Read json file as text, label ("pos", "neg") line by line 
print("Processing json")

with open(my_project_dir + training_file, 'r') as fp:
    json_data = json.load(fp)
    for line in json_data:

        text = line['text']
        label = line['label']

# Pre-processing steps:

# 1. normalize verbs like should've => should have, shouldn't => should not, we're => are' etc

        text = re.sub(r'(\w+)\'ve', r'\g<1>'+" have", text)
        text = re.sub(r'(\w+)n\'t', r'\g<1>'+" not", text)
        text = re.sub(r'(\w+)\'re', r'\g<1>'+ " are", text)
        text = re.sub(r'(\w+)\'s', r'\g<1>'+" is", text)
        text = re.sub(r'(\w)\'m', r'\g<1>'+" am", text)
        text = re.sub(r'(\w)\'ll', r'\g<1>'+" will", text)

# 2. correct spelling

        blob = TextBlob(text)
        blob = blob.correct()
        
	# 7. Write positive and negative words into corresponding .txt files 


        sentence = blob.sentences[0]
        clean_text = []
        w = ''

		# POS tagging
        for word, tag in sentence.tags:
        	word = word.lower()

# 3. Remove non-alphanumeric characters
        	word = re.sub(r'\W|\d', '', word, flags=re.UNICODE)

# 4. filter punctuation and stopwords
        	if (word not in stop) and (word not in string.punctuation) and len(word)>1:
        		w = Word(word)
        		#clean_text.append(w)
# 5. lemmatize according to POS tags:
    #	adjectives = {"JJ", "JJR", "JJS"}
	#	nouns = {"NN", "NNS", "NNP", "NNPS", "NP"}
	#	verbs = {"MD", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}
    # Write adj, nouns, verbs, adjectives into dictionaries where key=lemma, value = frequency
    # Adjectives
        		if tag.startswith('J'):
        			w = w.lemmatize("a")
        			if label == 'pos':
        				pos_dict_a[w] += 1
        				res_writer_p.write(w + "\n")
        			elif label == 'neg':
        				neg_dict_a[w] += 1
        				res_writer_n.write(w + "\n")
    # Nouns
        		elif tag.startswith('N'):
        			w = w.lemmatize()
        			if label == 'pos':
        				pos_dict_n[w] += 1
        				res_writer_p.write(w + "\n")
        			elif label == 'neg':
        				neg_dict_n[w] += 1
        				res_writer_n.write(w + "\n")
    #Verbs
        		elif tag.startswith('V'):
        			w = w.lemmatize("v")
        			if label == 'pos':
        				pos_dict_v[w] += 1
        				res_writer_p.write(w + "\n")
        			elif label == 'neg':
        				neg_dict_v[w] += 1
        				res_writer_n.write(w + "\n")
# Adverbs
        		elif tag.startswith('R'):
        			w = w.lemmatize("r")
        			if label == 'pos':
        				pos_dict_r[w] += 1
        				res_writer_p.write(w + "\n")
        			elif label == 'neg':
        				neg_dict_r[w] += 1
        				res_writer_n.write(w +"\n") 
# Other POS     		
        		else:
        			if label == 'pos':
        				res_writer_p.write(w + "\n")
        			elif label == 'neg':
        				res_writer_n.write(w + "\n")
        		
    

# Classifying input data with TextBlob Pattern analyzer

rp = open(my_project_dir+input_test_file,'r')
res_writer = open(my_project_dir+output_result_file,'w')

for line in rp:
    linelen = len(line)
    line = line[0:linelen-1]
    blob = TextBlob(line)
    sentence = blob.sentences[0]
    sent_pol = float(sentence.sentiment.polarity)
    sent_val = ''

    if sent_pol >=0.1:
      sent_val = 'pos'
    elif sent_pol <= -0.1:
      sent_val = 'neg'
    else:
      sent_val = 'neutral'

    res_writer.write(line+" => sentiment "+sent_val+"\n")

'''
pv = [(k, pos_dict_v[k]) for k in sorted(pos_dict_v, key=pos_dict_v.get, reverse=True)]

print("Negative verbs:")
for w, f in pv:
	if f > 1:
		print(w,f)

nv = [(k, neg_dict_v[k]) for k in sorted(neg_dict_v, key=neg_dict_v.get, reverse=True)]

print("Negative verbs:")
for w, f in nv:
	if f > 1:
		print(w,f)
'''



