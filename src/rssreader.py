'''
Created on 2 Oct 2011

@author: Steven
'''

import encodings
encodings.aliases.aliases['gb2312'] = 'gb18030'
from lib import feedparser
from google.appengine.ext import db
import logging
from lib import PyRSS2Gen
import datetime
from google.appengine.api import taskqueue
import handler_mapping

class RssStore(db.Model):
    site=db.StringProperty(required=True)
    link=db.LinkProperty(required=True)
    title=db.StringProperty(required=True)
    summary=db.TextProperty(required=True)
    date=db.StringProperty(required=True)
    create=db.DateTimeProperty(auto_now_add=True)
    
class RssReader(object):
    def __init__(self, site):
        self.site=site
        
    def get_rss(self, url):
        return feedparser.parse(url)
    
    def update_cache(self):
        rss_url = handler_mapping.handlers[self.site][1]
        rss = self.get_rss(rss_url)
        for item in rss["items"]:
            link = item[ "link" ]
            entity = RssStore.get_by_key_name(self.site+"_"+link)
            count = 0
            if entity is None:
                logging.debug("handler(update_cache): "+self.site)
                count=count+1
                taskqueue.add(url='/queue',queue_name=self.site+"-queue", params={'url': link,
                                                                                    "title":item["title"],
                                                                                    "date":item["date"],
                                                                                    "site":self.site})
        return "updated: %s"%count
    
    def response_rss(self, rss_url, out):
        rssList=[]
        rss = self.get_rss(rss_url)
        
        for item in rss["items"]:
            entity = RssStore.get_by_key_name(self.site+"_"+item["link"])
            summary =""
            if entity is None:
                logging.debug("handler(response_rss): "+self.site)
                taskqueue.add(url='/queue',queue_name=self.site+"-queue", params={'url': item["link"],
                                                                                    "title":item["title"],
                                                                                    "date":item["date"],
                                                                                    "site":self.site})
                summary = "no content"
            else:
                summary = entity.summary
                
            rssitem = PyRSS2Gen.RSSItem(
                 title = item["title"],
                 link = item["link"],
                 description = summary,
                 pubDate = item["updated"])
            if hasattr(item,"id"):
                rssitem.guid = item.id
            rssList.append(rssitem)
            
        rss = PyRSS2Gen.RSS2(title = rss[ "channel" ][ "title" ],
                    link = rss_url,
                    description = rss[ "channel" ][ "description" ],
                    lastBuildDate = datetime.datetime.now(),
                    items = rssList)
        rss.write_xml(out, encoding="utf-8")
        
            