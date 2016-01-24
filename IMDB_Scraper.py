from bs4 import BeautifulSoup
import urllib2

url = "http://www.imdb.com/chart/top?ref_=nv_mv_250_6"
test_url = urllib2.urlopen(url)
readhtml = test_url.read()
test_url.close()

soup = BeautifulSoup(test_url)
for movie in soup.find_all('td','title'):
	title = movie.find('a').contents[0]
	genres = movie.find('span','genre').findAll('a')
	genres = [g.contents[0] for g in genres]
	runtime = movie.find('span','runtime').contents[0]
	rating = movie.find('span','value').contents[0]
	print title,genres,runtime,rating
