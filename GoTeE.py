import urllib2, json
from pymongo import MongoClient

conn = MongoClient('lisa.stuy.edu', 27017)
laptopBros = conn.movies

#American Move JSON
R = urllib2.urlopen("https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json")
page = R.read()
dat = json.loads(page)
for i in dat:
    listing = {
        'title' : i["title"],
        'notes' : i["notes"],
        'director' : i["director"],
        'cast' : i["cast"],
        'year' : i["year"],
        'genre' : i["genre"]
    }
    laptopBros.movies.insert_one(listing)
#print dat[0]["title"]
#print json.dumps(dat, indent=4)
#for i in dat:
#    print i
