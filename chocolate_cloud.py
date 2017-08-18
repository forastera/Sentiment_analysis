from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path
import numpy as np
import matplotlib.pyplot as plt

d = path.dirname("__file__")


# change project directory and font directory to your own 
my_project_dir = '/Users/anna/Desktop/Projects/NLP/'
font_dir = '/Users/anna/Library/Fonts/RemachineScript_PERSONAL_USE_ONLY.ttf'

# console input for data, mask, result file
input_file = input("Enter the name of the file, like \"pos_all.txt\": ")
input_mask = input("Enter the name of the mask file, like \"heart.png\": ")
output_result_file = input("Enter the name of the output result file, like \"wordclouds_chocolate.png\": ")

text = open(path.join(d, my_project_dir+input_file)).read()
chocolate_mask = np.array(Image.open(my_project_dir+input_mask))
wordcloud1 = WordCloud(
    font_path= font_dir,
    stopwords=STOPWORDS,
    background_color='white',
    mask = chocolate_mask,
    max_words=500,
    width=600,
    height=600).generate(text)

wordcloud1.to_file(output_result_file)

# show
plt.figure(figsize=(10,10))

plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis("off")

plt.show()
#fig.savefig('/Users/anna/Desktop/Projects/NLP/wordclouds_chocolate.png', dpi=400)