from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu', 27017)
DB = c.test
restaraunt = mfDB['restaurants']


def ret_boroughs(borough):
    return restaraunt.find({"borough": borough})

def ret_zip(zip):
    return restaraunt.find({"zip": zip})

def ret_zipGrade(zip, grade):
    zips = ret_zip(zip)
    zip_grades = zips.find({"zip": zip}, {"grade" : grade});
    return zip_grades

def ret_zipMaxgrade(zip, grade):
    zips = ret_zip(zip)
    zip_grades = zips.find({"zip": zip}, {"grade": $lt grade})
    return zip_grades
