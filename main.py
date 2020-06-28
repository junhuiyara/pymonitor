url = 'https://www.adidas.com.sg/men-running-shoes?sort=price-low-to-high&v_size_en_sg=9_uk'

from urllib.request import Request, urlopen
import pymongo
from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("mongo_user")
password = os.getenv("mongo_password")

req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10).read()
web_word_count = len(webpage)

print(web_word_count)


client = pymongo.MongoClient("mongodb+srv://"+user+":"+password+"@cluster0-nlvco.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["test"]
collection = db["test_collection"]

"""
website_one = {
        'url' : url,
        'word_count' : web_word_count
    }

collection.insert_one(website_one)"""


#collection.update_one({"url":url},{"$set":{"word_count":web_word_count}})

#update the word_count if url and web_word_count doesnt match
collection.update_one({
    'word_count': { "$ne": web_word_count },
    'url': { '$eq': url }
},
{   
    "$set":{"word_count":web_word_count}
})