# sdarm-lessons-archive-downloader
A simple script to download pdf lessons from http://sdarm.org/ website.

## Usage (Linux)
Install requests (prevent ImportError: No module named requests)

```$ sudo pip install requests```

Edit languages list you want downloaded

```Example: languages = ["ro", "en"]```

Edit location where you want the files to be saved.

```Example: location = "/home/ghitabizau/Backups/"```

Run script using:

```$ python download_pdfs.py```

Open destination folder, sort files by size, delete empty pdfs (size < 100 KB).

[![Contact me on Codementor](https://www.codementor.io/m-badges/ghitab/find-me-on-cm-b.svg)](https://www.codementor.io/@ghitab?refer=badge)
