# Personal Media Catalog

## 📌 Project Overview

The Personal Media Catalog is a Python console-based application that allows users to manage a collection of personal media such as books, movies, and video games.  
The application uses **XML** for data storage, **XML Schema (XSD)** for validation, and follows important **software design patterns**.  
The project is version-controlled using **Git and GitHub**.

This project was developed as part of a course assignment to demonstrate skills in:
- Python programming
- XML technologies
- Software design patterns
- Version control with Git

---

## 🛠 Technologies Used

- **Python 3**
- **xml.etree.ElementTree** (XML parsing and writing)
- **lxml** (XSLT transformations)
- **XML & XSD**
- **Git & GitHub**

---
## 📁 Project Structure

personal-media-catalog/
│
├── src/
│   ├── main.py
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── media.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── catalog_repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── catalog_manager.py
│   │   └── media_factory.py
│   │
│   └── data/
│       ├── catalog.xml
│       └── media_catalog.xsd
│
├── media_catalog/
│   └── xslt/
│       ├── full_catalog.xsl
│       └── movies_only.xsl



---

## 🧩 Design Patterns Used

### 1️⃣ Singleton Pattern
- Implemented in `CatalogManager`
- Ensures only one instance of the catalog manager exists
- Prevents duplicate data states

### 2️⃣ Factory Pattern
- Implemented in `MediaFactory`
- Centralizes the creation of media objects
- Makes the system easy to extend with new media types

### 3️⃣ Repository Pattern
- Implemented in `CatalogRepository`
- Separates XML persistence logic from business logic
- Improves code organization and maintainability

---

## 📄 XML & XSD

- All media data is stored in `catalog.xml`
- The structure is defined by `media_catalog.xsd`
- XML data is loaded when the application starts
- Data is saved back to XML when the user exits

---

## 📊 XSLT Reporting

The application supports generating HTML reports from the XML catalog using XSLT.

Available stylesheets:
- `full_catalog.xsl` — Displays all media items
- `movies_only.xsl` — Displays only movie items

The generated HTML files can be opened in any web browser.

---

## ▶ How to Run the Application (Windows)

### 1️⃣ Check Python Installation
```bat
python --version

pip install -r requirements.txt

python src/main.py

Python console application to manage a personal media catalog using XML and design patterns


📋 Application Features

Add new media items

View stored media

Persistent storage using XML

Generate HTML reports using XSLT

Simple console-based menu interface

Author

GitHub Username: BirukWagnew



-----------------------------------------------------------------------------------------------



