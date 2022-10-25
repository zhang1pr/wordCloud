import requests
from bs4 import BeautifulSoup

with open('html.txt','r') as f:
  html = f.read()
soup = BeautifulSoup(html, 'html5lib')

arr = []
table = soup.findAll('div', attrs={'class':'tt'})
for item in table:
	cur = item.find('a')['title']
	cur = ''.join(cur.split(' ')[1:])
	arr.append(cur)

filename = 'title.txt'
with open(filename, 'w', newline='') as f:
	for item in arr:
		f.write(item)
		f.write('\n')
