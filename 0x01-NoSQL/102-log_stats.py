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


def top_10_IPs(nginx_col):
    """function that prints nginx logs stored in MongoDB and methods"""
    ip_pipe = [{
        "$group":
            {
                "_id": "$ip",
                "ip_count": {"$sum": 1}
            }
    },
        {
            "$sort": {"ip_count": -1},
        },
        {
            "$limit": 10
        },
        {
            "$project": {
                "_id": 0,
                "ip": "$_id",
                "ip_count": 1,
            }
        }
    ]
    print('IPs:')
    for top_ip in nginx_col.aggregate(ip_pipe):
        print('\t{}: {}'.format(top_ip['ip'], top_ip['ip_count']))


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/').logs.nginx
    logs_methods_print(client)
    top_10_IPs(client)
