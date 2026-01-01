# catalog_manager.py
from repositories.catalog_repository import CatalogRepository

class CatalogManager:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, repository):
        if not hasattr(self, '_initialized'):
            self.repository = repository
            self.media_list = self.repository.load_from_xml()
            self._initialized = True
    
    def add_media(self, media):
        self.media_list.append(media)
        print(f"✓ Added: {media.title}")
    
    def view_all_media(self):
        if not self.media_list:
            print("No media items in the catalog.")
            return
        
        print("\n" + "="*50)
        print("ALL MEDIA ITEMS")
        print("="*50)
        
        for i, media in enumerate(self.media_list, 1):
            print(f"[{i}] ", end="")
            media.display_info()
    
    def search_media(self):
        if not self.media_list:
            print("No media items to search.")
            return
        
        search_term = input("Enter search term (title/creator/type): ").strip()
        if not search_term:
            print("Please enter a search term.")
            return
        
        results = []
        for media in self.media_list:
            if media.matches_search(search_term):
                results.append(media)
        
        if results:
            print(f"\nFound {len(results)} result(s):")
            for i, media in enumerate(results, 1):
                print(f"[{i}] ", end="")
                media.display_info()
        else:
            print(f"No media found matching '{search_term}'")
    
    def delete_media(self):
        self.view_all_media()
        
        if not self.media_list:
            return
        
        try:
            choice = int(input("Enter the number of media to delete (0 to cancel): "))
            if choice == 0:
                return
            
            if 1 <= choice <= len(self.media_list):
                media = self.media_list[choice - 1]
                confirm = input(f"Delete '{media.title}'? (y/n): ").lower()
                
                if confirm == 'y':
                    deleted = self.media_list.pop(choice - 1)
                    print(f"✓ Deleted: {deleted.title}")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
    
    def edit_media(self):
        self.view_all_media()
        
        if not self.media_list:
            return
        
        try:
            choice = int(input("Enter the number of media to edit (0 to cancel): "))
            if choice == 0:
                return
            
            if 1 <= choice <= len(self.media_list):
                media = self.media_list[choice - 1]
                print(f"\nEditing: {media.title}")
                print("(Press Enter to keep current value)")
                
                # Get new values
                new_title = input(f"Title [{media.title}]: ").strip()
                if new_title:
                    media.title = new_title
                
                new_year = input(f"Year [{media.year}]: ").strip()
                if new_year and new_year.isdigit():
                    media.year = int(new_year)
                
                new_creator = input(f"Creator [{media.creator}]: ").strip()
                if new_creator:
                    media.creator = new_creator
                
                new_extra = input(f"Extra info [{media.extra}]: ").strip()
                if new_extra:
                    media.extra = new_extra
                
                print("✓ Media updated successfully.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
    
    def generate_report(self):
        try:
            from lxml import etree
            
            # Load XML file
            xml_file = self.repository.file_path
            xslt_file = "xslt/full_catalog.xsl"
            
            # Parse XML and XSLT
            xml_doc = etree.parse(xml_file)
            xslt_doc = etree.parse(xslt_file)
            
            # Transform
            transform = etree.XSLT(xslt_doc)
            result = transform(xml_doc)
            
            # Save to HTML
            output_file = "catalog_report.html"
            with open(output_file, "wb") as f:
                f.write(etree.tostring(result, pretty_print=True))
            
            print(f"✓ Report generated: {output_file}")
        except ImportError:
            print("Error: lxml library not installed. Install with: pip install lxml")
        except Exception as e:
            print(f"Error generating report: {e}")
    
    def save(self):
        self.repository.save_to_xml(self.media_list)
        print("Catalog saved successfully.")