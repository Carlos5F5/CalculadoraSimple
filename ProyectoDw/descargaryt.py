from pytube import YouTube

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)

print("Title: ", yt.title)
print("Descripcion: ", yt.description)

stream = yt.streams.get_highest_resolution()
stream.download()

print("Video Descargado")
