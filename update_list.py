from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import csv
import time

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
		#print the name
		print FileName
		textexist = os.path.exists(FileName)
	    
	    #create the playlist by first getting the current and then the playlist
		current = get_currently_playing(url)
		liste = get_playlist_links(url)
		for k in range(0,len(liste)):
			current.append(liste[k])
		
		oldlist=[]
		with open(FileName,'r') as txtfile:
			txtreader = csv.reader(txtfile,delimiter=',')
			for txtrow in txtreader:
				oldlist.append(row)
				
		if (len(oldlist)==len(current)): # nothing new because the same number of items in playlist
			print "nothing new in:", FileName
		else:
			current_day_file="news/" + time.strftime("%d_%m_%Y") +'.txt' 
			if (not os.path.exists("news/")): #check if news directory exitst if not make one
				os.makedirs("news")
			with open(current_day_file,'ar+') as newsfile:
				newsfile.write((FileName + "\n"))
			Number_new = len(current)-len(oldlist)
			if (oldlist[0]==current[0]): #First item is the same the last needs to be read
				for k in range(0,Number_new):
					print "new video", current[len(current)-k-1]
					
					#write new videos to current day file
					with open(current_day_file,'ar+') as newsfile:
						newsfile.write(current[k] + "\n")
						
					#new lines can simply be appended to file
					with open(FileName,'a') as txtfile2:
						video = current[len(current)-k-1] + "\n"
						FileName.write(video)
						
			else:
				for k in range(0,Number_new):
					print "new video", current[k]
					
					#write new videos to current day file
					with open(current_day_file,'ar+') as newsfile:
						newsfile.write(current[k] + "\n")
				#simply rewrite the file
				with open(FileName,'w')  as txtfile2:
					for k in range(0,len(current)):
						video = current[k] + "\n"
						txtfile2.write(video)
					
					
				
