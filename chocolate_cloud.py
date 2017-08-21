from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from os import path
import sys


# change project directory and font directory to your own 
my_project_dir = path.dirname(__file__)
font_dir = '/Users/anna/Library/Fonts/RemachineScript_PERSONAL_USE_ONLY.ttf'

# data, mask, result file
input_file = my_project_dir + "data/" + "pos_words.txt"
input_mask = my_project_dir + "figs/" + "heart.png"
output_result_file = my_project_dir + "figs/" + "pos_wordcloud.png"

# Optional: you can override defaut input file, mask and output result file 
# by providing command line arguments. Run the script like this:
# pythonw chocolate_cloud.py yourinputfile.txt yourmask.png yourresultfig.png

if len(sys.argv) == 4:
    input_file = my_project_dir + "data/" + sys.argv[1]
    input_mask = my_project_dir + "figs/" + sys.argv[2]
    output_result_file = my_project_dir + "figs/" + sys.argv[3]

text = open(path.join(input_file)).read()
chocolate_mask = np.array(Image.open(input_mask))
wordcloud1 = WordCloud(
    font_path= font_dir,
    stopwords=STOPWORDS,
    background_color='white',
    mask = chocolate_mask,
    max_words=500,
    width=500,
    height=500).generate(text)

wordcloud1.to_file(output_result_file)

# show
plt.figure(figsize=(10,10))

plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis("off")

plt.show()