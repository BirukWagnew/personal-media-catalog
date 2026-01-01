# catalog_repository.py
import xml.etree.ElementTree as ET
from models.media import Media

class CatalogRepository:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_from_xml(self):
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            
            media_items = []
            for media_elem in root.findall('media'):
                media_type = media_elem.find('type').text
                title = media_elem.find('title').text
                year = int(media_elem.find('year').text)
                creator = media_elem.find('creator').text
                extra = media_elem.find('extra').text
                
                from services.media_factory import MediaFactory
                media = MediaFactory.create_media(media_type, title, year, creator, extra)
                media_items.append(media)
            
            return media_items
        except FileNotFoundError:
            # Create new catalog if file doesn't exist
            root = ET.Element("catalog")
            tree = ET.ElementTree(root)
            tree.write(self.file_path, encoding="utf-8", xml_declaration=True)
            return []
        except Exception as e:
            print(f"Error loading catalog: {e}")
            return []
    
    def save_to_xml(self, media_list):
        # Create root element
        root = ET.Element("catalog")
        
        # Add each media item to XML
        for media in media_list:
            media_elem = ET.SubElement(root, "media")
            
            # Convert media to dictionary and create elements
            media_dict = media.to_dict()
            for key, value in media_dict.items():
                elem = ET.SubElement(media_elem, key)
                elem.text = str(value)
        
        # Write to file
        tree = ET.ElementTree(root)
        tree.write(self.file_path, encoding="utf-8", xml_declaration=True)