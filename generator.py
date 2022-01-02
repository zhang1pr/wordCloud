import matplotlib.pyplot as plt
import jieba
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import numpy as np
from PIL import Image

with open('title.txt','r') as f:
  textfile = f.read()

wordlist = jieba.lcut(textfile)
space_list = ' '.join(wordlist)
print(space_list)
background = np.array(Image.open('3.png')) 
recolorBackground = np.array(Image.open('iii1.jpeg')) 

wc = WordCloud(
  background_color='white',
  mask=background,
  max_words=1000,
  stopwords=STOPWORDS,
  font_path='xiaolai1.ttf',
  min_font_size=10,
  max_font_size=80,
  relative_scaling=0.25,
  random_state=50, 
  scale=2
).generate(space_list) 

image_color = ImageColorGenerator(recolorBackground)
wc.recolor(color_func=image_color)
wc.to_file('res.png')
