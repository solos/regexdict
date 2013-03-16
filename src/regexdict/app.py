#!/usr/bin/python
#coding=utf-8

import mako
import pymongo
import config
import json
import bottle
from bottle import response

conn = pymongo.Connection(config.MG_HOST, config.MG_PORT)
redict = conn.redict
redict.authenticate(config.MG_USER, config.MG_PASSWORD)

@bottle.route('/')
@bottle.mako_view("templates/index.html")
def index():
    return dict()

@bottle.route('/re/:regex')
@bottle.mako_view("templates/redict.html")
def query(regex):

    try:
        regex = regex.replace('"', '').replace("'", '')
        regex = '^%s$' % regex
        collection = redict.words.find({"_id": {"$regex": regex}}).limit(config.LIMIT)
        result = []
        for item in collection:
            result.append((item['_id'], item['definition']))
        return dict(result=result)
    except Exception, e:
        print e
        return {}

@bottle.route('/api/re/:regex')
def rapi(regex):

    regex = regex.replace('"', '').replace("'", '')
    regex = '^%s$' % regex
    try:
        collection = redict.words.find({"_id": {"$regex": regex}}).limit(config.LIMIT)
        items = []
        for item in collection:
            items.append((item['_id'], item['definition']))
        response.content_type = 'application/json'
        result = {'code': 1, 'words': items}
    except:
        response.content_type = 'application/json'
        result = {'code': 0, 'words': []}
    return json.dumps(result)

@bottle.route('/static/<filepath:path>')
def static(filepath):
    return bottle.static_file(filepath, root='./static/')

if __name__ == '__main__':
    bottle.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
