__author__ = "Francois Maine"
__copyright__ = "Copyright 2020, freedom Partners"
__email__ = "fm@freedom-partners.com"

import os
import markupsafe
import flask
import json

import geocoder
import wikiguide

app = flask.Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

_geo = geocoder.Geocoder()

_wiki_guide = wikiguide.Wikiguide()

@app.route("/", methods=['get'])
@app.route("/find", methods=['get'])
def find():
    response = {}
    items = []
    pages = []
    lat = flask.request.args.get("lat")
    lng = flask.request.args.get("lng")
    addr = flask.request.args.get("address")
    if (lat and lng):
        items = _wiki_guide.geosearch(lat,lng).get('query').get('geosearch')
    elif (addr):
        coords = _geo.geocode(addr)
        lat = coords[0]
        lng = coords[1]
        items = _wiki_guide.geosearch(lat,lng).get('query').get('geosearch')
    response['lat']=lat
    response['lng']=lng
    response['addresse'] = addr
    print(response)
    for item in items :
        pages.append({'url' : _wiki_guide.url_from_id(item['pageid']), 'title' : item['title']})
    response['pages'] = pages
    return flask.render_template('find.html', response=response)

@app.route("/test")
def test():
    return "This is a test"
