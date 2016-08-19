# sdarm-lessons-archive-downloader
A simple script to download pdf lessons from http://sdarm.org/ website.

## Usage (Linux)
1. Install requests (prevent ImportError: No module named requests)
$ sudo pip install requests

2. Edit languages list you want downloaded
Example: languages = ["ro", "en"]

3. Edit location where you want the files to be saved.
Example: location = "/home/ghitabizau/Backups/"

4. Run script using:
$ python download_pdfs.py

5. Open destination folder, sort files by size, delete empty pdfs (size < 100 KB).
