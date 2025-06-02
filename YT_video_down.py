import pytube

url = input("Enter the URL of the video you want to download: ")
yt = pytube.YouTube(url)
yt.streams.first().download()
print("Downloaded,url")




