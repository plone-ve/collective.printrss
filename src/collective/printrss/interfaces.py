# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.printrss import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectivePrintrssLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRssFeed(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    count = schema.Int(
        title=_(u'Number of items to display'),
        description=_(u'How many items to list.'),
        required=True,
        default=5)

    url = schema.TextLine(
        title=_(u'URL of RSS feed'),
        description=_(u'Link of the RSS feed to display.'),
        required=True,
        default=u'')

    timeout = schema.Int(
        title=_(u'Feed reload timeout'),
        description=_(u'Time in minutes after which the feed should be '
                      u'reloaded.'),
        required=True,
        default=100)
