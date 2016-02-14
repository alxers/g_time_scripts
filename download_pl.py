from random import randint
import urllib

urlopener = urllib.URLopener()
url = "https://aladex.ru/iptv/"
file_name = "iptv-"
file_extension = ".m3u"

def getRandomNum():
    return randint(0, 400)
    
def getFileName(file_name, rand_num, file_extension):
    file_num = str(rand_num)
    full_name = file_name + file_num + file_extension
    return full_name
    
    
def getUrlAndFileName(url, file_name):
    return [url + file_name, file_name]


# f1 = getUrlAndFileName(url, getFileName(file_name, getRandomNum(), file_extension))
# urlopener.retrieve(f1[0], f1[1])

def retrieveFiles():
    print "Downloading"
    for num in range(5):
        url_and_name = getUrlAndFileName(url, getFileName(file_name, getRandomNum(), file_extension))
        url1 = url_and_name[0]
        name = url_and_name[1]
        print(url1, name)
        urlopener.retrieve(url1, name)

retrieveFiles()
