#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB:"""


def logs_methods_print(nginx_col):
    """function that prints nginx logs stored in MongoDB and methods"""
    cnt = nginx_col.count_documents({})
    print('{} logs'.format(cnt), 'Methods:', sep='\n')

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt_method = nginx_col.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, cnt_method))

    print('{} status check'.format(
        nginx_col.count_documents({
            "method": "GET", "path": "/status"})))


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/').logs.nginx
    logs_methods_print(client)
