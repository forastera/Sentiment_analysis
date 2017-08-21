import string
import nltk
from nltk.corpus import stopwords
from nltk.corpus import CategorizedPlaintextCorpusReader
from nltk import word_tokenize
from os import path

'''
create corpus:

Annas-Air:~ anna$ mkdir my_movie_reviews
Annas-Air:~ anna$ mkdir my_movie_reviews/pos
Annas-Air:~ anna$ mkdir my_movie_reviews/neg
Annas-Air:~ anna$ echo "This is a great restaurant." > my_movie_reviews/pos/1.txt
Annas-Air:~ anna$ echo "Had a great time at the grove." > my_movie_reviews/pos/2.txt
Annas-Air:~ anna$ echo "Food fit for the ****" > my_movie_reviews/neg/1.txt
Annas-Air:~ anna$ echo "Slow service." > my_movie_reviews/neg/2.txt
Annas-Air:~ anna$ echo "I hated the food there." > my_movie_reviews/neg/3.txt
Annas-Air:~ anna$ echo "Would not recommend." > my_movie_reviews/neg/4.txt
Annas-Air:~ anna$ echo "Too expensive and too crowded" > my_movie_reviews/neg/5.txt
Annas-Air:~ anna$ echo "I loved it!" > my_movie_reviews/pos/3.txt
-bash: !": event not found
Annas-Air:~ anna$ echo "Great place." > my_movie_reviews/pos/3.txt
Annas-Air:~ anna$ echo "Too noisy, but overall good quality." > my_movie_reviews/pos/4.txt
Annas-Air:~ anna$ echo "The carnitas are too die for." > my_movie_reviews/pos/5.txt
Annas-Air:~ anna$ echo "README please" > my_movie_reviews/README
Annas-Air:~ anna$ mv my_movie_reviews/ data/


'''
my_project_dir = path.dirname(__file__)
training_directory = my_project_dir + "data/"+ "my_movie_reviews"
mr = CategorizedPlaintextCorpusReader(training_directory, r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*', encoding='ascii')
stop = stopwords.words('english')
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

#print all words and labels
#for doc in documents:
#	print(doc)


'''
alternatively, create a dictionary from an array of sentences:
'''
train = [('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible.', 'neg')]

all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]

classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features()

test_sentence = "This is the best band I've ever heard!"
test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
print(test_sent_features)
print(classifier.classify(test_sent_features))


