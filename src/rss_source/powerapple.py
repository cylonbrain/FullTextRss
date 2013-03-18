'''
Created on 11 Mar 2012

@author: Steven
'''
from lib.BeautifulSoup import BeautifulSoup
import re

def handler(sock, url):
    htmlsource=sock.read()
    soup = BeautifulSoup(htmlsource)
    content = soup.find(id=re.compile("postmessage_\d+"),name="td")
    if content is None:
        return "failed to read content"
    return unicode(content)