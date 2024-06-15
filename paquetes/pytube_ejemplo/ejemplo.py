from pytube import YouTube

url='https://youtu.be/wTP2RUD_cL0?si=1uudBqNIJQuSkHo7'





def download_mp3(url):
    try:
        audio= YouTube(url)
        audio=audio.streams.filter(only_audio=True).first()
        destino='/home/ignaciogovo/Music'
        audio.download(output_path=destino,  filename=f"{audio.title}.mp3")
        print("The video is downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection")
