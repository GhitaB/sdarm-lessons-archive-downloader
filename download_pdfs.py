import requests

prefix = "http://sdarmorg.listentosermon.net/files/publications/periodicals/sbl/pdf/"
languages = ["ro", "en"]
location = "/home/ghitabizau/Backups/"
# sbl1945_1_en.pdf


def download_file(url, filename):
    result = True
    try:
        r = requests.get(url)
        open(filename, 'wb').write(r.content)
    except:
        result = False
    return result

for year in range(1940, 2020):
    for number in range(1, 5):
        for lang in languages:
            sufix = "sbl" + str(year) + "_" + str(number) + "_" + lang + ".pdf"
            url = prefix + sufix
            filename = location + sufix
            print "Downloadind " + url
            result = download_file(url, filename)
            print result
