'''
Created on 4 Oct 2011

@author: Steven
'''
from rss_source import mitbbs
from rss_source import cnbeta
from rss_source import powerapple

handlers = {"mitbbs": (mitbbs.handler,"http://www.mitbbs.com/rss/top.xml"),
            "cnbeta": (cnbeta.handler,"http://www.cnbeta.com/backend.php"),
			"powerapple": (powerapple.handler,"http://bbs.powerapple.com/forum.php?mod=rss&auth=0")}