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
        print(f"URL del video: {video.watch_url}")
        print(f"Código embed: {video.embed_html}")
        print("---")
    
    # Get details of a specific video
    #video = client.get_video_details("VIDEO_ID")
    #if video:
    #    print(f"Detalles del video: {video.title}")

    '''
    Output esperado:
    PS C:\\Users\\MINEDUCYT\\OneDrive\\Desktop\\V0\\TubeKit\\Test> python Test.py
    Título: Python for Beginners - Learn Coding with Python in 1 Hour
    Canal: Programming with Mosh
    Vistas: 20133252
    Me gusta: 473550
    Duración: 1:00:06
    Miniatura: https://i.ytimg.com/vi/kqtD5dpn9C8/hqdefault.jpg
    URL del video: https://www.youtube.com/watch?v=kqtD5dpn9C8
    Código embed: <iframe width="640" height="360" src="https://www.youtube.com/embed/kqtD5dpn9C8" frameborder="0" allowfullscreen></iframe>
    ---
    [... otros videos similares ...]
    '''
