from pytube import YouTube

Video_save_directory = "../video downloads"

def download(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(Video_save_directory)
    except:
        print("Something went wrong")
    
    print("Video has been installed")

download(input("URL here: "))