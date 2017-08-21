# Sentiment Analysis

#### Classifiers were trained using using a collection of Yelp reviews for chocolatiers (json_train.json).
#### Input file for testing: test_data.txt
#### 3 different ways of doing sentiment analysis in Python
1. nltk NaiveBayesClassifier: classifier_own_corpus.py  
  run this script as `classifier_own_corpus.py`   
  or optionally, provide own input and output files:  
  `classifier_own_corpus.py yourtrainingdirectory yourtestfile.txt yourresultsfile.txt`  
  Output file: nltk_results.txt 
2. TextBlob sentiment: tb_words_classifier.py  
  run this script as `python tb_words_classifier.py`   
  or optionally, provide own input and output files:  
  `tb_words_classifier.py yourtestfile.txt yourresultsfile.txt`  
  Output file: textblob_results.txt  
3. Classifier using a dictionary of emotion words: emotion.py  
  run this script as `pythonw emotion.py` 
  or optionally, provide own input and output files:    
  `pythonw emotion.py yourtestfile.txt yourresultsfile.txt`  
  Two classifiers: one using the whole dictionary of emotion words (overall score)  
  from NRC-Emotion-Lexicon (http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)  
  and the other one only uses words in the training file (weighed score)  
  Output file: emotion_score_results.txt  
  Output figure: plot.png shows distribution of emotion scores in the training file  

 chocolate_cloud.py creates a wordcloud with either positive or negative words from the corpus.  
 more about creating wordclouds: (https://amueller.github.io/word_cloud/auto_examples/masked.html)  
 run this script as `pythonw chocolate_cloud.py` by default, a cloud of positive words is created  
 or optionally, provide own input and output files:  
 `pythonw chocolate_cloud.py yourinputfile.txt yourmask.png yourresultfig.png` 
 Output file: pos_wordcloud.png  

