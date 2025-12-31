from models.media import Media

class MediaFactory:
    @staticmethod
    def create_media(media_type, title, year, creator, extra):
        return Media(title, year, creator, extra)