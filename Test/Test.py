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
    
    # Get details of a specific video
    #video = client.get_video_details("VIDEO_ID")
    #if video:
    #    print(f"Detalles del video: {video.title}")

    """ 
    Expected output:

    PS C:\Users\MINEDUCYT\OneDrive\Desktop\V0\TubeKit\Test> python Test.py
        ---
        Título: What is Python? Why Python is So Popular?
        Canal: Programming with Mosh
        Vistas: 2049881
        Me gusta: 65514
        Duración: PT4M7S
        Miniatura: https://i.ytimg.com/vi/Y8Tko2YC5hA/hqdefault.jpg
        ---
        Título: What is Python? | Python Explained in 2 Minutes For BEGINNERS.
        Canal: Zero To Mastery
        Vistas: 115907
        Me gusta: 1346
        Duración: PT2M13S
        Miniatura: https://i.ytimg.com/vi/QoIRX37VZpo/hqdefault.jpg
        ---
        , etc...
    
    """