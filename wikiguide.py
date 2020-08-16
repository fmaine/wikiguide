__author__ = "Francois Maine"
__copyright__ = "Copyright 2020, freedom Partners"
__email__ = "fm@freedom-partners.com"

import requests

class Wikiguide():

    def __init__(self):
        self._lang = 'fr'

    def textsearch(self,words):
        pageids = []
        baseurl = 'https://'+self._lang+'.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch='
        url = baseurl+words
        response = requests.get(url)
        return response.json()

    def geosearch(self,lat,lng):
        pageids = []
        baseurl='https://'+self._lang+'.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gslimit=100&format=json&gscoord='
        url = "{}{}|{}".format(baseurl,lat,lng)
        response = requests.get(url)
        return response.json()

    def url_from_id(self,pageid):
        return 'https://fr.m.wikipedia.org/?curid='+str(pageid)
