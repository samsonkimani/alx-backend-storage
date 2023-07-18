#!/usr/bin/env python3

"""
inserting a new document in the collection
"""


def insert_school(mongo_collection, **kwargs):
    """ a function to insert elements in a collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
