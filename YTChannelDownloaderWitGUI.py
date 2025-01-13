import os
import threading
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import yt_dlp

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("800x600")

        # Variables
        self.channel_url = tk.StringVar()
        self.output_path = tk.StringVar(value=os.getcwd())
        self.video_info = []
        self.current_video = tk.StringVar(value="No video downloading currently.")
        self.download_progress = tk.IntVar(value=0)

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Input URL
        tk.Label(self.root, text="YouTube Channel/Playlist URL:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.channel_url, width=80).pack(pady=5)

        # Choose Output Path
        tk.Label(self.root, text="Download Path:").pack(pady=5)
        path_frame = tk.Frame(self.root)
        path_frame.pack(pady=5)
        tk.Entry(path_frame, textvariable=self.output_path, width=60).pack(side=tk.LEFT, padx=5)
        tk.Button(path_frame, text="Browse", command=self.browse_output_path).pack(side=tk.LEFT)

        # Start Download Button
        tk.Button(self.root, text="Start Download", command=self.start_download).pack(pady=10)

        # Video Information
        tk.Label(self.root, text="Video Information:").pack(pady=5)
        self.video_listbox = tk.Listbox(self.root, height=10, width=100)
        self.video_listbox.pack(pady=5)

        # Current Download Status
        tk.Label(self.root, text="Current Download:").pack(pady=5)
        tk.Label(self.root, textvariable=self.current_video).pack(pady=5)

        # Progress Bar
        tk.Label(self.root, text="Download Progress:").pack(pady=5)
        self.progress_bar = ttk.Progressbar(self.root, variable=self.download_progress, maximum=100, length=500)
        self.progress_bar.pack(pady=5)

    def browse_output_path(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path.set(path)

    def start_download(self):
        url = self.channel_url.get()
        output_path = self.output_path.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube channel or playlist URL.")
            return

        if not os.path.exists(output_path):
            messagebox.showerror("Error", "Please select a valid output path.")
            return

        # Start download in a separate thread
        threading.Thread(target=self.download_videos, args=(url, output_path)).start()

    def download_videos(self, url, output_path):
        self.video_info = []
        ydl_opts = {
            'format': 'bv*+ba/best',
            'merge_output_format': 'mp4',
            'outtmpl': f'{output_path}/%(uploader)s/%(title)s.%(ext)s',
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'writeautomaticsub': False,
            'progress_hooks': [self.progress_hook],
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                # Get video info
                info = ydl.extract_info(url, download=False)
                self.video_info = info.get('entries', [info])

                # Update video list
                self.video_listbox.delete(0, tk.END)
                for video in self.video_info:
                    self.video_listbox.insert(tk.END, video.get('title', 'Unknown Title'))

                # Start downloading
                ydl.download([url])

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            self.current_video.set(d.get('filename', 'Unknown Video'))
            self.download_progress.set(float(d['_percent_str'].strip('%')))
        elif d['status'] == 'finished':
            self.download_progress.set(100)
            self.current_video.set("Download completed!")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
