from os import listdir
from os.path import isfile, join

import os
import re
from pytube import Playlist

from datetime import datetime
import time


#download From youtube videolist
def videoDownload():
    
    while True:
        #print("waiting...")
        now = datetime.now()
        dt_string = now.strftime("%H:%M")
        if(dt_string=="14:00"):
            
            time.sleep(50)


            path= "H:/project/otomat-maske/python/VIDEOS" #downloaded videos

            
            for f in listdir(path):
                if isfile(join(path, f)):
                    os.remove(path+"//"+f)
                    # print("deleted")

            playlist = Playlist('https://www.youtube.com/playlist?list=PLuIqaTmucCmwdd8xjTfJX_9YJgBxnX4qs') #Playlist linki
            

            #Playlist regex
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

            
            print("Playlist video names")
            #Video download
            for video in playlist.videos:
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=path)
                    

videoDownload()
