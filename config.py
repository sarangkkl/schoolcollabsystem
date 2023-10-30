# This is the Config file
from pymongo import MongoClient
import os
URI_CONNECTION = "mongodb+srv://tejas22t:Coder123%21@mycluster.gmaql.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"
Client = MongoClient(URI_CONNECTION)
media_path = os.path.join(os.getcwd(), 'media')
media_path2 = os.path.join(os.getcwd(), 'media2')


# print(media_path)

PATH= media_path
PATH2= media_path2