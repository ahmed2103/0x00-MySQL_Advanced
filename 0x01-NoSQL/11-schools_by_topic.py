#!/usr/bin/env python3
"""Module do specific query based on MongoDB"""


def schools_by_topic(mongo_collection, topic):
    """Function to get all schools by topic"""
    return mongo_collection.find({"topics": {
        "$elemMatch": {"$eq": topic}
    }})
