'''
Created on 3 Oct 2011

There is scheduled task regular hit this ping page, and this will kick off the fetch site rss task

@author: Steven
'''
from rssreader import RssReader
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class WebFetchTask(webapp.RequestHandler):
    def get(self):
        site = self.request.get('site')
        if site is None or site=='':
            print "Need parameter"
            return
        rss = RssReader(site)
        rss.update_cache()

def main():
    run_wsgi_app(webapp.WSGIApplication([
        ('/ping', WebFetchTask),
    ]))

if __name__ == '__main__':
    main()