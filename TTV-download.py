import urllib

url_opener = urllib.URLopener()

path = "E:\[My Folder]\Private\Dropbox\GOALTIME\\"
ttv_list = "http://super-pomoyka.us.to/trash/ttv-list/"
allfon_list = "https://allfon.tv/autogenplaylist/"
playlists = [
    "ttv.m3u",
    "ttv.sport.player.m3u"
]

def download_file():
    for playlist in playlists:
        print "Downloading {0} to {1}..........".format(playlist, path)
        url_opener.retrieve(ttv_list + playlist, path + playlist)
        print "Downloading {0} to {1}..........".format(playlist, "current directory")
        url_opener.retrieve(ttv_list + playlist, playlist)

download_file()

# TODO: Move to the one function
import urllib2
import ssl
import shutil

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'pl-PL,pl;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request("https://allfon.tv/autogenplaylist/allfontv.m3u", headers=hdr)

try:
    page = urllib2.urlopen(req,context=context)
except urllib2.HTTPError, e:
    print e.fp.read()

output = open('allfontv.m3u','wb')
output.write(page.read())
output.close()

shutil.copy2('allfontv.m3u', path)

