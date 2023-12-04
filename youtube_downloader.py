import customtkinter as ctk
import os
from pytube import YouTube, Playlist

def download_video(url, output_path="."):
    yt = YouTube(url)
    video_stream = yt.streams.filter(file_extension="mp4", progressive=True).first()
    print(f"Downloading video: {yt.title}")
    video_stream.download(output_path)
    print("Download complete!")
def download_audio(url, output_path="."):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(f"Downloading audio: {yt.title}")
    audio_stream.download(output_path)
    print("Download complete!")

def download_playlist(playlist_url, output_path=".", download_videos=True):
    playlist = Playlist(playlist_url)
    print(f"Downloading playlist: {playlist.title}")

    for video_url in playlist.video_urls:
        if download_videos:
            download_video(video_url, output_path)
        else:
            download_audio(video_url, output_path)

    print("Playlist download complete!")

def create_gui():
    root = ctk.CTk()
    root.title("YouTube Downloader")

    label_url = ctk.CTkLabel(root, text="Enter YouTube URL or playlist URL:")
    label_url.pack(pady=20)

    entry_url = ctk.CTkEntry(root, width=400)
    entry_url.pack(pady=20)

    label_download_option = ctk.CTkLabel(root, text="Download option:")
    label_download_option.pack(pady=20)
    def switchname():
        answer=switch_download_option.get()
        print (answer)
        if answer==0:
           switch_download_option.configure(text="Audio")
        if answer==1:
            switch_download_option.configure(text="Video")
    switch_download_option = ctk.CTkSwitch(root, text="Audio",command=switchname)
    switch_download_option.pack(pady=10)

    button_download = ctk.CTkButton(root, text="Download")
    button_download.pack(pady=20)
    
        
    def download_clicked():
        url = entry_url.get()
        download_option = "video" if switch_download_option.get() else "audio"

        if "playlist" in url.lower():
            download_playlist(url, download_videos=download_option == "video")
        else:
            if download_option == "video":
                download_video(url)
            else:
                download_audio(url)

    button_download.configure(command=download_clicked)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
