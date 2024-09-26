import yt_dlp

url = 'https://www.youtube.com/watch?v=pueMFhjk5uQ&list=RDpueMFhjk5uQ&start_radio=1' 
ydl_opts = {
    'format': 'best', 
    'outtmpl': 'downloaded_video.%(ext)s',  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
