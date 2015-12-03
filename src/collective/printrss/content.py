#from plone.app.contenttypes.content import Link
from plone.app.portlets.portlets.rss import RSSFeed
from plone.dexterity.content import Item

FEED_DATA = {}


class RssFeed(Item):

    @property
    def initializing(self):
        """should return True if deferred template should be displayed"""
        feed = self._getFeed()
        if not feed.loaded:
            return True
        if feed.needs_update:
            return True
        return False

    def deferred_update(self):
        """refresh data for serving via KSS"""
        feed = self._getFeed()
        feed.update()

    def update(self):
        """update data before rendering. We can not wait for KSS since users
        may not be using KSS."""
        self.deferred_update()

    def _getFeed(self):
        """return a feed object but do not update it"""
        feed = FEED_DATA.get(self.url, None)
        if feed is None:
            # create it
            feed = FEED_DATA[self.url] = RSSFeed(self.url, self.timeout)
        return feed

    @property
    def siteurl(self):
        """return url of site for portlet"""
        return self._getFeed().siteurl

    @property
    def feedlink(self):
        """return rss url of feed for portlet"""
        return self.url.replace("http://", "feed://")

    @property
    def feedAvailable(self):
        """checks if the feed data is available"""
        return self._getFeed().ok

    @property
    def items(self):
        if self._getFeed().needs_update:
            self._getFeed().update()
        return self._getFeed().items[:self.count]

    @property
    def enabled(self):
        return self._getFeed().ok
