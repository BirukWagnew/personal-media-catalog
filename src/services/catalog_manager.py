from repositories.catalog_repository import CatalogRepository

class CatalogManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, repository):
        self.repository = repository
        self.root = self.repository.load_from_xml()

    def add_media(self, media):
        media_elem = self.root.makeelement("media", {})
        self.root.append(media_elem)

        for key, value in vars(media).items():
            elem = self.root.makeelement(key, {})
            elem.text = str(value)
            media_elem.append(elem)

    def save(self):
        self.repository.save_to_xml(self.root)