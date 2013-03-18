
import urllib2
import logging

from google.appengine.ext.db import stats

global_stat = stats.GlobalStat.all().get()
#print 'Total bytes stored: %d' % global_stat.bytes
if global_stat is None:
    logging.warning("global stat is none")
else:
    print 'Total entities stored: %d' % global_stat.count
    urllib2.urlopen("http://stevenftable.appspot.com/?v="+str(global_stat.count))