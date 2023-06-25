# This is the Config file

from pymongo import MongoClient
import requests, json

URI_CONNECTION = "mongodb+srv://tejas22t:Coder123%21@mycluster.gmaql.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"

Client = MongoClient(URI_CONNECTION, connect=False)
