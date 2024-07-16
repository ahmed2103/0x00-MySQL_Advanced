#!/usr/bin/env python3
"""Module to update topics of a document of MongoDB"""


def update_topics(mongo_collection, name, topics):
    """Function to update topics collection document of MongoDB"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
