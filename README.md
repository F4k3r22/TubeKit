# TubeKit: A Simple API Client for YouTube Data API v3

I wanted to simplify the API client to just what I needed so I wouldn't be redundant or get information I didn't want.

## Installation

```bash
git clone https://github.com/F4k3r22/TubeKit.git
cd TubeKit
pip install .
```

## Installation via Pypi

```bash
pip install TubeKit
```

## Basic use:

```python
from TubeKit import YouTubeClient


if __name__ == "__main__":
    # Replace with your API key
    client = YouTubeClient("YOUR_API_KEY")
    
    # Search for videos
    videos = client.search_videos(
        query="Python programming",
        max_results=5,
        language="en",
        region="US"
    )
    
    for video in videos:
        print(f"Título: {video.title}")
        print(f"Canal: {video.channel_title}")
        print(f"Vistas: {video.view_count}")
        print(f"Me gusta: {video.like_count}")
        print(f"Duración: {video.duration}")
        print(f"Miniatura: {video.thumbnail_url}")
        print("---") 
```

If you want to explore more features of TubeKit check the Test folder