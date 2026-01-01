# run.py
import os
import sys

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Check if lxml is installed
try:
    import lxml
except ImportError:
    print("Installing required packages...")
    os.system("pip install lxml")

# Create necessary directories
os.makedirs("data", exist_ok=True)
os.makedirs("xslt", exist_ok=True)

# Run the application
from src.main import main

if __name__ == "__main__":
    main()