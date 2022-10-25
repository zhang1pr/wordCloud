import matplotlib.pyplot as plt
import jieba
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
from PIL import Image

with open('title.txt','r') as f:
  titlefile = f.read()

stopwords = set(map(str.strip, open('stopwords.txt')))

jieba.load_userdict('dict.txt')
wordlist = jieba.cut(titlefile)
space_list = ' '.join(wordlist)


background = np.array(Image.open('i.jpeg')) 
recolorBackground = np.array(Image.open('i.jpeg')) 

wc = WordCloud(
  background_color='white',
  mask=background,
  max_words=1000,
  stopwords=stopwords,
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
