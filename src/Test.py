'''
Created on 18 Oct 2011

@author: Steven
'''
from lib import feedparser

f= open("G:\\top.xml","r")
feed = feedparser.parse("http://www.mitbbs.com/rss/top.xml")
s= feed.channel["title"]
f.close()
