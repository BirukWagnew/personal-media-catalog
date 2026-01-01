# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from repositories.catalog_repository import CatalogRepository
from services.catalog_manager import CatalogManager
from services.media_factory import MediaFactory

def show_menu():
    print("\n" + "="*50)
    print("PERSONAL MEDIA CATALOG")
    print("="*50)
    print("1. Add New Media")
    print("2. View All Media")
    print("3. Search Media")
    print("4. Delete Media")
    print("5. Edit Media")
    print("6. Generate HTML Report")
    print("7. Save and Exit")
    print("="*50)

def add_media_ui(manager):
    print("\nAdd New Media")
    print("-" * 30)
    
    # Media type selection
    print("Media Types: book, movie, game, music")
    media_type = input("Media type: ").strip().lower()
    
    # Validate media type
    valid_types = ['book', 'movie', 'game', 'music']
    if media_type not in valid_types:
        print(f"Invalid type. Please choose from: {', '.join(valid_types)}")
        return
    
    # Get media details
    title = input("Title: ").strip()
    if not title:
        print("Title is required!")
        return
    
    year = input("Year: ").strip()
    if not year.isdigit():
        print("Year must be a number!")
        return
    
    creator_label = "Author" if media_type == "book" else \
                   "Director" if media_type == "movie" else \
                   "Developer" if media_type == "game" else \
                   "Artist"
    creator = input(f"{creator_label}: ").strip()
    
    extra_label = "Pages" if media_type == "book" else \
                  "Duration (minutes)" if media_type == "movie" else \
                  "Platform" if media_type == "game" else \
                  "Number of tracks"
    extra = input(f"{extra_label}: ").strip()
    
    # Create and add media
    try:
        media = MediaFactory.create_media(media_type, title, int(year), creator, extra)
        manager.add_media(media)
    except Exception as e:
        print(f"Error adding media: {e}")

def main():
    # Initialize repository and manager
    repo = CatalogRepository("data/catalog.xml")
    manager = CatalogManager(repo)
    
    print("Welcome to Personal Media Catalog!")
    print(f"Loaded {len(manager.media_list)} media items.")
    
    while True:
        show_menu()
        choice = input("Your choice (1-7): ").strip()
        
        if choice == "1":
            add_media_ui(manager)
        
        elif choice == "2":
            manager.view_all_media()
        
        elif choice == "3":
            manager.search_media()
        
        elif choice == "4":
            manager.delete_media()
        
        elif choice == "5":
            manager.edit_media()
        
        elif choice == "6":
            manager.generate_report()
        
        elif choice == "7":
            manager.save()
            print("\nThank you for using Personal Media Catalog!")
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()