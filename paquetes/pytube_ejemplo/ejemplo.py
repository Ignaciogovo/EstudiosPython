from pytube import YouTube
import re








def download_mp3(url):
    try:
        audio= YouTube(url)
        audio=audio.streams.filter(only_audio=True).first()
        destino='/home/ignaciogovo/Music'
        nombre=audio.title.replace('/','_').replace(' ','_')
        nombre= re.sub(r'[<>:"/\|*?]', "-" , nombre)
        audio.download(output_path=destino,  filename=f"{nombre}.mp3")
        print("The video is downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection")





url_='https://www.youtube.com/watch?v=rtt8aXRU_C8'
download_mp3(url_)