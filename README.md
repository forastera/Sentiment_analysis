# Sentiment Analysis

#### Classifiers were trained using using a collection of Yelp reviews for chocolatiers (json_train.json).
#### Input file for testing: test_data.txt
#### 3 different ways of doing sentiment analysis in Python
1. nltk NaiveBayesClassifier: classifier_own_corpus.py  
  Output file: nltk_results.txt 
2. TextBlob sentiment: tb_words_classifier.py  
  run this as `pythonw tb_words_classifier.py`    
  Output file: textblob_results.txt  
3. Classifier using a dictionary of emotion words: emotion.py  
  run this as `pythonw emotion.py`  
  Two classifiers: one using the whole dictionary of emotion words (overall score)  
  and the other one only uses words in the training file (weighed score)  
  Output file: emotion_score_results.txt  
  Output figure: plot.png shows distribution of emotion scores in the training file  
  
 
   


