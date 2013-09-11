# Procura por imagens na URL especificada e faz download delas
# @autor Augusto Weiand <guto.weiand@gmail.com>
# @date 2013-09-11
# @version 1.0

import urllib2
import re
from os.path import basename
from urlparse import urlsplit

# Aguarda o input do terminal
bang = raw_input("http://")     
url = "http://"+bang

urlContent = urllib2.urlopen(url).read()

# HTML image tag: <img src="url" alt="some_text"/>
#imgUrls = re.findall('a .*?href="(.*?)"', urlContent)

# HTML a image url: <a href="url" alt="some_text"/>
imgUrls = re.findall('a .*?href="(.*?)"', urlContent)

# Realiza o Download
for imgUrl in imgUrls:
    try:
        imgData = urllib2.urlopen(url+imgUrl).read()
        fileName = basename(urlsplit(imgUrl)[2])
        output = open(fileName,'wb')
        output.write(imgData)
        output.close()
        print(fileName)
    except:
        pass