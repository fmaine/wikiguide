"""Wikiguide : Class wrapper to wikipedia search API

Wikipedia search API encapsulation

  Typical usage example:

  wg = wikiguide.Wikiguide()
  pages = wg.textsearch('Paris')
"""
__author__ = "Francois Maine"
__copyright__ = "Copyright 2020, freedom Partners"
__email__ = "fm@freedom-partners.com"

import requests


class Wikiguide():
    """Wikipedia search API wrapper

    Attributes:
        _lang : Wikipedia language code
    """

    def __init__(self, lang='fr'):
        """Default class init """
        self._lang = lang

    def textsearch(self, words: str):
        baseurl = 'https://' + self._lang + '.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&prop=info&inprop=url&srsearch='
        url = baseurl + words
        response = requests.get(url)
        return response.json()

    def geosearch(self, lat: float, lng: float):
        baseurl = 'https://' + self._lang + '.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gslimit=100&format=json&prop=info&inprop=url&gscoord='
        url = "{}{}|{}".format(baseurl, lat, lng)
        response = requests.get(url)
        return response.json()

    def id_to_fullurl(self, pageid):
        baseurl = 'https://' + self._lang + '.wikipedia.org/w/api.php?action=query&format=json&prop=info&inprop=url&pageids='
        url = baseurl + str(pageid)
        response = requests.get(url)
        return response.json()['query']['pages'][str(pageid)]['fullurl']


    def url_from_id(self, pageid):
        return 'https://' + self._lang + '.m.wikipedia.org/?curid=' + str(pageid)
