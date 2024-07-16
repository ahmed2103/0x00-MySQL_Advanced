#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB:"""





if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/').logs.nginx
    logs_methods_print(client)
