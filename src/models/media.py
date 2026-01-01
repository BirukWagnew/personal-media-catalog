# media.py
from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, media_type, title, year, creator, extra):
        self.media_type = media_type
        self.title = title
        self.year = year
        self.creator = creator
        self.extra = extra
    
    @abstractmethod
    def display_info(self):
        pass
    
    def __str__(self):
        return f"{self.media_type.capitalize()}: {self.title} ({self.year}) by {self.creator}"
    
    def to_dict(self):
        return {
            'type': self.media_type,
            'title': self.title,
            'year': self.year,
            'creator': self.creator,
            'extra': self.extra
        }
    
    def matches_search(self, search_term):
        search_term = search_term.lower()
        return (search_term in self.title.lower() or 
                search_term in self.creator.lower() or
                search_term in self.media_type.lower())


class Book(Media):
    def __init__(self, title, year, author, pages):
        super().__init__("book", title, year, author, f"{pages} pages")
        self.pages = pages
    
    def display_info(self):
        print(f"📚 Book: {self.title}")
        print(f"   Author: {self.creator}")
        print(f"   Year: {self.year}")
        print(f"   Pages: {self.pages}")
        print()


class Movie(Media):
    def __init__(self, title, year, director, duration):
        super().__init__("movie", title, year, director, f"{duration} minutes")
        self.duration = duration
    
    def display_info(self):
        print(f"🎬 Movie: {self.title}")
        print(f"   Director: {self.creator}")
        print(f"   Year: {self.year}")
        print(f"   Duration: {self.duration} minutes")
        print()


class VideoGame(Media):
    def __init__(self, title, year, developer, platform):
        super().__init__("game", title, year, developer, platform)
        self.platform = platform
    
    def display_info(self):
        print(f"🎮 Game: {self.title}")
        print(f"   Developer: {self.creator}")
        print(f"   Year: {self.year}")
        print(f"   Platform: {self.platform}")
        print()


class MusicAlbum(Media):
    def __init__(self, title, year, artist, tracks):
        super().__init__("music", title, year, artist, f"{tracks} tracks")
        self.tracks = tracks
    
    def display_info(self):
        print(f"🎵 Album: {self.title}")
        print(f"   Artist: {self.creator}")
        print(f"   Year: {self.year}")
        print(f"   Tracks: {self.tracks}")
        print()