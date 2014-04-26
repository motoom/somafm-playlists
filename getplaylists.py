
# Download somafm.com playlists, for use in VLC, XMMS or iTunes et.al.
#
# Software by Michiel Overtoom, motoom@xs4all.nl
       
import urllib
import urllib2
import xml.dom.minidom


def playlistURLs():
    data = urllib2.urlopen("http://api.somafm.com/channels.xml").read()
    dom = xml.dom.minidom.parseString(data) 
    channels = dom.getElementsByTagName("channel")
    for channel in channels:
        playlists = channel.getElementsByTagName("fastpls")
        for playlist in playlists:
            if playlist.attributes["format"].value == "mp3":
                yield playlist.firstChild.wholeText
            

for url in list(playlistURLs()):
    _, plsfilename = url.rsplit("/", 1) 
    print "Retrieving %s from %s" % (plsfilename, url)
    data = urllib2.urlopen(url).read()
    with open(plsfilename, "wt") as f:
        f.write(data)
