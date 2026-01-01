# media_factory.py
from models.media import Book, Movie, VideoGame, MusicAlbum

class MediaFactory:
    @staticmethod
    def create_media(media_type, title, year, creator, extra):
        if media_type.lower() == "book":
            return Book(title, int(year), creator, extra)
        elif media_type.lower() == "movie":
            return Movie(title, int(year), creator, extra)
        elif media_type.lower() == "game":
            return VideoGame(title, int(year), creator, extra)
        elif media_type.lower() == "music":
            return MusicAlbum(title, int(year), creator, extra)
        else:
            # Generic media as fallback
            from models.media import Media
            return Media("generic", title, year, creator, extra)