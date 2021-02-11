from Database import *
import json, os

dbfile = 'db.json'

try:

    db = Database(json.load(open('db.json')))
    rows = db.getall("person", ["name"])
    [print(r[0]) for r in rows]

except Exception as e:

    print('Error: {}'.format(str(e)))

