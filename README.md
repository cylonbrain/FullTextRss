#FullTextRss#
===========

## A Google App Engine based Full Text RSS builder ##

Using GAE task queue to queue up each RSS entry. For each RSS source, using customized feed to parse the full text content. Then store into GAE data storage. Feed getting via rss.py and cached when feed served.

To create a new RSS feed source, you need to:
1. Create corresponding rss source in rss_source package
2. Add cron task to specify how frequent to fetch this rss source
3. Register this rss source handler in handler_mapping.py