# Final Project Report  
Personal Media Catalog

---

## 👥 Team Members

- Biruk Wagnew
- Kidus Workagenhu
- Surafel Teshale
- Messay Gebyehu

---

## 📌 Project Summary

This project is a Python console application designed to manage a personal media catalog.  
The application supports storing, viewing, and managing media items such as books and movies using XML for persistent storage.

The project demonstrates:
- XML and XSD usage
- Python object-oriented programming
- Software design patterns
- Git and GitHub version control

---

## 🧩 Design Patterns Implementation

### 1️⃣ Singleton Pattern

**Where used:** `CatalogManager`  
**Why used:**  
The Singleton pattern ensures that only one instance of the catalog manager exists during the application runtime. This prevents duplicate catalogs and ensures consistent data handling.

**How implemented:**  
The `__new__()` method is overridden to control object creation.

---

### 2️⃣ Factory Pattern

**Where used:** `MediaFactory`  
**Why used:**  
The Factory pattern centralizes the creation of media objects and hides object creation logic from the rest of the application.

**Benefits:**
- Cleaner code
- Easy to add new media types in the future

---

### 3️⃣ Repository Pattern

**Where used:** `CatalogRepository`  
**Why used:**  
The Repository pattern separates data persistence logic (XML read/write) from business logic.

**Benefits:**
- Better code organization
- Easier maintenance
- Cleaner architecture

---

## 📄 XML & XSD Usage

- Media data is stored in `catalog.xml`
- The structure is defined by `media_catalog.xsd`
- XML is parsed and written using `xml.etree.ElementTree`

The schema ensures:
- Correct data structure
- Valid data types
- Consistent XML format

---

## 📊 XSLT Reporting

Two XSLT stylesheets were implemented:
- `full_catalog.xsl` — displays all media items
- `movies_only.xsl` — displays only movie items

These stylesheets transform XML data into readable HTML reports.

---

## ⚠ Challenges & Solutions

### Challenge 1: XML Structure Design
**Solution:**  
Started with a simple schema and expanded it step by step.

### Challenge 2: Design Pattern Implementation
**Solution:**  
Separated responsibilities clearly and implemented each pattern in its own module.

### Challenge 3: Git & Version Control
**Solution:**  
Used frequent commits with meaningful messages and maintained a clean commit history.

---

## ✅ Conclusion

This project successfully meets all technical requirements of the assignment.  
It demonstrates strong understanding of XML, Python programming, software design patterns, and version control.

The application is stable, maintainable, and ready for demonstration.
