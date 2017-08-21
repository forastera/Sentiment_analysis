from textblob.blob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
<<<<<<< HEAD
import sys
from os import path
=======
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
import string
import json
import re

<<<<<<< HEAD
# Make sure the directory where your script is has folders /data/, /figs/ and /results/
my_project_dir = path.dirname(__file__)

# Input and output files
# dict_file.txt has a collection of pos/neg adjectives, nouns, verbs and adverbs
# clean_text.txt has cleaned text (no stopwords, no lemmatization)
# pos_words.txt and neg_words.txt (after cleaning, lemmatization, not unique)

training_file = "json_train.json"
input_test_file = "test_data.txt"
output_result_file = "textblob_results.txt"
all_words_file = "clean_text.txt"
dict_file = "dict_file.txt"
pos_words_file = "pos_words.txt"
neg_words_file = "neg_words.txt"

# Optional: you can override defaut input test file and output result file 
# by providing command line arguments. Run the script like this:
# python tb_words_classifier.py yourtestfile.txt yourresultsfile.txt

if len(sys.argv) == 3:
    input_test_file = sys.argv[1]
    output_result_file = sys.argv[2]
=======
# change project directory to your own 
my_project_dir = '/Users/anna/Desktop/Projects/NLP/'

# console input for training, testing, and results files
training_file = input("Enter the name of the training file, like \"json_train.json\": ")
input_test_file = input("Enter the name of the test file, like \"test_data.txt\": ")
output_result_file = input("Enter the name of the output result file, like \"results.txt\": ")

stop = stopwords.words('english')
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13

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
<<<<<<< HEAD
res_writer_p = open(my_project_dir + "data/" + pos_words_file,'w')
res_writer_n = open(my_project_dir + "data/" + neg_words_file,'w')
res_writer_all = open(my_project_dir + "data/" + all_words_file,'w')

train_list = []
stop = stopwords.words('english')

# Read json file as text, label ("pos", "neg") line by line 
#print("Processing json")
=======
res_writer_p = open(my_project_dir+'pos_words.txt','w')
res_writer_n = open(my_project_dir+'neg_words.txt','w')

train_list = []

# Read json file as text, label ("pos", "neg") line by line 
print("Processing json")
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13

with open(my_project_dir + training_file, 'r') as fp:
    json_data = json.load(fp)
    for line in json_data:
<<<<<<< HEAD
=======

>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
        text = line['text']
        label = line['label']

# Pre-processing steps:

<<<<<<< HEAD
# 1. normalize verbs like should've => should have, shouldn't => should not, we're => we are' etc
=======
# 1. normalize verbs like should've => should have, shouldn't => should not, we're => are' etc

>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
        text = re.sub(r'(\w+)\'ve', r'\g<1>'+" have", text)
        text = re.sub(r'(\w+)n\'t', r'\g<1>'+" not", text)
        text = re.sub(r'(\w+)\'re', r'\g<1>'+ " are", text)
        text = re.sub(r'(\w+)\'s', r'\g<1>'+" is", text)
        text = re.sub(r'(\w)\'m', r'\g<1>'+" am", text)
        text = re.sub(r'(\w)\'ll', r'\g<1>'+" will", text)
<<<<<<< HEAD
# 2. correct spelling
        blob = TextBlob(text)
        #blob = blob.correct()

        for sentence in blob.sentences:
            for word, tag in sentence.tags: # POS tagging
                word = word.lower()
# 3. Remove non-alphanumeric characters and numbers
                word = re.sub(r'\W|\d', '', word, flags=re.UNICODE)

# 4. Filter stopwords and punctuation
                if (word not in stop) and (word not in string.punctuation) and (len(word)>1):
                    res_writer_all.write(word + " ")
                    w = Word(word)
=======

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
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
# 5. lemmatize according to POS tags:
    #	adjectives = {"JJ", "JJR", "JJS"}
	#	nouns = {"NN", "NNS", "NNP", "NNPS", "NP"}
	#	verbs = {"MD", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}
    # Write adj, nouns, verbs, adjectives into dictionaries where key=lemma, value = frequency
    # Adjectives
<<<<<<< HEAD
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

rp = open(my_project_dir + "data/" +input_test_file,'r')
res_writer = open(my_project_dir + "results/" + output_result_file,'w')
=======
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
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13

for line in rp:
    linelen = len(line)
    line = line[0:linelen-1]
    blob = TextBlob(line)
<<<<<<< HEAD
    blob = blob.correct()
=======
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
    sentence = blob.sentences[0]
    sent_pol = float(sentence.sentiment.polarity)
    sent_val = ''

    if sent_pol >=0.1:
      sent_val = 'pos'
    elif sent_pol <= -0.1:
      sent_val = 'neg'
    else:
      sent_val = 'neutral'

<<<<<<< HEAD
    res_writer.write(line+"\n"+"Sentiment: "+sent_val+"\n\n")

# Print out a dictonary of pos and neg adj, nouns, verbs and adverbs

def print_dict(d):
    w = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
    for word, frequency in w:
       res_writer_dict.write(word + " " + str(frequency)+ "\n")

res_writer_dict = open(my_project_dir + "data/" + dict_file, 'w')

res_writer_dict.write("Word   Frequency" + "\n")
res_writer_dict.write("Positive adjectives:" + "\n")
print_dict(pos_dict_a)
res_writer_dict.write("\n"+"Negative adjectives:" + "\n")
print_dict(neg_dict_a)
res_writer_dict.write("\n"+"Positive nouns:" + "\n")
print_dict(pos_dict_n)
res_writer_dict.write("\n"+"Negative nouns:" + "\n")
print_dict(neg_dict_n)
res_writer_dict.write("\n"+"Positive verbs:" + "\n")
print_dict(pos_dict_v)
res_writer_dict.write("\n"+"Negative verbs:" + "\n")
print_dict(neg_dict_v)
res_writer_dict.write("\n"+"Positive adverbs:" + "\n")
print_dict(pos_dict_r)
res_writer_dict.write("\n"+"Negative adverbs:" + "\n")
print_dict(neg_dict_r)
=======
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
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13



