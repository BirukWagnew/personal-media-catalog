import sys
import os


from repositories.catalog_repository import CatalogRepository
from services.catalog_manager import CatalogManager
from services.media_factory import MediaFactory

def show_menu():
    print("\n=== Personal Media Catalog ===")
    print("1. Add Media")
    print("2. Save and Exit")

def main():
    repo = CatalogRepository("data/catalog.xml")
    manager = CatalogManager(repo)

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            year = input("Year: ")
            creator = input("Creator: ")
            extra = input("Extra info: ")

            media = MediaFactory.create_media(
                "generic", title, year, creator, extra
            )
            manager.add_media(media)

        elif choice == "2":
            manager.save()
            print("Saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
