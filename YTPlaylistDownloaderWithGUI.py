import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from threading import Thread


def download_playlist(playlist_url, output_path, progress_label, video_label):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(playlist_title)s/%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'writeautomaticsub': False,
        'ignoreerrors': True,
        'retries': 10,
        'nooverwrites': True,
        'quiet': False,
        'progress_hooks': [lambda d: update_progress(d, progress_label, video_label)],
        'postprocessors': [
            {'key': 'FFmpegMerger'},
            {'key': 'FFmpegEmbedSubtitle'},
        ],
        'postprocessor_args': {
            'FFmpegEmbedSubtitle': ['-c:s', 'mov_text'],
        },
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def update_progress(d, progress_label, video_label):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes', 1)
        progress = int(downloaded / total * 100)
        progress_label.config(text=f"Progress: {progress}%")
        video_title = d.get('info_dict', {}).get('title', 'Unknown')
        video_label.config(text=f"Downloading: {video_title}")
    elif d['status'] == 'finished':
        progress_label.config(text="Download completed!")
        video_label.config(text="")


def start_download(entry_url, output_path_var, progress_label, video_label):
    playlist_url = entry_url.get()
    output_path = output_path_var.get()

    if not playlist_url:
        messagebox.showerror("Error", "Please enter a YouTube playlist URL.")
        return
    if not output_path:
        messagebox.showerror("Error", "Please select an output path.")
        return

    # Clear previous progress
    progress_label.config(text="Starting download...")
    video_label.config(text="")

    # Run the download in a separate thread
    thread = Thread(target=download_playlist, args=(playlist_url, output_path, progress_label, video_label))
    thread.start()


def select_output_path(output_path_var):
    selected_path = filedialog.askdirectory()
    if selected_path:
        output_path_var.set(selected_path)


def create_gui():
    root = tk.Tk()
    root.title("YouTube Playlist Downloader")
    root.geometry("600x400")
    root.resizable(False, False)

    # Input URL
    tk.Label(root, text="YouTube Playlist URL:").pack(pady=5, anchor='w', padx=10)
    entry_url = tk.Entry(root, width=70)
    entry_url.pack(padx=10, pady=5)

    # Output Path
    tk.Label(root, text="Output Path:").pack(pady=5, anchor='w', padx=10)
    output_path_var = tk.StringVar()
    output_path_entry = tk.Entry(root, textvariable=output_path_var, width=50)
    output_path_entry.pack(side='left', padx=10)
    tk.Button(root, text="Browse", command=lambda: select_output_path(output_path_var)).pack(side='right', padx=10)

    # Progress
    progress_label = tk.Label(root, text="Progress: 0%", font=("Arial", 12))
    progress_label.pack(pady=20)

    # Current Video Title
    video_label = tk.Label(root, text="Downloading: None", font=("Arial", 10))
    video_label.pack(pady=10)

    # Start Download Button
    tk.Button(
        root,
        text="Start Download",
        command=lambda: start_download(entry_url, output_path_var, progress_label, video_label),
        bg="green", fg="white"
    ).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
