from pytube import Playlist
from pytube import YouTube
import os
import moviepy.editor as mp
import re

pl = Playlist("https://www.youtube.com/playlist?list=PLySKRj7KSLYgS9jVyonZTFpiYkIzZXF2-")

#Mention the folder path where you want to download videos
savePath = "D:\Pranto\GitHub\Youtube_download_mp3\store"

#Mention the start and end video numbers of that playlist in 0-based index
start = 0
end = 11

vidNum = start+1
for video in pl.videos[start:end]:
    print(vidNum,". ",video.title)
    print("..............Downloading...........")
    video.streams.filter(progressive=True).get_by_resolution("720p").download(savePath)
    print(vidNum,". Finished.....!")
    vidNum = vidNum + 1


print('-------- All Download complete--------------')

# folder = savePath

# for file in os.listdir(folder):
#     if re.search('mp4',file):
#         mp4_path = os.path.join(folder,file)
#         mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
#         new_file = mp.AudioFileClip(mp4_path)
#         new_file.write_audiofile(mp3_path)
#         os.remove(mp4_path)

# print('Conversion complete')
