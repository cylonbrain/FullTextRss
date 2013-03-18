'''
Created on 5 Oct 2011

@author: Steven
'''
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import rssreader
import handler_mapping
import logging
class RssGenerator(webapp.RequestHandler):
    def get(self):
        name = self.request.get('site')
        if not handler_mapping.handlers.has_key(name):
            logging.warning("Request rss: %s not found"%name)
            return
        
        rss = rssreader.RssReader(name)
        rss.response_rss(handler_mapping.handlers[name][1], self.response.out)

def main():
    run_wsgi_app(webapp.WSGIApplication([
        ('/rss', RssGenerator),
    ]))

if __name__ == '__main__':
    main()