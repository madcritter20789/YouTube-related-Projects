import yt_dlp

def download_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',  # Organize into playlist folder
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'writesubtitles': True,  # Download subtitles
        'subtitleslangs': ['en'],  # Only English subtitles
        'writeautomaticsub': False,  # Exclude auto-generated subtitles
        'ignoreerrors': True,  # Skip videos with errors
        'retries': 10,  # Retry failed downloads
        'nooverwrites': True,  # Skip already downloaded files
        'quiet': False,  # Show detailed progress
        'postprocessors': [
            {  # Merge video and audio into one file
                'key': 'FFmpegMerger',
            },
            {  # Embed subtitles into the final file
                'key': 'FFmpegEmbedSubtitle',
            },
        ],
        'postprocessor_args': {
            'FFmpegEmbedSubtitle': ['-c:s', 'mov_text'],  # Use mov_text codec for MP4
        },
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_playlist(playlist_url)
