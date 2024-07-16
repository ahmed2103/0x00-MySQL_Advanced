#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB:"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    nginx_logs = client.logs.nginx
    cnt = nginx_logs.count_documents({})
    print('{} logs'.format(cnt), 'Methods:', sep='\n')

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt_method = nginx_logs.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, cnt_method))

    print('{} status check'
          .format(nginx_logs.count_documents(
            {"method": "GET", "path": "/status"})), end='')
