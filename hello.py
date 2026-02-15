from urllib.parse import urlencode, quote
import os
import pathlib

# Example external web URL
base = "https://example.com/search"
params = {"q": "hello world", "page": 1}
url = base + "?" + urlencode(params)
print("Example web URL:", url)

# File URL (file://) for ad.py
file_path = os.path.abspath("ad.py")
file_url = pathlib.Path(file_path).as_uri()
print("File URL:", file_url)

# Local HTTP URL for ad.py when serving this folder (python -m http.server)
http_url = "http://localhost:8000/" + quote("ad.py")
print("Local HTTP URL (serve with: python -m http.server):", http_url)