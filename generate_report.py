#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.catalog_manager import CatalogManager
from src.repositories.catalog_repository import CatalogRepository

def main():
    repo = CatalogRepository('data/catalog.xml')
    manager = CatalogManager(repo)
    manager.generate_report()
    print("Report generated successfully!")

if __name__ == "__main__":
    main()
