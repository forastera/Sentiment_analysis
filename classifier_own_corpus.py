<<<<<<< HEAD
import string
from itertools import chain
=======

import string
from itertools import chain

>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.corpus import CategorizedPlaintextCorpusReader
<<<<<<< HEAD
from os import path
import nltk
import sys
import re


my_project_dir = path.dirname(__file__)

# change training directory to your own 
# training files need to be in subfolders /pos/ and /neg/
my_corpus_dir = '/Users/anna/nltk_data/corpora/'

# Training, input and output files
training_directory = my_project_dir + "data/"+ "my_chocolatier_reviews"
input_test_file = my_project_dir + "data/" + "test_data.txt"
output_result_file = my_project_dir + "results/" + "nltk_results.txt"

# Optional: you can override defaut input test file and output result file 
# by providing command line arguments. Run the script like this:
# python classifier_own_corpus.py yourtrainingdirectory yourtestfile.txt yourresultsfile.txt

if len(sys.argv) == 4:
    training_directory = sys.argv[1]
    input_test_file = sys.argv[2]
    output_result_file = sys.argv[3]

# Reading in the corpus, documents are stored in folders /neg/ and /pos/

mr = CategorizedPlaintextCorpusReader(training_directory, r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*', encoding='ascii')
=======
import nltk
import sys

# change directories to your own 
my_corpus_dir = '/Users/anna/nltk_data/corpora/'
my_project_dir = '/Users/anna/Desktop/Projects/NLP/'

# console input for training, testing, and results files
training_directory = input("Enter the name of the training directory, like \"my_chocolatier_reviews\": ")
input_test_file = input("Enter the name of the test file, like \"test_data.txt\": ")
output_result_file = input("Enter the name of the output result file, like \"results.txt\": ")

# Reading in the corpus, documents are stored in folders /neg/ and /pos/

mr = CategorizedPlaintextCorpusReader(my_corpus_dir + training_directory, r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*', encoding='ascii')
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13

stop = stopwords.words('english')
# go through the corpus document by document, remove stopwords and puctuation
# fileids() is the name of the file without .txt

print("Building word features...")
<<<<<<< HEAD

def clean_words(word):
	word = word.lower()
	word = re.sub(r'\W|\d', '', word, flags=re.UNICODE)
	return word

documents = [([clean_words(w.lower()) for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]
=======
documents = [([w.lower() for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13

# dictionary with word frequencies
word_features = FreqDist(chain(*[i for i,j in documents]))

# Dividing documents into training set and test set tag
numtrain = int(len(documents) * 90 / 100)
train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag  in documents[numtrain:]]

print("Training...")
classifier = nbc.train(train_set)
print("Done training")
print("Accuracy: ", nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(15)

<<<<<<< HEAD
test_doc = open(input_test_file,'r')
res_writer = open(output_result_file,'w')

# Extract features from the input list of words
def extract_features(words):
    return dict([(clean_words(word), True) for word in words])
=======
# Extract features from the input list of words
def extract_features(words):
    return dict([(word, True) for word in words])

test_doc = open(my_project_dir + input_test_file,'r')
res_writer = open(my_project_dir + output_result_file,'w')
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13

for line in test_doc:
	linelen = len(line)
	line = line[0:linelen-1]
	probabilities = classifier.prob_classify(extract_features(line.split()))
	predicted_sentiment = probabilities.max()
<<<<<<< HEAD
	res_writer.write(line + "\n" +"Sentiment: "+ predicted_sentiment +"\n\n")
=======
	res_writer.write(line+" => sentiment "+ predicted_sentiment +"\n")
>>>>>>> eb6284aed364ab372e5b42ef61cbb260ddfdff13




