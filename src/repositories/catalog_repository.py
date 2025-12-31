import xml.etree.ElementTree as ET

class CatalogRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_from_xml(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        return root

    def save_to_xml(self, root):
        tree = ET.ElementTree(root)
        tree.write(self.file_path, encoding="utf-8", xml_declaration=True)
