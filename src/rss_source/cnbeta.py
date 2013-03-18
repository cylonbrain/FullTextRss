'''
Created on 19 Oct 2011

@author: Steven
'''
from lib.BeautifulSoup import BeautifulSoup
import urllib2
import re

def handler(content, url):
    m=re.search(".*?(\d+)\.htm",url)
    if m is None or len(m.groups())<1:
        return "Failed to parser url"
    
    com_url = "http://www.cnbeta.com/comment/normal/%s.html"%m.groups()[0]
    comment = ""
    try:
        sock = urllib2.urlopen(com_url)
        htmlsource=sock.read().decode('gb18030','replace').encode('utf-8') 
        comment_soup = BeautifulSoup(htmlsource)
        comment = "".join("%s<br/>"%x.text for x in comment_soup.findAll("dd",{"class":"re_detail"}))
    except urllib2.HTTPError:
         comment = ""
    
    
    content_soup = BeautifulSoup(content,fromEncoding="gbk")
    content = content_soup.find("div",{"id":"news_content"})
    
    if content is None:
        return "content not found"
    result = u"%s<br/>Comment%s"%(content,comment)
    return unicode(result)
