#!/usr/bin/env python3
"""Module to insert a new document to a collection MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document to a collection MongoDB"""
    return mongo_collection.insert_one(kwargs).inserted_id
