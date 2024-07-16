#!/usr/bin/env python3
"""Module to retrieve all documents from MongoDB"""


def list_all(mongo_collection):
    """Function to retrieve all documents from MongoDB"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
