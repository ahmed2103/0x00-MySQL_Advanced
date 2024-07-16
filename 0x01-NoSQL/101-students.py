#!/usr/bin/env python3
"""Module restore students mongo collections sorted by AVG score"""


def top_students(mongo_collection):
    """Function restore students mongo collections sorted by AVG score DESC"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"},
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return mongo_collection.aggregate(pipeline)
