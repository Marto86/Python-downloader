from os import path, rename
from pytube import YouTube as yt

fformat = ""
#Set the path to download folder !!!!!
down_load = desktop = path.expanduser("music")
link = input("Please enter link of the video video: ")
youtube = yt(link)
while fformat != "mp3" and fformat != "mp4":
    fformat = input("Please select fformatt mp3 or mp4? ")


if fformat == "mp4":

    youtube.streams.get_highest_resolution().download(down_load)

elif fformat == "mp3":

    video = youtube.streams.first()
    downloaded_file = video.download(down_load)
    base, ext = path.splitext(downloaded_file)
    new_file = base + '.mp3'
    rename(downloaded_file, new_file)

print("File Downloaded!")

input("Press enter to exit...")