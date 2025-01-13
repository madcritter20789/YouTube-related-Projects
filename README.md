# YouTube Video Downloader
This repository contains four Python scripts for downloading YouTube content, including entire channel videos, playlists, and associated metadata. It uses the powerful yt-dlp library for efficient video downloading and processing, providing users with a convenient way to batch download YouTube content with advanced features like subtitle downloading and video merging. These scripts also include a graphical user interface (GUI) for a user-friendly experience.

# YouTube Video Downloader (All Channel Videos Download)
**Description:**
This script allows you to download all videos from a specified YouTube channel at the highest quality with audio. It organizes the downloaded videos into folders based on the channel's name and ensures that subtitles (in English) are downloaded where available.

**Features :**

The script uses **yt-dlp** with options to download the best video and audio formats and merges them into a single MP4 file.

Subtitles (if available) are downloaded and embedded into the video file.

The script checks whether the videos have already been downloaded and avoids overwriting them.

The download location is organized by the uploader/channel name.Automatically organizes downloaded files into folders.

**How to Use :**

Set the channel_url to the desired YouTube channel URL.

Run the script, and the videos will be downloaded into the specified output_path.

# YouTube Playlist Downloader
**Description:**
This script is designed to download all videos from a YouTube playlist. It downloads the best video and audio available, merges them into MP4 format, and saves the files in an organized structure based on the playlist title.

**Features :**

The script uses yt-dlp to download videos from the provided playlist URL.

Each video is saved in the appropriate folder based on the playlist name, with subtitles downloaded and embedded if available.

The script supports retries in case of network failures and skips previously downloaded files to avoid redundant downloads.

**How to Use :**

Set the playlist_url to the desired YouTube playlist URL.

Run the script, and the playlist videos will be downloaded into the specified output path.

**Additional Features: GUI Versions**

To provide a more user-friendly experience, GUI versions of both the YouTube channel downloader and playlist downloader are included. These versions utilize tkinter for the interface, offering features like:

**Input Fields:**
Enter the YouTube channel or playlist URL and choose an output directory.

**Progress Bars:** 
Monitor download progress in real-time.

**Current Video Display:** 
See the title of the currently downloading video.

**Installation and Setup:**

Clone the repository or download the script files.

Ensure you have Python 3.6 or later installed.

Install the required dependencies by running:

```bash
  pip install yt-dlp Pillow
```

Run the respective script for your preferred interface (CLI or GUI).

For GUI scripts, ensure you have the tkinter module installed (it is included with standard Python installations).

Execute the script, and follow the instructions to download videos.
