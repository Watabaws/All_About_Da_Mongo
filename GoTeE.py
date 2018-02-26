import urllib2, json
from pymongo import MongoClient

conn = MongoClient('lisa.stuy.edu', 27017)
laptopBros = conn.movies

#American Move JSON
R = urllib2.urlopen("https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json")
page = R.read()
dat = json.loads(page)
print len(dat)
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


def get_title(title):
    return laptopBros.find({'title':title})

def get_director(dir):
    return laptopBros.find({'director': dir})

def get_year(year):
    return laptopBros.find({'year': year})

def get_genre(gen):
    return laptopBros.find({'genre': gen})
