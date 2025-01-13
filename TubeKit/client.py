import requests
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from isodate import parse_duration

@dataclass
class VideoInfo:
    id: str
    title: str
    description: str
    channel_title: str
    channel_id: str
    thumbnail_url: str
    published_at: datetime
    duration_: str = ""
    view_count: str = "0"
    like_count: str = "0"
    embed_html_: str = ""

    @property
    def watch_url(self) -> str:
        """Returns the direct URL to view the video on YouTube"""
        return f"https://www.youtube.com/watch?v={self.id}"
    
    @property
    def duration(self) -> str:
        """Returns the duration of the video in HH:MM:SS format"""
        return str(parse_duration(self.duration_)).split("T")[-1]
    
    @property
    def embed_html(self, width: int = 640, height: int = 360) -> str:
        """Generates the HTML code to embed the video"""
        return f'<iframe width="{width}" height="{height}" src="https://www.youtube.com/embed/{self.id}" frameborder="0" allowfullscreen></iframe>'

class YouTubeClient:

    """
    Simple client for the YouTube API.

    Before using the client you must create your API key here in order to use it: https://console.developers.google.com/?hl=en-US
    with YouTube Data API v3 access.
    """
    BASE_URL = "https://www.googleapis.com/youtube/v3"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def _make_request(self, endpoint: str, params: Dict) -> Dict:
        """
        Realiza una petición a la API de YouTube.
        
        Args:
            endpoint: El endpoint de la API a consultar
            params: Parámetros adicionales para la consulta
            
        Returns:
            Dict con la respuesta de la API
            
        Raises:
            requests.exceptions.RequestException: Si hay un error en la petición
        """
        params["key"] = self.api_key
        response = requests.get(f"{self.BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def search_videos(self, query: str, max_results: int = 10, language: str = None, region: str = None) -> List[VideoInfo]:
        """
        Busca videos en YouTube y obtiene información detallada de cada uno.
        
        Args:
            query: Término de búsqueda
            max_results: Número máximo de resultados (default: 10)
            language: Código de idioma para los resultados (ej: 'es')
            region: Código de región para los resultados (ej: 'ES')
            
        Returns:
            Lista de VideoInfo con la información de los videos encontrados
        """
        # Parámetros de búsqueda según la documentación
        search_params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "relevanceLanguage": language,
            "regionCode": region,
            "fields": "items(id/videoId,snippet)"
        }
        
        search_response = self._make_request("search", search_params)
        
        videos = []
        if "items" not in search_response:
            return videos
            
        # Obtener los IDs de los videos encontrados
        video_ids = [item["id"]["videoId"] for item in search_response["items"]]
        
        # Obtener información detallada de los videos
        if video_ids:
            videos_params = {
                "part": "snippet,contentDetails,statistics",
                "id": ",".join(video_ids),
            }
            videos_response = self._make_request("videos", videos_params)
            
            for item in videos_response.get("items", []):
                video = VideoInfo(
                    id=item["id"],
                    title=item["snippet"]["title"],
                    description=item["snippet"]["description"],
                    channel_title=item["snippet"]["channelTitle"],
                    channel_id=item["snippet"]["channelId"],
                    thumbnail_url=item["snippet"]["thumbnails"]["high"]["url"],
                    published_at=datetime.fromisoformat(item["snippet"]["publishedAt"].replace('Z', '+00:00')),
                    duration_=item["contentDetails"]["duration"],
                    view_count=item["statistics"].get("viewCount", "0"),
                    like_count=item["statistics"].get("likeCount", "0"),
                    embed_html_=item.get("player", {}).get("embedHtml", "")
                )
                videos.append(video)
                
        return videos

    def get_video_details(self, video_id: str) -> Optional[VideoInfo]:
        """
        Obtiene los detalles de un video específico.
        
        Args:
            video_id: ID del video de YouTube
            
        Returns:
            VideoInfo con la información del video o None si no se encuentra
        """
        params = {
            "part": "snippet,contentDetails,statistics",
            "id": video_id
        }
        
        response = self._make_request("videos", params)
        
        if not response.get("items"):
            return None
            
        item = response["items"][0]
        return VideoInfo(
            id=item["id"],
            title=item["snippet"]["title"],
            description=item["snippet"]["description"],
            channel_title=item["snippet"]["channelTitle"],
            channel_id=item["snippet"]["channelId"],
            thumbnail_url=item["snippet"]["thumbnails"]["high"]["url"],
            published_at=datetime.fromisoformat(item["snippet"]["publishedAt"].replace('Z', '+00:00')),
            duration_=item["contentDetails"]["duration"],
            view_count=item["statistics"].get("viewCount", "0"),
            like_count=item["statistics"].get("likeCount", "0"),
            embed_html_=item.get("player", {}).get("embedHtml", "")
        )
