#!/usr/bin/env python3

"""
getting the top student by average
"""


def top_students(mongo_collection):
    """ getting the top student"""
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    students = list(mongo_collection.aggregate(pipeline))
    return students
