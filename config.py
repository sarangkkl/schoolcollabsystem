# This is the Config file
from pymongo import MongoClient
import os
URI_CONNECTION = "mongodb+srv://tejas22t:Coder123%21@mycluster.gmaql.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"
Client = MongoClient(URI_CONNECTION)
media_path = os.path.join(os.getcwd(), 'media')
files = os.listdir(media_path)

PATH= files