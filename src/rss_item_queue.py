'''
Created on 3 Oct 2011

@author: Steven
'''
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging;
import handler_mapping
from rssreader import RssStore
import urllib2
from datetime import datetime

class WebFetchTask(webapp.RequestHandler):
    def post(self): # should run at most 1/s
        url = self.request.get('url')
        site = self.request.get('site')
        title = self.request.get('title')
        date = self.request.get('date')
        logging.info("load from url: "+ url)
        
        raw = self.read_from_web(url)
        if raw is None:
            return
        logging.info("handler_name "+site)
        handler = handler_mapping.handlers[site][0]
        
        summary = handler(raw, url)
        
        if summary is None:
            logging.error("Failed to parse: "+url)
            return;
        if RssStore.get_by_key_name(site+"_"+url) is not None:
            return
        rssItem = RssStore(key_name=site+"_"+url,
                           site=site,
                           link=url,
                           title=title,
                           date=date,
                           summary=summary)
        rssItem.put()

    def read_from_web(self, url):
        try:
            return urllib2.urlopen(url)
        except:
            logging.error("downloading error on: "+url)
            return None
        
def main():
    run_wsgi_app(webapp.WSGIApplication([
        ('/queue', WebFetchTask),
    ]))

if __name__ == '__main__':
    main()