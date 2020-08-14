__author__ = "Francois Maine"
__copyright__ = "Copyright 2020, freedom Partners"
__email__ = "fm@freedom-partners.com"

import requests

class Wikiguide():

    def __init__(self):
        pass


    def geosearch(self,lat,lng):
        pageids = []
        baseurl='https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gslimit=100&format=json&gscoord='
        url = "{}{}|{}".format(baseurl,lat,lng)
        response = requests.get(url)
        return response.json()

    def url_from_id(self,pageid):
        return 'https://fr.wikipedia.org/?curid='+str(pageid)
