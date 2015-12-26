from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import csv

#this was inspired and I learned a lot from this here http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/

#set base url  for youtube
BASE_URL = "https://www.youtube.com"

#define functions needed for getting information from playlist
def get_currently_playing(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    boccat = soup.find("div", "  content-alignment    watch-player-playlist  ")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("li","yt-uix-scroller-scroll-unit  currently-playing")]
    return category_links
	
def get_playlist_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    boccat = soup.find("div", "  content-alignment    watch-player-playlist  ")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("li","yt-uix-scroller-scroll-unit ")]
    return category_links
    
    
#read the text file 
with open('playlists.txt') as csvfile:
	next(csvfile) #skip first row
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		FileName = row[0] + '.txt'
		url = row[1]
		#print the name and the url 
		print FileName
		print url
		textexist = os.path.exists(FileName)
		
		#create the playlist by first getting the current and then the playlist
		current = get_currently_playing(url)
		liste = get_playlist_links(url)
		for k in range(0,len(liste)):
			current.append(liste[k])
			
		#write the playlist to text files
		with open(FileName,'w') as txtfile:
			for k in current:
				video = k + "\n"
				txtfile.write(video)
			
