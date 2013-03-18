'''
Created on 3 Oct 2011

@author: Steven
'''
from lib.BeautifulSoup import BeautifulSoup

def handler(sock, url):
    htmlsource=sock.read().decode('gb18030','replace').encode('utf-8') 
    soup = BeautifulSoup(htmlsource)
    content = soup.find("td",{"class":"jiawenzhang-type"})
    if content is None:
        return "content not found"
    return unicode(content)
