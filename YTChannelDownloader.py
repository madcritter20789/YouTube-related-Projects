import os
import yt_dlp

def download_channel_videos(channel_url, output_path='D:/Data-Structure-and-Algorithms/Bots/YTDownloader'):
    """
    Downloads all videos from a specified YouTube channel at the highest quality with audio.

    Args:
        channel_url (str): The URL of the YouTube channel.
        output_path (str): The directory where videos will be saved.
    """
    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    # yt-dlp options for downloading videos at max quality with audio
    ydl_opts = {
        'format': 'bv*+ba/best',  # Best video + best audio, falls back to best if unavailable
        'merge_output_format': 'mp4',  # Ensure output is in MP4 format
        'outtmpl': f'{output_path}/%(uploader)s/%(title)s.%(ext)s',  # Organized by uploader/channel
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
            print(f'Starting download of all videos from {channel_url}...')
            ydl.download([channel_url])
            print('All videos downloaded successfully!')
        except Exception as e:
            print(f"An error occurred: {e}")

# Usage
if __name__ == "__main__":
    channel_url = "https://www.youtube.com/@WLOP"  # Replace with your target channel URL
    download_channel_videos(channel_url)
