# youtube_checkplaylists
This is  mostly based on this blog entry, I did not write, http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/
This is more like an excercise

It really just ckecks a list of youtube playlitst for any new videos.

the "playlist.txt" file should contain the urls to the playlitst. 

setuplaylists.py just sets up all the text files for the playlists
updateplaylists.py looks at the playlist files and compares them to the number of videos on the web
and writes the Url to the new videos to a news folder and command line

known bugs. 
so far it returns the video that was on the top of the playlist when it was setup, and not the new video.
so I can only see that there is a new video but do not get the actual link to it.

