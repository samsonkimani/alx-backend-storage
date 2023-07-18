#!/usr/bin/env python3

"""
updating a document using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """ updating all topics """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
